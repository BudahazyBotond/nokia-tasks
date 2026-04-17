from pathlib import Path

def do_the_drops(data:list):
    for line in data:
        N = int(line[0])
        H = int(line[1])
        print(min_drops(N, H))

def min_drops(N:int, H:int):
    if H <= 1: return H
    if N == 1: return H
    
    min = H
    for i in range(1, H+1):
        drops = int(max(min_drops(N-1, i-1), min_drops(N, H-i)))
        if drops < min:
            min = drops
    return min + 1


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
