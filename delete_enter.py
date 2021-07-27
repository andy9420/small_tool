while True:
    result = ''
    while True:
        a = ''
        a = input().replace('\n','')
        if a == 'E':
            print(result)
            result = ''
            break
        result += a + ' '
 

        