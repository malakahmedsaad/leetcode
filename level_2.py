# Q: How do you remove duplicates from a list?
# A: I created a new list and added elements only if they weren't already in it.
#
# def remove_duplicates(numbers):
#     noduplicates = []
#     for i in numbers:
#         if i not in noduplicates:
#             noduplicates.append(i)
#     return noduplicates
#
# print(remove_duplicates([1, 2, 2, 3, 4, 1, 5]))


# Q: How do you find the missing number in a sequence?
# A: I sorted the list and checked for the first gap in the sequence by comparing neighbors.
#
# def find_missing_number(nums):
#     nums.sort()
#     for i in range(len(nums) - 1):
#         if nums[i+1] != nums[i] + 1:
#             return nums[i] + 1
# print(find_missing_number([4,5,7,8]))


# Q: How do you count the vowels in a string?
# A: I converted the sentence to lowercase, then checked each character against a list of vowels.
#
# def count_vowels(sentence):
#     counter = 0
#     vowels = ['i', 'e', 'a', 'o', 'u']
#     for i in sentence.lower():
#         if i in vowels:
#             counter += 1
#     return counter
# print(count_vowels("PYTHoN"))


# Q: How do you check if two words are anagrams?
# A: I sorted both words alphabetically and compared them.
#
# def is_anagram(word1,word2):
#     sorted1 = sorted(word1)
#     sorted2 = sorted(word2)
#     if sorted1 == sorted2:
#         return True
#     else:
#         return False
# print(is_anagram("listjen", "silent"))


# Q: How do you get all odd numbers from a list?
# A: I looped through the list and added numbers that are not divisible by 2.
#
# def find_odds(nums):
#     odds = []
#     for i in nums:
#         if i % 2 != 0:
#             odds.append(i)
#     return odds
#
# print(find_odds([1, 2, 3, 4, 5, 6]))


# Q: How do you count how many times each word appears in a sentence?
# A: I split the sentence into words and used a dictionary to keep track of word counts.
#
# def word_frequency(sentence):
#     words = sentence.split()
#     counter = {}
#     for i in words:
#         if i in counter:
#             counter[i] += 1
#         else:
#             counter[i] = 1
#     return counter
# print(word_frequency("the cat and the dog"))


# Q: How do you do the same word frequency task using a Python library?
# A: I used the Counter class from the collections module to simplify counting.
#
# from collections import Counter
# def word_frequency(sentence):
#     words = sentence.split()
#     return dict(Counter(words))
# print(word_frequency("the cat and the dog"))


# Q: How do you find the longest word in a sentence?
# A: I split the sentence and compared word lengths, updating the longest found so far.
#
# def longest_word(sentence):
#     words = sentence.split()
#     longest = ""
#     for y in words:
#         if len(y) > len(longest):
#             longest = y
#     return longest
#
# print(longest_word("The quick brown fox jumpsi"))


# Q: How do you check if a number is prime?
# A: I returned False for numbers <= 1 and checked divisibility from 2 up to √num.
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2,int(num**0.5)):
#         if num % i == 0:
#             return False
#
#     return True
# print(is_prime(7))
# print(is_prime(10))


# Q: How do you find the second largest number?
# A: I tracked the largest and second largest while looping through the list.
#
# def second_largest(nums):
#     largest = 0 # or float('-inf') for negatives
#     second = 0
#     for i in nums:
#         if i > largest:
#             second = largest
#             largest = i
#         elif i > second:
#             second = i
#     return second
# print(second_largest([3, 1, 4, 5, 2]))
# print(second_largest([10, 20, 9]))


# Q: How do you check if parentheses are balanced?
# A: I used a counter that goes up for '(', down for ')', and made sure it never goes negative and ends at zero.
#
# def valid_parantheses(sentence):
#     count = 0
#     for i in sentence:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -= 1
#         if count < 0:
#             return False  # too many closing parentheses
#     return count == 0  # all opened ones are closed
# 
# print(valid_parantheses("())("))
