from pathlib import Path

def get_total_in_minute(date_start: str, date_end: str):
    
    total_minutes = 0
    total_minutes += (int(date_start.split(" ")[0].split("-")[0])-int(date_end.split(" ")[0].split("-")[0]))*365*24*60
    total_minutes += (int(date_start.split(" ")[0].split("-")[1])-int(date_end.split(" ")[0].split("-")[1]))*30*24*60
    total_minutes += (int(date_start.split(" ")[0].split("-")[2])-int(date_end.split(" ")[0].split("-")[2]))*24*60
    total_minutes += (int(date_start.split(" ")[1].split(":")[0])-int(date_end.split(" ")[1].split(":")[0]))*60
    total_minutes += (int(date_start.split(" ")[1].split(":")[1])-int(date_end.split(" ")[1].split(":")[1]))
    total_minutes += (int(date_start.split(" ")[1].split(":")[2])-int(date_end.split(" ")[1].split(":")[2]))/60
    return total_minutes

def parse_line(line: str):
    line = line.split("\t")
    return line[0], line[1], line[2]

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    data = data.split("\n")
    data = data[2::]


if __name__ == "__main__":
    main()
