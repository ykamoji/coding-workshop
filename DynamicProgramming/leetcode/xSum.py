import json
import time
from sortedcontainers import SortedList


# Check if key2, freq2 is better than key1, freq1
def checkOrdering(key1, freq1, key2, freq2):
    return freq1 < freq2 or (freq1 == freq2 and key1 < key2)


class Deque:

    def __init__(self):
        self.arr = SortedList()
        self.freqMap = {}

    def __getitem__(self, index):
        return self.arr[index]

    def __iter__(self):
        return iter(self.arr)

    def __repr__(self):
        return str([item for item in self.arr])

    def __len__(self):
        return len(self.arr)

    def pop(self, idx):
        item = self.arr.pop(idx)
        del self.freqMap[item[1]]
        return item

    def add(self, obj):
        self.freqMap[obj[1]] = obj[0]
        self.arr.add(obj)

    def update(self, item, update_freq):
        self.arr.remove((self.freqMap[item], item))
        if update_freq == 0:
            del self.freqMap[item]
            return
        self.freqMap[item] = update_freq
        self.arr.add((update_freq, item))


def remove_operation(remove_item, topx, rest, s, x):

    if remove_item in topx.freqMap:
        # If item to remove is in topx
        # If freq == 0, remove it from the top list
        topx.update(remove_item, topx.freqMap[remove_item] - 1)
        s -= remove_item

        if len(topx) < x and len(rest) > 0:
            # if length is less than x then add the best rest into the topx if available
            topx.add(rest[-1])
            best_rest = rest.pop(-1)
            s += best_rest[1] * best_rest[0]
        else:
            # check if the frequency in topx is now lower or equal than best in rest
            if len(rest) > 0 and checkOrdering(topx[0][1], topx[0][0], rest[-1][1], rest[-1][0]):
                # Move the removed item from topx to rest and bring the best from rest into topx
                previous_topx_item = topx.pop(0)
                previous_rest_item = rest.pop(-1)

                topx.add(previous_rest_item)
                rest.add(previous_topx_item)

                s += -previous_topx_item[1] * previous_topx_item[0] + previous_rest_item[1] * previous_rest_item[0]

    else:
        # item to remove is in rest
        # S doesn't change, but update the frequency of rest item and the ordering in rest changes
        rest.update(remove_item, rest.freqMap[remove_item] - 1)

    return s


def add_operation(add_item, topx, rest, s, x):

    if add_item in topx.freqMap:
        # If item to add is in topx, no changes to rest positioning, but S and topx change
        topx.update(add_item, topx.freqMap[add_item] + 1)
        s += add_item
    elif len(topx) < x:
        # if topx is less than x, place it here.
        topx.add((1, add_item))
        s += add_item
    else:
        # If item to add is in rest,
        if add_item in rest.freqMap:
            # Check if any reordering of rest is needed
            rest.update(add_item, rest.freqMap[add_item] + 1)
        else:
            # add to rest and check if we need to push it to topx and update S
            rest.add((1, add_item))

        # check if need to swap the updated item to topx and update S
        if checkOrdering(topx[0][1], topx[0][0], rest[-1][1], rest[-1][0]):
            swap_topx_item = topx.pop(0)
            swap_rest_item = rest.pop(-1)

            topx.add(swap_rest_item)
            rest.add(swap_topx_item)

            s += -swap_topx_item[1] * swap_topx_item[0] + swap_rest_item[1] * swap_rest_item[0]

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
        topx.add((item[1], item[0]))

    rest = Deque()
    for item in [[k, v] for k, v in freqMap.items()][x:]:
        rest.add((item[1], item[0]))

    s = 0
    for freq, item in topx:
        s += item * freq
    arr.append(s)
    for i in range(1, n - k + 1):
        if debug: print(f"Current: s = {s} {rest}\t\t{topx}")
        if debug: print(f"Removing {nums[i-1]}")
        s = remove_operation(nums[i - 1], topx, rest, s, x)
        if debug: print(f"Adding {nums[i+k-1]}")
        s = add_operation(nums[i + k - 1], topx, rest, s, x)
        if debug: print(f"Updated: s = {s} {rest}\t\t{topx} \n")
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