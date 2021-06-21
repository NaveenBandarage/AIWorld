file1 = open("newfile.txt", "r")
file2 = open("cleanfile.txt", "w")


# for newLine in file1:
#     # Remove the new line characters and extra spacing
#     newLine = newLine.strip()
#     if not newLine.strip(): continue
#     if not newLine.startswith("["):
#         continue
#     newLine.replace("fuck", "")
#     newLine.replace("bitch", "")
#     newLine.replace("nigga", "")
#     newLine.replace("Yeah Yeah Yeah", "")
#     newLine.replace("shit", "")
#     newLine.replace("retarded", "")
#     newLine.replace("pussy", "")
#     newLine.replace("niggas", "")

# f1 = open('newfile.txt', 'r')
# f2 = open('cleanfile.txt', 'w')
# for newLine in file1:
#     newLine.replace("fuck", "")
#     newLine.replace("bitch", "")
#     newLine.replace("nigga", "")
#     newLine.replace("Yeah Yeah Yeah", "")
#     newLine.replace("shit", "")
#     newLine.replace("retarded", "")
#     newLine.replace("pussy", "")
#     newLine.replace("niggas", "")
#     file2.write(newLine)

checkWords = ("fuck", "Fuck", "bitch", "Bitch", "Nigga", "nigga",
              "shit", "retarded", "pussy", "Pussy", "niggas", "Niggas", "   ", "sex", "dick" , "Dick")
repWords = " "

for line in file1:
    for check in checkWords:
        line = line.replace(check, repWords)
    file2.write(line)

file1.close()
file2.close()

# For each part in the new line look for grade
# Move to the next line regardless

# newLine = file1.readline()
