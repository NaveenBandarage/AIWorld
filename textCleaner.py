file1 = open("executeInput.txt","r")
file2 = open("executeOutput.txt", "w")


for newLine in file1:
    # Remove the new line characters and extra spacing
    newLine = newLine.strip()
    if not newLine.strip(): continue
    if not newLine.startswith("["):
        file2.write(newLine + '\n')

    # For each part in the new line look for grade
    # Move to the next line regardless 
    
newLine = file1.readline()
