from collections import deque


class MonotonicDeque:
    def __init__(self):
        self.deque = deque()

    def push(self, x):
        while not self.empty() and self.deque[-1] < x:
            self.deque.pop()
        self.deque.append(x)

    def pop(self, x):
        if self.front() == x:
            return self.deque.popleft()

    def front(self):
        if self.deque:
            return self.deque[0]

    def empty(self):
        return len(self.deque) == 0


nums = [10,-5,-2,4,0,3]
k = 2

nums_len = len(nums)

def withDP():
    dp = {}
    dp[0] = nums[0]
    for index in range(1, nums_len):
        cost = -1e9
        for i in range(max(index - k, 0), index):
            cost = max(cost, dp[i])
        dp[index] = cost + nums[index]

    jumpScore = dp[nums_len - 1]
    print(f"Jump Score: {jumpScore}")


def withDSA():
    dp = {}
    dp[0] = nums[0]
    mdq = MonotonicDeque()
    for index in range(1, nums_len):
        mdq.push(dp[index-1])
        if index - k - 1 >= 0: mdq.pop(dp[index - k - 1])
        dp[index] = mdq.front() + nums[index]

    jumpScore = dp[nums_len - 1]
    print(f"Jump Score: {jumpScore}")


withDP()
withDSA()