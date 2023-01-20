import os
import codecs
import pandas as pd

def containsDigitAndLetters(st):
    digit = False
    letter = False
    for elem in st:
        if (elem.isdigit()):
            digit = True
        if (elem.isalpha()):
            letter = True
    return digit and letter

fileNames = os.listdir("Data/")
for elem in fileNames:
    if (not os.path.isfile("Data/" + elem)):
        fileNames.remove(elem)

lines = []
for fileName in fileNames:
    file = codecs.open('Data/' + fileName, "r", "utf_8_sig")
    for line in file:
        if (line.find("main")):
            line = line[0:line.find("main")];
        if (containsDigitAndLetters(line) and line.find("Консоль") and line not in lines):
            lines.append(line)
    file.close()

fileNames = os.listdir("Data/МТЦ/")
for fileName in fileNames:
    file = codecs.open('Data/МТЦ/' + fileName, "r", "utf_8_sig")
    for line in file:
        if (line.find("main")):
            line = line[0:line.find("main")];
        if (containsDigitAndLetters(line) and line.find("Консоль") and line not in lines):
            lines.append(line)
    file.close()

#print(lines)

df = pd.DataFrame(lines)
df.to_excel("data.xlsx")
#for line in lines:
