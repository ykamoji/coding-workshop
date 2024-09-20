from utils.dputil import getValue, putValue, printDP

N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])

MOD = 1000000007

dag = {i+1:[] for i in range(N)}


for i in range(1, N):
    for j, val in enumerate(input().split()):
        if int(val) == 1:
            dag[i] += [int(j+1)]
print(dag)


def countPaths(vertex, k, paths):

    if k == 0:
        print(paths)
        return 1

    getValue(vertex, k)

    count = 0
    for next in dag[vertex]:
        count = (count + countPaths(next, k-1, paths=paths + [next])) % MOD

    putValue(vertex, k, count)

    return count


total = 0
for start in range(1, N):
    # print(f"Checking with vertex {start}")
    total += countPaths(start, K, [start])

print(f"Total number of paths: {total}")