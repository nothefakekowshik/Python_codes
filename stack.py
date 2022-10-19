def func(str):
    stack = []
    top = -1
    result = True
    for e in str:
        if (e == '(' or e == '{' or e == '['):
            stack.append(e)
            top += 1
        else:
            if (e == ')' and stack[top] == '('):
                stack.pop()
                top -= 1
            elif (e == ']' and stack[top] == '['):
                stack.pop()
                top -= 1
            elif (e == '}' and stack[top] == '{'):
                stack.pop()
                top -= 1
            else:

                result = False
    if result == True and top == -1:
        print('balanced')
    else:
        print('not balanced')
    print(stack)


def main():
    t = int(input())
    while t:
        str = input()
        func(str)
        t -= 1


if __name__ == '__main__':
    main()