from pathlib import Path

def convert_to_magic_nums(nums:list):
    for i in range(len(nums)):
        allNines = True
        for j in range(len(nums[i])):
            if nums[i][j] != "9":
                allNines = False
        if allNines:
            check_if_magic_num(conver_to_magic_num_if_all_nines(nums[i]))
        elif len(nums[i]) % 2 == 0:
            check_if_magic_num(convert_if_even_length(nums[i]))
        elif len(nums[i]) % 2 == 1:
            check_if_magic_num(convert_if_odd_length(nums[i]))
    
def convert_if_odd_length(num:str):
    length = len(num)
    chars = list(num)
    initial_chars = chars.copy()
    if length == 1 and chars[0] < "9":
        return str(int(num)+1)
    else:
        middle = chars[int(length/2+0.5-1)]
        del chars[int(length/2+0.5-1)]
        length = int(length - 1)
        for i in range(int(length/2)-1,-1,-1):
            if chars[i] == chars[length-1-i]:
                continue
            elif chars[i] > chars[length-1-i]:
                chars[length-1-i] = chars[i]
                if not i == 0:
                    for j in range(length-i,length):
                        chars[j] = "0"
            else: 
                chars[i] = str(int(chars[i])+1)
                chars[length-1-i] = chars[i]
                if not i == 0:
                    for j in range(length-i,length):
                        chars[j] = "0"
            #print(list(map(str,chars)))
        chars.insert(int(length/2), middle)
        if initial_chars == chars:
            chars[int(length/2+0.5)] = str(int(chars[int(length/2+0.5)])+1)
        num = ''.join(chars)
        return num

def brute_force_check(nums:list):
    
    for i in range(len(nums)):
        nums[i] = str(int(nums[i]) + 1)
        while nums[i] != nums[i][::-1]:
            nums[i] = str(int(nums[i]) + 1)
        print(nums[i])

def convert_if_even_length(num:str):
    length = len(num)
    chars = list(num)
    for i in range(int(length/2)-1,-1,-1):
        if chars[i] == chars[length-1-i]:
            continue
        elif chars[i] > chars[length-1-i]:
            chars[length-1-i] = chars[i]
            if not i == 0:
                for j in range(length-i,length):
                    chars[j] = "0"
        else: 
            chars[i] = str(int(chars[i])+1)
            chars[length-1-i] = chars[i]
            if not i == 0:
                for j in range(length-i,length):
                    chars[j] = "0"
        #print(list(map(str,chars)))
    num = ''.join(chars)
    return num

def conver_to_magic_num_if_all_nines(num:str):
    
    return f"1{(len(num)-1)*'0'}1"

def check_if_magic_num(num:str):
    if num[::-1] == num:
        print(num)
    else:
        print("hiba: " + num)

def delete_empty_or_letter_occurrances(nums:list):
    for i in range(len(nums)):
        if not nums[i].isdigit() or nums[i] == "":
            del nums[i]
    return nums

def check_for_power(nums: list):
    for i in range(len(nums)):
        if nums[i].__contains__("^"):
            a = int(nums[i].split("^")[0])
            b = int(nums[i].split("^")[1])
            nums[i] = str(a**b)
    return nums

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    #print(data, end="")
    data = data.split("\n")
    data = check_for_power(data)
    data = delete_empty_or_letter_occurrances(data)
    convert_to_magic_nums(data)
    

if __name__ == "__main__":
    main()
