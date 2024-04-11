for i in range(3) :
    a, b, c, d = map(int,input().split())

    h = a + b + c + d 

    if h == 0 :
        print('D')
    elif h == 1 :
        print('C')
    elif h == 2 :
        print('B')
    elif h == 3 :
        print('A')
    elif h == 4 :
        print('E')

    continue