# def say_hello():
#     return("hello world")
#
# def main():
#     print(say_hello())
#
# if __name__ == '__main__':
#     main()

#Write a function add_numbers(a, b) that returns the sum of two numbers.Your turn!

# def add_numbers(a,b):
#     return a+b
# def main():
#     add_numbers(3,6)
#
# if __name__ == '__main__':
#     main()

#find_max([3, 7, 2, 9, 5]) → 9
# def find_max(numbers):
#     max = numbers[0]
#     for i in numbers:
#         if i > max:
#             max = i
#     return max
# print(find_max([3,7,2,9,5]))

#count_evens([1, 2, 3, 4, 5, 6]) → 3
# def count_evens(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count += 1
#     return count
#
# print(count_evens([1, 2, 3, 4, 5, 6]))

#reverse_list([1, 2, 3, 4]) → [4, 3, 2, 1]
# def reverse_list(numbers):
#     newnumbers = []
#     for i in numbers:
#         newnumbers.insert(0,i)
#     return newnumbers
# print(reverse_list([1, 2, 3, 4]))

#OR

# def reverse_list(numbers):
#     numbers = numbers [::-1]
#     return numbers
# print(reverse_list([1, 2, 3, 4]))

# is_palindrome("racecar") → True
# is_palindrome("hello") → False
#
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

# first_duplicate([1, 2, 3, 2, 4, 5]) → 2
# first_duplicate([1, 2, 3, 4, 5]) → None

# def first_duplicate(numbers):
#     numberslist = []
#     for i in numbers:
#         if i in numberslist:
#             return i
#         else:
#             numberslist.append(i)
#
# print(first_duplicate([1, 2, 3, 2, 4, 5]))

# fibonacci(0) → 0
# fibonacci(1) → 1
# fibonacci(5) → 5
# fibonacci(6) → 8

def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))
print(fibonacci(5))
# fibonacci(5) → 5
# fibonacci(6) → 8













