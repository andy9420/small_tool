def detect_document(path):
    """Detects document features in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

def detect_text(path,file_name):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')
    all_text = []
    first = True
    img = cv2.imread(path)
    for text in texts:
        #print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('{} bounds: {}'.format(text.description,','.join(vertices)))

        #all_text += '{}\n'.format(','.join(vertices))

        
        if first:
            #all_text += '{} \n'.format(','.join(vertices))
            first = False
        else:
            #all_text += '{}  bounds: {} \n'.format(text.description,','.join(vertices))
            all_text.append('{}'.format(','.join(vertices)))

    
    for line in range(len(all_text)):
        point = []
        #print(str(all_text[line]).replace('(','').replace(')','').split(','))
        points = str(all_text[line]).replace('(','').replace(')','').split(',')
        point.append([int(points[0]),int(points[1])])
        point.append([int(points[4]),int(points[5])])
        img = cv2.rectangle(img, tuple(point[0]), tuple(point[1]), (0,255,0), 2)

    cv2.imwrite('/home/cvlab/下載/google_img_result/' + file_name + '.jpg', img)
    cv2.namedWindow("image")
    cv2.imshow('image', img)
    cv2.waitKey(0)
    



    '''resule_file_name = '/home/cvlab/下載/google_txt/' + file_name + '.txt'
    fp = open(resule_file_name,'w')
    fp.write(all_text)
    fp.close()'''

    #print(all_text)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

if __name__ == '__main__':
    import os
    from google.cloud import vision
    import io
    import cv2
    #detect_document('/home/cvlab/ContourNet/datasets/ic15/ic15_test_images/0000001.jpg')
    #detect_text('/home/cvlab/ContourNet/datasets/ic15/ic15_test_images/0000001.jpg')
    for dirPath, dirNames, fileNames in os.walk("/home/cvlab/下載/google/"):
        print (dirPath)
        for f in fileNames:
            detect_text(os.path.join(dirPath, f), f[:-4])
            #print(f[:-4])