from pathlib import Path

def do_the_drops(data:list):
    for line in data:
        N = int(line[0])
        H = int(line[1])
        print(min_drops(N, H))

def min_drops(N:int, H:int):
    if H <= 1: return H
    if N == 1: return H
    
    if N == 2:
        drops = 0
        floor = 0
        while H > drops:
            floor += 1
            drops += floor
        return floor


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
