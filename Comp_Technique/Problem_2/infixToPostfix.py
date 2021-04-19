import re

class MyClass:
    def __init__(self):
        self.item = []
        self.tokensArray = []

    def push(self,it):
        self.item.append(it)

    def peek(self):
        if self.isempty() == True:
            return 0
        return self.item[-1]

    def pop(self):
        if self.isempty() == True:
            return 0
        return(self.item.pop())
    
    def popTwice(self):
        self.pop()
        self.pop()

    def length(self):
        return (len(self.item))
        
    def topChar(self):
        return self.item[len(self.item ) - 1]

    def firstTwoChar(self):
        return (self.item[len(self.item) - 1], self.item[len(self.item) - 2])

    def expToken(self, exp):
        operators = '+-*/()^'
        tokens = []
        for char in exp:
            if char in operators:
                tokens.append(char)
            elif char == ' ':
                continue 
            elif re.findall('^(\d+)$', char):
                if (len(tokens) == 0 or tokens[len(tokens) - 1] in operators):
                    tokens.append(char)
                else:
                    tokens[len(tokens) - 1] += char
        self.tokensArray = tokens
             

    def isempty(self):
        if self.item == []:
            return True
        else:
            return False


    def isOperand(self, ch): 
        return re.findall('^(\d+)$', ch)

    def notGreater(self, i):
        precedence = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}
        print(self.peek())
        if self.peek() == '(':
            return False
        a = precedence[i]
        b = precedence[self.peek()] 
        if a  <= b:
            return True
        else:
            return False

    def infixToPostfix(self, infixExp):
        self.expToken(infixExp)
        output = []
        
        for i in self.tokensArray:
            
            if self.isOperand(i): # check if operand add to output
                print(i, "~ Operand pushed to stack")
                output.append(i)

            # If the character is an '(', push it to stack 
            elif i  == '(':
                self.push(i)
                print(i, "~ Found ( push into stack")

            elif i == ')':  # if ')' pop till '('
                while( self.isempty() != True and self.peek() != '('):
                    n = self.pop() 
                    output.append(n)
                    print(n, "~ Operand popped from stack")
                if (self.isempty() != True and self.peek() != '('):
                    print("______________________")
                    return -1
                else:
                    x = self.pop()
                    print(x, "Popping and deleting (")
            else: 
                while(self.isempty() != True and self.notGreater(i)):
                    n = self.pop()
                    output.append(n)
                    print(n, "Operator popped after checking precedence from stack")
                self.push(i)

        # pop all the operator from the stack 
        while self.isempty() != True:
            xx = self.pop()
            output.append(xx)
            print(xx,"~ pop at last")
        print(' '.join(output))
        return output
    
    def evaluatePostfix(self, exp):
        operators = '+/*^-'
        for char in exp:
            if st.isOperand(char):
                st.push(char)
            
            elif char in operators:
                first_two_chars = st.firstTwoChar()
                res = 0
                if (char == '+'):
                    res = int(first_two_chars[1]) + int(first_two_chars[0])
                elif (char == '*'):
                    res = int(first_two_chars[1]) * int(first_two_chars[0])
                elif (char == '-'):
                    res = int(first_two_chars[1]) - int(first_two_chars[0])
                elif (char == '/'):
                    res = int(first_two_chars[1]) / int(first_two_chars[0])
                elif (char == '^'):
                    res = int(first_two_chars[1]) ** int(first_two_chars[0])

                st.popTwice()
                st.push(res)

        return st.topChar()

st = MyClass()
infixVal = input("Please enter your infix expression: \n")
postfix_exp = st.infixToPostfix(infixVal)

evaluation = st.evaluatePostfix(postfix_exp)
print(evaluation)