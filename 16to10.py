while True:
    try:
        a = input("輸入16進制色碼：")
        b = []
        for i in range(len(a)):
            if a[i] == 'A' or a[i] == 'a':
                b.append(10)
            elif a[i] == 'B' or a[i] == 'b':
                b.append(11)
            elif a[i] == 'C' or a[i] == 'c':
                b.append(12)
            elif a[i] == 'D' or a[i] == 'd':
                b.append(13)
            elif a[i] == 'E' or a[i] == 'e':
                b.append(14)
            elif a[i] == 'F' or a[i] == 'f':
                b.append(15)
            else:
                b.append(int(a[i]))
        
        R = 16 * b[0] + b[1]
        G = 16 * b[2] + b[3]
        B = 16 * b[4] + b[5]

        print('R:' + str(R) + ' G:' + str(G) + ' B:' + str(B))
    
    except:
        print('輸入錯誤')