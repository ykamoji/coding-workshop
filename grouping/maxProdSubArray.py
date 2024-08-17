arr = [2, 3, -2, 4]
# arr = [-2, 0, -1]
# arr = [-10]


def arr_product(sub_arr):

    if len(sub_arr) == 0:
        return -1e10

    sum = 1
    for item in sub_arr:
        sum *= item
    return sum


def maxProduct():
    val = -1e10
    for i in range(len(arr)):
        temp_val = max(arr_product(arr[:i + 1]), arr_product(arr[i + 1:]))
        # print(arr[l:i + 1], arr[i + 1:r + 1], temp_val)
        if temp_val > val:
            val = temp_val

    return val


val = maxProduct()
print(f"Maximum product = {val}")


def maxProduct_optim():
    val = -1e10
    mx, mn = 1, 1
    for i in range(len(arr)):
        t = mn
        mn = min(min(arr[i], mn * arr[i]), mx * arr[i])
        mx = max(max(arr[i], mx * arr[i]), t * arr[i])
        val = max(val, mx)

    return val


val = maxProduct_optim()

print(f"Maximum product (optimized) = {val}")
