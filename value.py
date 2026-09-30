
word = input("Enter a word: ")
target = input("Enter the character to search: ")

count = 0

for char in word:
    if char == target:
        count = count + 1
print(count)

word = input("Enter a word: ")

count = 0

for char in word:
    if char.isupper():
        count = count + 1

print("Uppercase letters:", count)
