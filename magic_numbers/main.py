from pathlib import Path

def convert_to_magic_nums(nums:list):
    for i in range(len(nums)):
        allNines = True
        for j in range(len(nums[i])):
            if nums[i][j] != "9":
                allNines = False
        if allNines:
            print(conver_to_magic_num_if_all_nines(nums[i]))
        elif len(nums[i]) % 2 == 0:
            print(convert_if_even_length(nums[i]))
        elif len(nums[i]) % 2 == 1:
            print("odd")
    
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
        if num[i] == num[length-1-i]:
            continue
        elif num[i] > num[length-1-i]:
            chars[length-1-i] = chars[i]
            if not i == 0:
                for j in range(length-i,length):
                    chars[j] = "0"
        else: 
            chars[i] = str(int(num[i])+1)
            chars[length-1-i] = chars[i]
            if not i == 0:
                for j in range(length-i,length):
                    chars[j] = "0"
    num = ''.join(chars)
    return num

def conver_to_magic_num_if_all_nines(num:str):
    
    return f"1{(len(num)-1)*'0'}1"

def check_if_magic_num(num:str):
    if num[::-1] == num:
        return True
    else:
        return False

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
