class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
                continue
            y=stack.pop()
            x=stack.pop()   
            result=0
            if token =="+":
                result=x+y 
            elif token =="-":
                result=x-y 
            elif token =="/":
                result=int(x/y) 
            elif token =="*":
                result=x*y
            stack.append(result)
        return stack.pop()
        