# Given an array of integers,
# write a function that returns the largest sum of non-adjacent numbers.
#  Numbers can be 0 or negative.For example,
# array = [1 , 2, 3, 1]
# here possible combinations could be 
# array[0], array[2] = 1, 3 ==> 4(1+3)
# array[0], array[3] = 1, 1 ==> 2(1+1)
# array[1], array[3] = 2, 1 ==> 3(2+1)

# maximus is 4 , which is made by taking array[0] and array[2]
# hence answer is 4

# solution
# start from the base case


# f(1)  = 1         ---> 1
# f(2)  = 1, 2      ---> 2
# f(3)  = 1, 2, 3   ---> max(f(3-2)+3 , f(3-1)) = 4, where 3 is newly added element
# f(4)  = 1, 2, 3, 1 ----> max(f(4-2)+ 1, f(4-1)) = 4, where 4 is the newly added element

def solve(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])
 
    memoize = [0]*len(arr)
    memoize[0] = arr[0]
    memoize[1] = max(arr[1], memoize[0])

    for i in range(2, len(arr)):
        item = arr[i]
        memoize[i] = max(memoize[i-2]+item, memoize[i-1])
    
    return memoize[-1]


def main():
    test_cases = [
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 1]
    ]
    for case in test_cases:
        answer = solve(case)
        print(case, answer)

if __name__ == '__main__':
    main()