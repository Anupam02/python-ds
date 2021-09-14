from stack import Stack


def reverse_string(string: str) -> str:
    s = Stack()
    rev_str = ''
    for letter in string:
        s.push(letter)

    while s.is_empty():
        top = s.pop()
        rev_str += top

    return rev_str


def main():
    test_cases = ['this', 'is', 'a', 'specific', 'stack', 'implementation', 'question']
    for case in test_cases:
        assert reverse_string(case) == case[::-1]
    