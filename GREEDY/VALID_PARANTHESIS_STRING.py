def isValid(s: str) -> bool:
    def recurse(index: int, open_count: int) -> bool:
        # If we've reached the end of the string, check if the parentheses are balanced
        if index == len(s):
            return open_count == 0
        
        # If at any point the open_count is negative, return False (more ')' than '(')
        if open_count < 0:
            return False
        
        # Process the current character
        if s[index] == '(':
            # Consider it as an opening parenthesis
            return recurse(index + 1, open_count + 1)
        elif s[index] == ')':
            # Consider it as a closing parenthesis
            return recurse(index + 1, open_count - 1)
        elif s[index] == '*':
            # Explore all three possibilities for '*'
            return (recurse(index + 1, open_count + 1) or  # Treat '*' as '('
                    recurse(index + 1, open_count - 1) or  # Treat '*' as ')'
                    recurse(index + 1, open_count))        # Treat '*' as ''
        
        # In case of invalid input, just return False (not expected in this problem)
        return False
    
    # Start recursion from index 0 with 0 open parentheses
    recur_value = recurse(0, 0)
    print("recur value is {}".format(recur_value))

    def dp_memo(dp,index,count):
        if index == len(s):
            if count == 0:
                return True
            else:
                return False
        
        if count < 0:
            return False

        if dp[index][count] != -1:
            return dp[index][count]
        
        if s[index] == '(':
            dp[index][count] = dp_memo(dp, index + 1, count + 1)
        elif s[index] == ')':
            dp[index][count] = dp_memo(dp, index + 1, count - 1)
        elif s[index] == '*':
            dp[index][count] = (dp_memo(dp, index + 1, count + 1) or  
                                dp_memo(dp, index + 1, count - 1) or 
                                dp_memo(dp, index + 1, count))     
            
        return dp[index][count]
        
        
    n = len(s)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    val = dp_memo(dp,0,0)
    print("memo value is {}".format(val))

def checkValidString(s: str) -> bool:
    # First pass (left to right)
    open_count = 0
    for char in s:
        if char == '(' or char == '*':
            open_count += 1
        else:  # char == ')'
            open_count -= 1
        if open_count < 0:
            return False
    
    # Second pass (right to left)
    close_count = 0
    for char in reversed(s):
        if char == ')' or char == '*':
            close_count += 1
        else:  # char == '('
            close_count -= 1
        if close_count < 0:
            return False
    
    return True


stri = "(*(("
isValid(stri)
print(checkValidString(stri))