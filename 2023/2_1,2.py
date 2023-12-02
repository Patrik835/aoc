def file_prep(path):
    nice = []
    game_id = []
    for i in range(100):
        game_id.append(i+1)
    with open(path,"r") as data:
        count = 0
        for line in data.readlines():
            count += 1
            if count < 100:
                nice.append(line[8:].strip("\n").replace(" ", ""))
            else:
                nice.append(line[9:].strip("\n").replace(" ", ""))
        nice = [i.split(";") for i in nice]
        dictio = zip(game_id, nice)
        dictio = dict(dictio)
    return dictio

def count_result(dictionary):
    part_1 = 0
    part_2 = 0
    c = 0
    for value in dictionary.values():
        c += 1
        result = {"red": 0, "green": 0, "blue": 0}
        for i in value:
            good = i.split(",")
            for e in good:
                if "red" in e:
                    if int(e.replace("red", "")) > result["red"]:
                        result["red"] = int(e.replace("red", ""))
                if "green" in e:
                    if int(e.replace("green", "")) > result["green"]:
                        result["green"] = int(e.replace("green", ""))
                if "blue" in e:
                    if int(e.replace("blue",""))>result["blue"]:
                        result["blue"] =int(e.replace("blue",""))
        if result["red"] <= 12 and result["green"] <= 13 and result["blue"] <= 14:
            part_1 += c
        part_2 += result["red"] * result["green"] * result["blue"]
    return part_1, part_2
dictionary = (file_prep("input/2_input.txt"))
print(count_result(dictionary))
