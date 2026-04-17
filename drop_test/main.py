from pathlib import Path

def do_the_drops(data:list):
    for line in data:
        N = int(line[0])
        H = int(line[1])
        print(bike_drop(N, H))

def min_drops(N:int, H:int, memo:list):
    if memo[N][H] != -1:
        return memo[N][H]
    if H == 1 or H == 0:
        return H
    if N == 1:
        return H
    res = H
    for i in range(1, H + 1):
        cur = max(min_drops(N - 1, i - 1, memo), \
                    min_drops(N, H - i, memo))
        if cur < res:
            res = cur
    memo[N][H] = res + 1
    return memo[N][H]

def bike_drop(N, H):
    memo = [[-1 for _ in range(H + 1)] for _ in range(N + 1)]
    return min_drops(N, H, memo)

def line_parse(line:list):
    for i in range(len(line)):
        line[i] = line[i].split(", ")
    return line

def main():
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    data = line_parse(data)
    #print(data, end="")
    do_the_drops(data)


if __name__ == "__main__":
    main()
