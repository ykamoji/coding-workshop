s = "()(()"

str_len = len(s)


def validSequence():

    stack = [-1]
    max_length = 0

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length


print(f"Longest Sequence length = {validSequence()}")

