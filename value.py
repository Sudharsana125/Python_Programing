numb = list(map(int, input("Enter numbers: ").split()))
total = 0
for i in numb:
    if i % 2 == 0:
        total = total+i
print(total)

n = int(input("Enter the num:"))
for i in range(0,21):
    print(n*i)

n = int(input("Enter the ending number: "))

for i in range(1, n + 1, 2):
    print(i)

rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print()


numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter number to search: "))

for number in numbers:
    if number == target:
        print("Number found")
        break
else:
    print("Number not found")

numbers = list(map(int, input("Enter numbers: ").split()))

for number in numbers:
    print(number)
else:
    print("Loop completed")



word = input("Enter a word: ")
target = input("Enter the character to search: ")

count = 0

for char in word:
    if char == target:
        count = count + 1
print(count)


