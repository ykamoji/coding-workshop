from utils.dputil import getValue, putValue, printDP

seq = [1, 0, 1, 0, 0, 0, 0]
len_seq = len(seq)
seq_to_exclude = [0, 1, 0, 0]
len_seq_ex = len(seq_to_exclude)


def sequence_search(index, target, usedp=False):

    if target == len_seq_ex:
        return 1

    if index == len_seq:
        return 0

    if usedp: getValue(index, target)

    if seq[index] == seq_to_exclude[target]:
        check = sequence_search(index + 1, target + 1, usedp)
    else:
        check = sequence_search(index + 1, target, usedp)

    if usedp: putValue(index, target, check)

    return check


present = sequence_search(0, 0, usedp=True)

# printDP()

print(f"{seq_to_exclude} is {'' if present else 'not '}present in {seq}")