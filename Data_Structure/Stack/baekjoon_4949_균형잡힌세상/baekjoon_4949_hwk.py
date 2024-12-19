while True:
    string = input()
    if string=='.': break
    stack = []

    for chr in string:
        if chr =='(' or chr=='[':
            stack.append(chr)
        elif chr==')' or chr==']':
            if not len(stack):
                print('no')
                break
            poped_str = stack.pop()
            if chr==')' and poped_str=='[':
                print('no')
                break
            elif chr==']' and poped_str=='(':
                print('no')
                break
    else:
        if len(stack):
            print('no')
        else:
            print('yes')
