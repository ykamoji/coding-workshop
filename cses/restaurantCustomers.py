def maxCustomers():

    arr_len = int(input())
    arr = []
    i = 0
    in_res = []
    out_res = []
    while i < arr_len:
        arrival, outgoing = input().split()
        in_res.append(int(arrival))
        out_res.append(int(outgoing))
        arr.append([int(arrival), int(outgoing)])
        i += 1

    in_res.sort()
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

print(maxCustomers())



