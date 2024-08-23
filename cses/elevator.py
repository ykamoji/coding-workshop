weights = [4, 8, 6, 1]
weights_len = len(weights)
M = 10


def bruteForce():
    visited = [0] * weights_len

    def minimumRides(limit):
        count = 0
        while 0 in visited:
            for i in range(weights_len):
                if weights[i] <= limit and visited[i] == 0:
                    visited[i] = 1
                    limit -= weights[i]
            count += 1
            limit = M

        return count

    count = minimumRides(M)
    print(f"Minimum number of rides needed = {count}")


bruteForce()