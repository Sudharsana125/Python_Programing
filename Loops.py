numbers = [1, 2, 3, 4, 5]
s=[]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        s.append(numbers[i])
        print(s)

for i in range(2, 7):
    print(i)

s = []
for i in range(0, 10, 2):
    s.append(i)
print(s)


a = list(map(int, input("Enter the numb: ").split()))
num = []
for i in a:
    if i % 2 == 0:
        num.append(i)
print(num)

a = list(map(int, input("Enter numbers: ").split()))

for i in range(len(a)):
    print("Index:", i, "Value:", a[i])

a = list(map(int,input("Enetr the nums: ").split()))
for i in a :
    if i < 5:
        break
    print(i)
