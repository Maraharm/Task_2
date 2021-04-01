def is_balanced():
    text = input("Введите строку>>")
    otkr = [input("Введите скобки>>")]
    brackets = "〈〉()[]{}"
    closing = []
    for character in otkr:
        if character == '<':
            closing.append('>')
        if character == '(':
            closing.append(')')
        if character == '[':
            closing.append(']')
        if character == '{':
            closing.append('}')
    print(closing)
    stack = [] # keep track of opening brackets types
    for character in text:
        if character in otkr: # bracket
            stack.append(otkr.index(character))
            print(stack)
        elif character in closing: # bracket
            if stack and stack[-1] == closing.index(character):
                stack.pop()  # remove the matched pair
            else:
                return False # unbalanced (no corresponding opening bracket) or
                             # unmatched (different type) closing bracket
    return True

is_balanced()