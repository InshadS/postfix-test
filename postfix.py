def postfix_evaluation(s):
    stack= []

    if not len(s):
        return None

    for i in s:
        if i.isdigit():
            stack.append(int(i))

        elif i== "+":
            num1= stack.pop()
            num2= stack.pop()
            stack.append(num1+num2)

        elif i== "-":
            num1= stack.pop()
            num2= stack.pop()
            stack.append(num1-num2)

        elif i== "/":
            num1= stack.pop()
            num2= stack.pop()
            stack.append(num1/num2)

        elif i== "*":
            num1= stack.pop()
            num2= stack.pop()
            stack.append(num1*num2)

        else:
            return None

    return stack[0]

# if __name__ == '__main__':
#     s = '123++'
#     print(postfix_evaluation(s))
