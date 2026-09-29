nums1 = list(map(int,input("Enetr the nums: ").split()))
nums2 = list(map(int,input("Enetr the nums: ").split()))

nums= nums1+nums2
nums.sort()

n = len(nums)
if n%2==1:
    print(nums[n//2])
else:
    middle1 = nums[n//2-1]
    middle2 = nums[n//2]
    print((middle1 + middle2)//2)