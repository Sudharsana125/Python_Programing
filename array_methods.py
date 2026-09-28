arr = [12,34,56,78,90]
arr.extend([1,2])
print(arr)
arr.sort()
print(arr)
print(len(arr))

arr.insert(0,14)
print(arr)
print(arr.count(12))
print(arr.index(56))

arr.sort(reverse=True)
print(arr)
print(14 not in arr)

var = arr[:2]
print(var)

list1 = [10, 20, 30]
list2 = [40, 50, 60]
result = list1 + list2
print(result)

students = [
    ["Arun", 85],
    ["Priya", 92],
    ["Rahul", 78]
]
print(students)