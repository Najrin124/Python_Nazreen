--#
1. Reverse a String
s = "Python"

reverse = s[::-1]

print(reverse)

Output:
nohtyP

2. Check Palindrome
A palindrome reads the same forward and backward.

s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

Output:
Palindrome


3. Check Prime Number
A prime number has only 2 factors: 1 and itself.
n = 7

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

Output:
Prime

4. Fibonacci Series
a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

Output:
0 1 1 2 3 5 8 13 21 34
🧠 Remember:
a, b = b, a + b


5. Factorial
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)

Output:
120
🧠 Remember: Start fact = 1, then multiply.


6. Armstrong Number

Example: 153

1³ + 5³ + 3³ = 153

n = 153
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")

Output:
Armstrong
🧠 Remember:
% 10 → last digit
// 10 → remove last digit


7. Reverse a Number
n = 12345
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse)

Output:

54321

🧠 Remember: % 10 gets last digit, // 10 removes it.


8. Largest and Second Largest
Largest
numbers = [10, 25, 5, 40, 15]

print(max(numbers))

Output:

40
Second Largest
numbers = [10, 25, 5, 40, 15]

numbers = list(set(numbers))
numbers.sort()

print(numbers[-2])

Output:

25
🧠 Remember: sort() → [-1] largest, [-2] second largest.


9. Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

result = list(set(numbers))

print(result)

Output:

[1, 2, 3, 4, 5]

🧠 Remember: set() automatically removes duplicates.


10. Character Frequency
s = "hello"

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

print(count)

Output:

{'h': 1, 'e': 1, 'l': 2, 'o': 1}

🧠 Remember:

count[ch] = count.get(ch, 0) + 1

means increase count by 1.


11. Find Missing Number

Given:

[1, 2, 3, 5]

Missing number = 4

numbers = [1, 2, 3, 5]

n = 5

total = n * (n + 1) // 2

missing = total - sum(numbers)

print(missing)

Output:

4
🧠 Remember:

Expected total − Actual total = Missing number


12. Two Sum

Find two numbers whose sum equals the target.

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(i, j)

Output:

0 1

Because:
2 + 7 = 9


13. Move Zeros to End

Input:

[0, 1, 0, 3, 12]

Output:

[1, 3, 12, 0, 0]
numbers = [0, 1, 0, 3, 12]

result = []

for n in numbers:
    if n != 0:
        result.append(n)

zeros = len(numbers) - len(result)

result.extend([0] * zeros)

print(result)

🧠 Remember: First collect non-zero → then add zeros.


14. Sort a List
Ascending
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)

Output:

[1, 2, 3, 5, 8]
Descending
numbers.sort(reverse=True)

print(numbers)

Output:
[8, 5, 3, 2, 1]


15. Count Vowels
s = "python programming"

vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print(count)

🧠 Remember: if ch in "aeiou".


16. Check Anagram

Two strings are anagrams if they contain the same characters.

Example:

listen
silent
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

Output:

Anagram

🧠 Remember: sorted(string1) == sorted(string2).


17. Find Duplicate Elements
numbers = [1, 2, 3, 2, 4, 5, 3]

duplicates = []

for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)

print(duplicates)

Output:
[2, 3]

18. Merge Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)
Output:
[1, 2, 3, 4, 5, 6]

Remove duplicates after merging
result = list(set(list1 + list2))

print(result)


19. Linear Search

Linear search checks elements one by one.

numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not Found")

Output:

Found at index 2

🧠 Remember: Linear = one by one.

Time Complexity: O(n)


20. Binary Search

Binary search works on a sorted list.

numbers = [10, 20, 30, 40, 50]
target = 40

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Found at index", mid)
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

Output:

Found at index 3

🧠 Remember:

Sorted → Find Middle → Compare → Left/Right

Time Complexity: O(log n)

🧠 Tata Elxsi Quick Revision
#	Question	Main thing to remember
1	Reverse String	[::-1]
2	Palindrome	Original == Reverse
3	Prime	%
4	Fibonacci	a, b = b, a+b
5	Factorial	Multiplication
6	Armstrong	%10, //10, power
7	Reverse Number	%10, //10
8	Second Largest	sort(), [-2]
9	Remove Duplicate	set()
10	Character Frequency	dict + get()
11	Missing Number	Expected − Actual
12	Two Sum	Pair + target
13	Move Zeros	Non-zero + zeros
14	Sort	sort()
15	Vowels	in "aeiou"
16	Anagram	sorted()
17	Duplicates	count()
18	Merge	+
19	Linear Search	One by one, O(n)
20	Binary Search	Sorted + middle, O(log n)

Most important: Don't just memorize the code. In the interview, be ready to explain what each line does. For Tata Elxsi, I would especially practice Prime, Palindrome, Fibonacci, Armstrong, second-largest, duplicates, Two Sum, and Binary Search until you can write them without looking.
