s = input()

if s != "":
    stack_1 = []
    for i in s:
        a_dict = {'(': ')', '[': ']', '{': '}'}
        try:
            if i == '(' or i == '[' or i == '{':
                stack_1.append(i)
            else:
                if i == a_dict[stack_1[len(stack_1) - 1]]:
                    stack_1.pop()
                else:
                    print(False)
                    break
        except:
            print(False)
            break
    else:
        if stack_1 == []:
            print(True)
        else:
            print(False)
else:
    print(True)