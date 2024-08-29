arr = [
    [5, 8],
    [2, 4],
    [3, 9]
]

arr_len = len(arr)


def maxCustomers():

    in_res = [times[0] for times in arr]
    in_res.sort()
    out_res = [times[1] for times in arr]
    out_res.sort()

    maxCust, currentCustTrack, incoming, outgoing = 0, 0, 0, 0

    while incoming < arr_len and outgoing < arr_len:

        if in_res[incoming] <= out_res[outgoing]:
            currentCustTrack += 1
            incoming += 1
        else:
            currentCustTrack -= 1
            outgoing += 1

        maxCust = max(maxCust, currentCustTrack)

    return maxCust


print(f"Maximum number of customers = {maxCustomers()}")



