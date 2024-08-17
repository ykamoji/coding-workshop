# seq = [1, 5, 7, 10, 9, 6, 7, 9, 2, 3]
seq = [3, 2, 5, 4, 5, 7, 8, 1, 11, 9]
seq_len = len(seq)
dp = {}
lis = []
inserted = {}


def sequence():

    for i in range(seq_len):
        if len(lis) == 0 or lis[-1] < seq[i]:
            lis.append(seq[i])
            inserted[i] = len(lis) - 1

        else:
            for j in range(len(lis)):
                if lis[j] > seq[i]:
                    lis[j] = seq[i]
                    inserted[i] = j
                    break

        # print(f"{i} : {lis}")

    # print(f"{list(inserted.values())}")

    final_lis = []
    lis_len = len(lis) - 1
    for i in range(len(seq)-1, -1, -1):
        if inserted[i] == lis_len:
            final_lis.append(seq[i])
            lis_len -= 1

    final_lis = final_lis[::-1]

    print(f"Best increasing array = {final_lis}")

sequence()