from pathlib import Path



def convert_if_even_length(num:str):
    length = len(num)
    for i in range(int(length/2)):
        chars = list(num)
        if num[i] == num[length-1-i]:
            continue
        elif num[i] > num[length-1-i]:
            chars[length-1-i] = chars[i]
        else: 

            chars[i] = str(int(num[i])+1)
            chars[length-1-i] = chars[i]
    num = ''.join(chars)
    return num



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
    convert_if_even_length("1234")
    data = Path("input.txt").read_text(encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()
