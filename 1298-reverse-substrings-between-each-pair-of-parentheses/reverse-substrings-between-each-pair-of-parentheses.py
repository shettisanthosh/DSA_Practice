class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_brackets = []  
        result = []         
        for current_char in s:
            if current_char == '(':
                open_brackets.append(len(result))
            elif current_char == ')':
                start = open_brackets.pop()
                result[start:] = reversed(result[start:])
            else:
                result.append(current_char)
        return "".join(result)
