import os 


while(True):
    path = input("Enter path to count file num, Enter 'E' close program:")
    if path == 'E':
        break 
    
    #count file num
    for dirPath, dirNames, fileNames in os.walk(path):
        print(len(fileNames))
        break
    
    '''
    #get shell command
    copy_save_path = input("Enter save file path:")
    copy_file_num = input("Enter need copy file num:")
    for dirPath, dirNames, fileNames in os.walk(path):
        name = ""
        for i in range(int(copy_file_num)):
            name += fileNames[i] + ' '
        print("cp " + name + copy_save_path)
        break
    '''


