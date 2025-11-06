import json
import bisect
import time

# Check if key2, freq2 is better than key1, freq1
def checkOrdering(key1, freq1, key2, freq2):
    return freq1 < freq2 or (freq1 == freq2 and key1 < key2)


class Deque:

    def __init__(self):
        self.arr = []

    def __getitem__(self, index):
        return self.arr[index]

    def __iter__(self):
        return iter(self.arr)

    def __repr__(self):
        return str(self.arr)

    def __len__(self):
        return len(self.arr)

    def getFreq(self, key):
        for i, (k, v) in enumerate(self.arr):
            if k == key: return i, v
        return -1, 0

    def pop(self, idx):
        return self.arr.pop(idx)

    def add(self, obj):
        item, freq = obj
        for idx, arr_item in enumerate(self.arr):
            insert_idx = idx
            if checkOrdering(arr_item[0], arr_item[1], item, freq):
                break
        else:
            insert_idx = len(self.arr)

        self.arr.insert(insert_idx, [item, freq])

        return insert_idx

    def update(self, item, update_freq):
        idx, old_freq = self.getFreq(item)

        self.arr[idx][1] = update_freq

        if self.arr[idx][1] == 0:
            return self.arr.pop(idx)
        else:
            if old_freq < update_freq:
                i = idx - 1
                while i >= 0:
                    if not checkOrdering(self.arr[i][0], self.arr[i][1], item, update_freq):
                        break
                    i -= 1
                self.arr.insert(i+1, self.arr.pop(idx))
            else:
                i = idx + 1
                while i < len(self.arr):
                    if checkOrdering(self.arr[i][0], self.arr[i][1], item, update_freq):
                        break
                    i += 1
                self.arr.insert(i-1, self.arr.pop(idx))


def remove_operation(remove_item, topx, rest, s, x):
    idx, freq = topx.getFreq(remove_item)

    if idx > -1:
        # If item to remove is in topx
        # If freq == 0, remove it from the top list
        topx.update(remove_item, freq - 1)
        s -= remove_item

        if len(topx) < x and len(rest) > 0:
            # if length is less than x then add the best rest into the topx if available
            topx.add(rest[0])
            best_rest = rest.pop(0)
            s += best_rest[0] * best_rest[1]
        else:
            # check if the frequency in topx is now lower or equal than best in rest
            if len(rest) > 0 and checkOrdering(topx[-1][0], topx[-1][1], rest[0][0], rest[0][1]):
                # Move the removed item from topx to rest and bring the best from rest into topx
                previous_topx_item = topx.pop(-1)
                previous_rest_item = rest.pop(0)

                topx.add(previous_rest_item)
                rest.add(previous_topx_item)

                s += -previous_topx_item[0] * previous_topx_item[1] + previous_rest_item[0] * previous_rest_item[1]

    else:
        # item to remove is in rest
        # S doesn't change, but update the frequency of rest item and the ordering in rest changes
        idx, freq = rest.getFreq(remove_item)
        rest.update(remove_item, freq - 1)

    return s


def add_operation(add_item, topx, rest, s, x):
    idx, freq = topx.getFreq(add_item)

    if idx > -1:
        # If item to add is in topx, no changes to rest positioning, but S and topx change
        topx.update(add_item, freq + 1)
        s += add_item
    elif len(topx) < x:
        # if topx is less than x, place it here.
        topx.add([add_item, 1])
        s += add_item
    else:
        # If item to add is in rest,
        idx, freq = rest.getFreq(add_item)
        if idx > -1:
            # Check if any reordering of rest is needed
            rest.update(add_item, freq + 1)
        else:
            # add to rest and check if we need to push it to topx and update S
            rest.add([add_item, 1])

        # check if need to swap the updated item to topx and update S
        if checkOrdering(topx[-1][0], topx[-1][1], rest[0][0], rest[0][1]):
            swap_topx_item = topx.pop(-1)
            swap_rest_item = rest.pop(0)

            topx.add(swap_rest_item)
            rest.add(swap_topx_item)

            s += -swap_topx_item[0] * swap_topx_item[1] + swap_rest_item[0] * swap_rest_item[1]

    return s


def xsum(k, x, nums, debug=False):

    freqMap = {}
    for item in nums[:k]:
        if item in freqMap:
            freqMap[item] += 1
        else:
            freqMap[item] = 1

    # print(freqMap)

    n = len(nums)
    arr = []

    freqMap = dict(sorted(freqMap.items(), key=lambda item: (item[1], item[0]), reverse=True))

    topx = Deque()
    for item in [[k, v] for k, v in freqMap.items()][:x]:
        topx.add(item)

    rest = Deque()
    for item in [[k, v] for k, v in freqMap.items()][x:]:
        rest.add(item)

    s = 0
    for item, freq in topx:
        s += item * freq
    arr.append(s)
    for i in range(1, n - k + 1):
        if debug: print(f"Current: : {topx} s = {s} {rest}")
        if debug: print(f"Removing {nums[i-1]}")
        s = remove_operation(nums[i - 1], topx, rest, s, x)
        if debug: print(f"Adding {nums[i+k-1]}")
        s = add_operation(nums[i + k - 1], topx, rest, s, x)
        if debug: print(f"Updated: {topx} s = {s} {rest}\n")
        arr.append(s)
    return arr


if __name__ == '__main__':

    with open("../../testcases/xSum.json", "r") as f:
        testcases = json.load(f)


    for testcase in testcases:
        nums = testcase["nums"]
        x = testcase["x"]
        k = testcase["k"]
        expected = testcase["output"]
        start = time.time()
        actual = xsum(k, x, nums)
        duration = (time.time() - start)*1000
        if expected != actual:
            print(f"\n!!! Failed Expected {expected}, got {actual}\n")
        else:
            print(f"\n({duration:.4f}ms) Passed nums={nums}, x={x}, k={k}, output = {expected}\n")