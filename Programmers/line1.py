import collections
def solution(inputString):
    answer = 0
    left_stack = collections.deque()
    right_stack = collections.deque()
    for i in inputString:
        if i == '(' or i == '{' or i == '[' or i == '<':
            left_stack.append(i)
        elif i == ')' or i == '}' or i == ']' or i == '>':
            right_stack.append(i)
            while len(left_stack) > 0 and len(right_stack) > 0 and left_stack[-1] == right_2_left(right_stack[-1]):
                left_stack.pop()
                right_stack.pop()
                answer += 1
    if len(left_stack) > 0 or len(right_stack) > 0:
        return -1
    
    return answer

def right_2_left(r):
    if r == ')':
        return '('
    if r == '}':
        return '{'
    if r == ']':
        return '['
    if r == '>':
        return '<'
    return ''

print(solution("line [plus]"))