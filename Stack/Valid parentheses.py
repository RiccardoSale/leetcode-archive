"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        map_ = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c not in map_:  # append only open parantheses e continuo ad appenderle
                stack.append(c)
                continue
            if not stack or stack[-1] != map_[c]:
                # se e vuoto o se l'ultimo elemento non è uguale da quello mappato da c
                return False
                # dato che se e vuoto e mi trovo una parentesi chiusa ERRORE
            stack.pop()
        return not stack  # not stack return True if there are no element remaining
        # we do not want close parentheses 