from pathlib import Path

def file_fee(data:list):
    print("RENSZAM\tDIJ")
    for line in data:
        print(f"{parse_line(line)[0]}\t{int(get_fee(get_total_in_minute(parse_line(line)[1], parse_line(line)[2])))}")
        with open("fees.txt", "a", encoding="utf-8") as f:
            f.write("RENSZAM\tDIJ\n")
            f.write(f"{parse_line(line)[0]}\t{int(get_fee(get_total_in_minute(parse_line(line)[1], parse_line(line)[2])))}\n")

def get_fee(total_minutes: int):
    fee = 0
    if total_minutes <= 30:
        return fee
    if total_minutes/60/24 >= 1:
        fee += ((total_minutes/60)//24)*10000
        total_minutes -= ((total_minutes/60)//24)*24*60
    total_minutes -= 30
    if total_minutes <= 30:
        total_minutes -= 30
    if total_minutes//60 >= 1:
        if total_minutes//60 <= 3:
            fee += (total_minutes//60)*300
            if total_minutes//60 < 3 and total_minutes - (total_minutes//60)*60 > 0 :
                fee += 300
                total_minutes = 0
            elif total_minutes//60 == 3 and total_minutes - (total_minutes//60)*60 > 0:
                fee += 500
            total_minutes = 0
        else:
            fee += 3*300
            total_minutes -= 3*60
            fee += (total_minutes//60)*500
            total_minutes -= (total_minutes//60)*60
            if total_minutes > 0:
                fee += 500
                total_minutes = 0
    if total_minutes > 0:
        fee += 300
        total_minutes = 0
    return fee

def get_total_in_minute(date_start: str, date_end: str):
    total_minutes = 0
    total_minutes += (int(date_end.split(" ")[0].split("-")[0]) - int(date_start.split(" ")[0].split("-")[0])) * 365 * 24 * 60
    total_minutes += (int(date_end.split(" ")[0].split("-")[1]) - int(date_start.split(" ")[0].split("-")[1])) * 30 * 24 * 60
    total_minutes += (int(date_end.split(" ")[0].split("-")[2]) - int(date_start.split(" ")[0].split("-")[2])) * 24 * 60
    total_minutes += (int(date_end.split(" ")[1].split(":")[0]) - int(date_start.split(" ")[1].split(":")[0])) * 60
    total_minutes += (int(date_end.split(" ")[1].split(":")[1]) - int(date_start.split(" ")[1].split(":")[1]))
    total_minutes += (int(date_end.split(" ")[1].split(":")[2]) - int(date_start.split(" ")[1].split(":")[2])) / 60
    return total_minutes

def parse_line(line: str):
    line = line.split("\t\t")
    return line[0].strip(), line[1].strip(), line[2].strip()

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    data = data.split("\n")
    data = data[2::]
    file_fee(data)


if __name__ == "__main__":
    main()
