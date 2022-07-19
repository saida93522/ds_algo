# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


# Invalid ----> ([[])] order not matching
# Invalid ----> ([) 
# Invalid ----> {(}()) 


# Solution: last have LIFO behaviour,we keep track of the open brackets but more importantly we track the most recent open bracket to match it to the next closing bracket. we remove the last left parenthesis matched to the next closing brackets from the stack.

# Time Complexity: O(n) n= # of char in string as n increases runtime scale in linear fashion
# Space Complexity: O(n) # scale linearly with the input

# worst case if string is valid: O(n). if n = 8 then the max element stack holds is 4 we store half of n, however it still scales linearly. if n = 8,stack = 4, if n = 10 stack = 5 i.e.
# //
# worst case if invalid:  O(n), if n ONLY holds open brackets,then we are going to push all the items in the stack n times. if n holds 1000 open brackets, stack will hold 1000 open brackets
#
#
#
#


def valid_par(s):
    stack = []
    for i in s:
        # push left brackets to the stack 
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            # if stack is empty there is no open/left brackets to match to == invalid Parenthese     
            if len(stack) == 0:
                return False
            # if stack is not empty, then at this point i must be a right bracket, ')','}',']'

            # peek the top of the stack to ensure most recent open bracket in the stack matches the right bracket[i]

            # if it is not match, Parenthese are not balanced return false
            if i == '}' and stack[-1] != '{' or i == ')' and stack[-1] != '(' or i == ']' and stack[-1] != '[':
                return False
            # we found a match,{},[],() --> remove from the stack.. continue until we removed all matching brackets
            else:
                stack.pop()
    return len(stack) == 0



print(valid_par("([[])"))