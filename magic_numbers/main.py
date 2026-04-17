from pathlib import Path





def conver_to_magic_num_if_all_nines(num:str):
    return f"1{(len(num)-1)*'0'}1"

def check_if_magic_num(num:str):
    if num[::-1] == num:
        return True
    else:
        return False

def check_for_power(num: str):
    if num.__contains__("^"):
        a = int(num.split("^")[0])
        b = int(num.split("^")[1])
        return a**b
    else:
        return int(num)

def main():
    print(conver_to_magic_num_if_all_nines("9999"))
    data = Path("input.txt").read_text(encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()
