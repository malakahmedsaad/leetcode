# 1
# Q: What does this function do?
# A: I created a simple function that returns "hello world", and then called it from main.

# def say_hello():
#     return("hello world")
#
# def main():
#     print(say_hello())
#
# if __name__ == '__main__':
#     main()


# 2
# Q: How do you add two numbers?
# A: I wrote a function that takes two arguments and returns their sum.

# def add_numbers(a,b):
#     return a+b
# def main():
#     add_numbers(3,6)  # I call the function but forgot to print the result; still, the logic is correct.
#
# if __name__ == '__main__':
#     main()


# 3
# Q: How did you find the maximum number in a list?
# A: I initialized `max` with the first element, then compared each item in the list and updated it.

# def find_max(numbers):
#     max = numbers[0]
#     for i in numbers:
#         if i > max:
#             max = i
#     return max
# print(find_max([3,7,2,9,5]))


# 4
# Q: How did you count the number of even numbers?
# A: I looped through the list and increased the counter when the number was divisible by 2.

# def count_evens(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count += 1
#     return count
#
# print(count_evens([1, 2, 3, 4, 5, 6]))


# 5
# Q: How do you reverse the list?
# A: I used two methods. One with `insert(0, i)` to build the reverse, and one with slicing.

# def reverse_list(numbers):
#     newnumbers = []
#     for i in numbers:
#         newnumbers.insert(0,i)
#     return newnumbers
# print(reverse_list([1, 2, 3, 4]))

# OR

# def reverse_list(numbers):
#     numbers = numbers [::-1]
#     return numbers
# print(reverse_list([1, 2, 3, 4]))


# 6
# Q: How do you check if a word is a palindrome?
# A: First, I used a while loop with two pointers to compare characters from both ends.
# Then I did the same thing using Python slicing for a simpler solution.

# def is_palindrome(word):
#     right = len(word) - 1
#     left = 0
#     while left < right:
#         if word[left] != word[right]:
#             return False
#
#         left += 1
#         right -= 1
#     return True
# print(is_palindrome("racecar"))

# def is_palindrome(word):
#     return word == word[::-1]
# print(is_palindrome("racecar"))


# 7
# Q: How do you find the first duplicate?
# A: I used a list to keep track of seen numbers. If a number appears again, I return it immediately.

# def first_duplicate(numbers):
#     numberslist = []
#     for i in numbers:
#         if i in numberslist:
#             return i
#         else:
#             numberslist.append(i)
#
# print(first_duplicate([1, 2, 3, 2, 4, 5]))


# 8
# Q: How do you implement the Fibonacci sequence?
# A: I used recursion with the base cases for 0 and 1, and recursively added the previous two numbers.

# def fibonacci(n):
#     if n == 0 :
#         return 0
#     elif n == 1 :
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(6))
# print(fibonacci(5))


# 9
# Q: How did you capitalize the first letter of every word?
# A: I split the sentence into words, capitalized each one, and joined them back with spaces.

# def capitalize(sentence):
#     words = sentence.split()
#     capitalized_words = []
#     for word in words:
#         capitalized_words.append(word.capitalize())
#     return " ".join(capitalized_words)
#
# print(capitalize("python is fun"))  # Output: "Python Is Fun"


# 10
# Q: How did you sum the digits of a number?
# A: I turned the number into a string to iterate through each digit and added them as integers.

# def sum_of_digits(numbers):
#     total = 0
#     for i in str(numbers):
#         total += int(i)
#
#     return total
# print(sum_of_digits(123))
