while True:
    data = input()
    if data=='.':
        break
    else:
        stack = []
        for chr in data:
            if chr=='(':
                stack.append(')')
            elif chr=='[':
                stack.append(']')
            elif chr==')' or chr==']':
                try:
                    temp = stack.pop()
                    if chr != temp:
                        print('no')
                        break
                except IndexError:
                    print('no')
                    break
            elif chr=='.':
                print('no' if stack else 'yes')
                break