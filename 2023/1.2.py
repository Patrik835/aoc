import re
# from 1_1 import count_result
def file_prep(path):
    file = open(path, "r")
    read = file.read()
    nice = read.split("\n")
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine","1","2", "3","4","5","6","7","8","9"]
    full_list = []
    for i in nice:
        element_list = []
        word = ""
        for j in i:
            word += j
            for number in numbers:
                if number in word:
                    element_list.append(number)
                    word = ""
        full_list.append(element_list)
    return full_list
def decode_list(encoded_list):
    fin_list = []
    numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for i in encoded_list:
        small_list = []
        for j in i:
            if j in numbers.keys():
                small_list.append(numbers[j])
            else:
                small_list.append(j)
        fin_list.append(small_list)
    return fin_list

def count_result(nice_list):
    fin_list = []
    result = 0
    for i in nice_list:
        if len(i) == 1:
            fin_list.append(i[0]+i[0])
        else:
            fin_list.append(i[0]+i[-1])
    print(fin_list)
    for i in fin_list:
        result += int(i)
    return result

prepared_list = file_prep("input/1_input.txt")
decoded_list = decode_list(prepared_list)
print(count_result(decoded_list))
# import re
#
# with open("input/1_input.txt") as f:
#     data = f.read().strip()
#
#
# def calibration(data):
#     ls = data.split("\n")
#     ns = [re.findall("\d", x) for x in ls]
#     return sum(int(n[0] + n[-1]) for n in ns)
#
#
# # Part 1
# print(calibration(data))
#
# # Part 2
# data = (
#     data.replace("one", "one1one")
#     .replace("two", "two2two")
#     .replace("three", "three3three")
#     .replace("four", "four4four")
#     .replace("five", "five5five")
#     .replace("six", "six6six")
#     .replace("seven", "seven7seven")
#     .replace("eight", "eight8eight")
#     .replace("nine", "nine9nine")
# )
# print(calibration(data))