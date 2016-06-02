class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        operations = set('+-/*')
        operands = []
        for item in A:
            if item not in operations:
                operands.append(item)
            else:
                operand2 = int(operands.pop())
                operand1 = int(operands.pop())
                if item == '+':
                    operands.append(operand1+operand2)
                elif item == '-':
                    operands.append(operand1-operand2)
                elif item == '*':
                    operands.append(operand1*operand2)
                elif item == '/':
                    try:
                        operands.append(operand1/operand2)
                    except ZeroDivisionError:
                        return
        return operands.pop()


s = Solution()
print(s.evalRPN("12*3-5+"))
