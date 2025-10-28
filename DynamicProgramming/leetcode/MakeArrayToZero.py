import time

nums = [35,30,33,32,29,31,33,27,30,38,36,31,29,29,32,35,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,35,43,33,36,32,34,37,31,41,34,30,37,35,43,36]
count = 0
n = len(nums)

def traverse(curr, inc):
   arr = nums[:]
   while 0 <= curr < n:
       if arr[curr] == 0:
           curr += inc
       elif arr[curr] > 0:
           arr[curr] -= 1
           inc *= -1
           curr += inc
   return 1 if all(x == 0 for x in arr) else 0

start = time.time()
for curr in [i for i in range(n) if nums[i] == 0]:
    count += traverse(curr, 1) + traverse(curr, -1)
duration = time.time() - start
print(count, duration)
