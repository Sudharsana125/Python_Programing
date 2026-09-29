num = map(int,input("Enetr the number: ").split())
for i in num :
    if i % 2==0:
        continue
    print(i)

num = list(map(int,input("Enetr the number: ").split()))
for i in num :
    if i <0:
        continue
    print(i)

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print()

rows = int(input("Enter number of rows: "))

matrix = []

for i in range(rows):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

print("Matrix:")

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

