import re

def file_prep(path):
    file = open(path, "r")
    read = file.read()
    nice = read.split("\n")
    print(nice)
    num_list = []
    for i in nice:
        string = ""
        for j in i:
            if re.search("[1-9]", j):
                string += j
        num_list.append(string)
    return num_list
def count_result(nice_list):
    fin_list = []
    result = 0
    for i in nice_list:
        if len(i) == 1:
            fin_list.append(i+i)
        else:
            fin_list.append(i[0]+i[-1])
    for i in fin_list:
        result += int(i)
    return result

print(count_result(file_prep("input/1_input.txt")))