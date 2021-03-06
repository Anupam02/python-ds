"""
Use a stack data structure to convert integer values to binary

Example: 242

242 / 2 = 121 -> 0
121 / 2 = 60  -> 1
60 / 2  = 30  -> 0
30 / 2  = 15  -> 0
15 / 2  = 7   -> 1
7 / 2   = 3   -> 1
3 / 2   = 1   -> 1
1 / 2   = 0   -> 1
"""

from stack import Stack


def div_by_2(dec_num):
    s = Stack()
    bin_num = ''
    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num//2

    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num


def main():
    test_cases = [242, 2, 1, 4]
    for case in test_cases:
        assert div_by_2(case) == bin(case)[2:]

if __name__ == '__main__':
    main()

