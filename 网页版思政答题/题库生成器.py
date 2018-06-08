import re
import json
import copy
datapool = []
datadict = [0, [], [], [], []]

idn = 1
with open("./maogai1.txt", encoding='UTF-8') as fp:
    read = fp.read()
    read = re.sub(
        r' {4}', "\n", read)
    read = re.sub(
        r'\n\n', "\n", read)
    read = re.sub(
        r'\n\n', "\n", read)
    read = re.sub(
        r'\n\n', "\n", read)
    read = re.sub(
        r' ', "", read)
    read = re.sub(
        r'\n\n', "\n", read)
    # read.rstrip()
    lines = read.split('\n')
    del lines[-1]
    # print(lines)
    for i in range(len(lines)):

        if lines[i].startswith('1') | lines[i].startswith('2') | lines[i].startswith('3') | lines[i].startswith('4') | lines[i].startswith(
                '5') | lines[i].startswith('6') | lines[i].startswith('7') | lines[i].startswith('8') | lines[i].startswith('9'):
            datadict[2] = re.sub(
                r'[ABCDEFG]+', "", lines[i])
            if re.findall(r'[ABCDEFG]+', lines[i]) != []:
                datadict[4] = re.findall(r'[ABCDEFG]+', lines[i])
            else:
                datadict[4] = re.findall(r'[ABCDEFG]+', lines[i + 1])
            datadict[0] = idn
            idn += 1

        elif (lines[i].startswith('A') | lines[i].startswith('B') | lines[i].startswith('C') | lines[i].startswith('D') |
                lines[i].startswith('E') | lines[i].startswith('F')):
            datadict[3].append(lines[i])
            continue
        else:
            datadict[1].append(lines[i])
        # print(datadict)
        datapool.append(copy.deepcopy(datadict))

        datadict[1] = []
        datadict[2] = []
        datadict[3] = []
        datadict[4] = []
    fp.close()
print(datapool)


with open('data.js','w') as fpn:
    fpn.write("var arr=")
    fpn.write(str(datapool)，encoding= 'utf8')
    fpn.write(";")# str强制转化为文本
    fpn.close()
