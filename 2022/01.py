## AOC
################
## Year:    2022
## Day:     01

data_file = open("01.data",'r')

elves = []
temp = []

for line in data_file:
    line = line.strip()

    if line != "":
        temp.append(int(line))
    else:
        elves.append(temp)
        temp = []

max_elf_tally = 0

for elf in elves:
    elf_tally = 0
    for item in elf:
        elf_tally += item
    if elf_tally > max_elf_tally:
        max_elf_tally = elf_tally

print(max_elf_tally)
