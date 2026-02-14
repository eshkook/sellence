from typing import List, Optional

def reverse_string(s: str) -> str:
    """
    Reverse a string without using built-in reverse methods.
    
    Args:
        s: Input string to reverse
        
    Returns:
        Reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Write a function that takes a list of integers and a target sum, and returns the indices of two numbers that add up to the target. 
# You can assume there's exactly one solution, and you can't use the same element twice.
def two_sum(int_list: List[int], target_sum: int) -> Optional[List[int]]:
    """
    takes a list of integers and a target sum, and returns the indices of two numbers that add up to the target. 
    
    Args:
        int_list: Input list of integers
        target_sum: Input sum target integer
        
    Returns:
        indices of two numbers that add up to the target, or None. 
    """
    # O(n^2) approach:
    # for index_1 in range(len(int_list)):
    #     for index_2 in range(index_1 + 1, len(int_list)):
    #         if int_list[index_1] + int_list[index_2] == target_sum:
    #             return [index_1, index_2]

    # O(n) approach:
    seen = {}  # value -> index
    for i, num in enumerate(int_list):
        complement = target_sum - num
        if complement in seen: # O(1) time, because all it does is check whether a key has any value in a dict
            return [seen[complement], i]
        seen[num] = i
            
    return None

# Write a function that takes a string and returns True if it's a palindrome 
# (reads the same forwards and backwards), False otherwise. Ignore spaces, punctuation, and capitalization.
def is_palindrome(s: str) -> bool:

    s = s.lower()

    forward_index = 0
    reverse_index = len(s) - 1
    while True:
        while True:
            if forward_index >= len(s):
                return True
            if not s[forward_index].isalnum():
                forward_index += 1
            else:
                break
        while True:
            if reverse_index < 0:
                return True
            if not s[reverse_index].isalnum():
                reverse_index -= 1
            else:
                break
        if forward_index >= reverse_index: 
            return True
        if s[forward_index] != s[reverse_index]:
            return False
        forward_index += 1
        reverse_index -= 1

# Write a function that takes a list containing n distinct numbers from the range 0 to n, with one number missing. 
# Find and return the missing number.
def missing_number(numbers: List[int]) -> int:
    n = len(numbers)
    expected = n * (n + 1) // 2
    return expected - sum(numbers)   

# Write a function that takes an integer n and returns a list of strings representing numbers from 1 to n, 
# with the following rules:
# For multiples of 3, use "Fizz" instead of the number
# For multiples of 5, use "Buzz" instead of the number
# For multiples of both 3 and 5, use "FizzBuzz"
# Otherwise, use the number as a string
def fizzbuzz(number: int) -> List[str]:
    output = []
    for num in range(1, number + 1):
        s = ''
        if not num % 3:
            s += 'Fizz'
        if not num % 5:
            s += 'Buzz'
        if not s:
            s = str(num)
        output.append(s)
    return output

# Write a function that takes a string and returns a dictionary where keys are characters 
# and values are their frequency counts in the string.
def char_frequencies(s: str) -> dict:
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

# Write a function that takes a string and returns the first character that appears only once. 
# If no such character exists, return None.
def first_single_char(s: str) -> Optional[str]:
    for char, freq in char_frequencies(s).items():
        if freq == 1:
            return char
    return None

# Write a function that takes two sorted lists of integers and merges them into a single sorted list. 
# Don't use the built-in sort() or sorted() functions.
def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    merged_list = []
    len1 = len(list1)
    len2 = len(list2)
    index1 = 0
    index2 = 0
    while True:
        if index1 == len1:
            merged_list += list2[index2:]
            return merged_list
        if index2 == len2:
            merged_list += list1[index1:]
            return merged_list
        if list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1

# Write a function that takes a sorted list of integers and removes duplicates in-place, 
# returning the new length of the list. The relative order of elements should be kept the same, 
# and you should modify the input list so that the first k elements contain the unique values (where k is the returned length).
def remove_dups(numbers: List[int]) -> List[int]:
    seen = {}
    index = 0
    while index < len(numbers):
        if numbers[index] in seen:
            numbers = numbers[:index] + numbers[index + 1:]
        else:
            seen[numbers[index]] = 1
            index += 1
    return(numbers)

# Write a function that takes two strings and returns True if they are anagrams of each other 
# (contain the same characters with the same frequencies), False otherwise. Ignore spaces and capitalization.
def are_anagrams(str1: str, str2: str) -> bool:
    str1 = str1.lower()
    str2 = str2.lower()
    
    freq1 = {}
    freq2 = {}

    for char in str1:
        if not char.isalnum():
            continue
        freq1[char] = freq1.get(char, 0) + 1
    for char in str2:
        if not char.isalnum():
            continue
        freq2[char] = freq2.get(char, 0) + 1

    return freq1 == freq2

# Write a function that takes a list of strings and groups the anagrams together. 
# Return a list of lists, where each inner list contains strings that are anagrams of each other.
def group_anagrams(list_strings: List[str]) -> List[List]:
    group_anagrams = []
    d = [(s, char_frequencies(s)) for s in list_strings]
    for (s, freq) in d:
        found = False
        for (str_list, freq_list) in group_anagrams:
            if freq == freq_list:
                str_list.append(s)
                found = True
                break
        if not found:
            group_anagrams.append(([s], freq))

    group_anagrams = [str_list for (str_list, freq_list) in group_anagrams]
    return group_anagrams

def fast_group_anagrams(list_strings: List[str]) -> List[List]:
    seen = {}
    for s in list_strings:
        sorted_s = tuple(sorted(s))
        if sorted_s in seen:
            seen[sorted_s].append(s)
        else:
            seen[sorted_s] = [s]
        
    return list(seen.values())

# class ClassName:
#     def __init__(self, param1: type1, param2: type2):
#         """Initialize the class with parameters."""
#         self.attribute1 = param1
#         self.attribute2 = param2
    
#     def method_name(self, param: type) -> return_type:
#         """Method description."""
        
#         return result

# Implement a Stack class with the following methods:
# __init__(): Initialize an empty stack
# push(value: int) -> None: Add an element to the top of the stack
# pop() -> Optional[int]: Remove and return the top element (return None if stack is empty)
# peek() -> Optional[int]: Return the top element without removing it (return None if stack is empty)
# is_empty() -> bool: Return True if the stack is empty
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> Optional[int]:
        return self.stack.pop()
    
    def peek(self) -> Optional[int]:
        last = self.stack[-1] if len(self.stack) else None
        return last
    
    def is_empty(self):
        return not bool(self.stack)

if __name__ == "__main__":
    s = Stack()
    
    print(s.is_empty())
    s.push(9)
    print(s.pop())
    # print(s.peek())

    # print(fast_group_anagrams(['asd', 'sda', 'ss']))
    # print(group_anagrams(['asd', 'sda', 'ss']))
    # print(are_anagrams('sggg', 'g sgg'))
    # print(remove_dups([1,3,4,1,6,7,3,98]))
    # print(merge_sorted_lists([1,3,4,7,8], [2,3,5,9]))
    # print(first_single_char('sskd'))
    # print(char_frequencies('anjsua'))
    # print(fizzbuzz(5))
    # print(missing_number([0,1,2,3]))
    # print(is_palindrome('ads dA'))
    # print(two_sum([1,2,3,4,5], 4))
    # print(reverse_string("hello"))
    