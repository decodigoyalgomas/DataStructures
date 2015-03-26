from stack import Stack


def infix_to_postfix(infix):
    opstack = Stack()

    infix_list = infix.split()
    postfit_list = []
    prec = {}

    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    for item in infix_list:
        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or item in "0123456789":
            postfit_list.append(item)
        elif item == "(":
            opstack.push(item)
        elif item == ")":
            topItem = opstack.pop()
            while topItem != "(":
                postfit_list.append(topItem)
                topItem = opstack.pop()
        else:
            while not opstack.isEmpty() and prec[opstack.peek()] >= prec[item]:
                postfit_list.append(opstack.pop())
            opstack.push(item)

    while not opstack.isEmpty():
        postfit_list.append(opstack.pop())
    return "".join(postfit_list)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2