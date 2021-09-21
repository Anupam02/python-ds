#  Given a word convert it to numeronym. 
# 
#  example:
#  kubernetes -> k8s
#  internationalization -> i18n
# 
#  convert string to all possible numeronym
# 
#  Input: better
#  Output: ['b2ter', 'be2er', 'bet2r', 'b3er', 'be3r', 'b4r']
#  Input: cricket
#  Output: ['c2cket', 'cr2ket', 'cri2et', 'cric2t', 'c3ket', 'cr3et', 'cri3t', 'c4et', 'cr4t', 'c5t']
import unittest


def solve(input_str: str) -> list:
    result_list = []
    if len(input_str) <= 3:
        return result_list
    extracted_word = input_str[1:-1]
    sliding_window_size = 2
    while sliding_window_size <= len(input_str) - 2:
        for i in range(len(extracted_word) - sliding_window_size + 1):
            _neuronym = f"{input_str[0:i+1]}{sliding_window_size}{input_str[sliding_window_size+i+1: len(input_str)]}"
            result_list.append(_neuronym)
        sliding_window_size += 1
    return result_list


class TestNeuronym(unittest.TestCase):
    def setUp(self):
        self.result = solve("better")
        self.expected = ['b2ter', 'be2er', 'bet2r', 'b3er', 'be3r', 'b4r']
    
    def test_count_equal(self):
        self.assertCountEqual(self.result, self.expected)
    
    def test_list_eq(self):
        self.assertListEqual(self.result, self.expected)
        

if __name__ == '__main__':
    unittest.main()
