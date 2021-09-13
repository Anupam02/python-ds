"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.

Example:
    (), ()(), (({[]})) < - balanced
    ((), (())))        < - unbalanced
"""
from stack import Stack

open_close_brackets_map = {
    ")": "(",
    "}": "{",
    "]": "["
}


def check_balanced_parenthesis(paren_string: str):
    s = Stack()
    for bracket_sign in paren_string:
        if bracket_sign in open_close_brackets_map.values():
            s.push(bracket_sign)
        elif bracket_sign in open_close_brackets_map.keys():
            complementary_bracket = open_close_brackets_map.get(bracket_sign)
            if s.peek() == complementary_bracket:
                s.pop()
    if s.is_empty():
        return True
    return False


def main():
    assert check_balanced_parenthesis('(())')
    assert not check_balanced_parenthesis('(()')


if __name__ == '__main__':
    main()