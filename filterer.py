
try:
    words_list = []
    with open('unfilteredwords.txt', 'r') as file:
        for line in file:
            line.strip()
            if len(line) == 6:
                words_list.append(line.upper())
except:
    print("An unexpected error occurred while handling unfilteredwords.txt")

try:
    with open('filteredwords.txt', 'x') as file:
        for word in words_list:
            file.write(word)
except FileExistsError:
    print("ERROR: filteredwords.txt already exists.")

except:
    print("An unexpected error occurred while handling filteredwords.txt")