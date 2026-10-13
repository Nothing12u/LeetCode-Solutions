'''OPENING_BRACKETS = ['(', '[', '{']
CLOSING_BRACKETS = [')', ']', '}']'''
class Solution:
    def isValid(self, s: str) -> bool:
        '''stack_brackets = []
        for ch in s:
            if ch in CLOSING_BRACKETS:
                if len(stack_brackets) == 0: return False 
                st_top = stack_brackets[len(stack_brackets)-1]
                if (
                    (st_top == '(' and ch == ')') or
                    (st_top == '[' and ch == ']') or
                    (st_top == '{' and ch == '}')
                    ):
                    stack_brackets.pop()
                else:
                    stack_brackets.append(ch)
            else:
                stack_brackets.append(ch)
        return len(stack_brackets) == 0'''
        ope=[]
        for i in range(len(s)):
            if s[i]=='[' or s[i]=='(' or s[i]=='{':
                ope.append(s[i])
           
            elif ope and ((ope[len(ope)-1]=='{' and s[i]=='}') or (ope[len(ope)-1]=='(' and s[i]==')') or (ope[len(ope)-1]=='[' and s[i]==']')):
                ope.pop(len(ope)-1)
            else:
                return False
        return len(ope)==0