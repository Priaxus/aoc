## AOC
################
## Year:    2022
## Day:     02


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

elf_tallies = []

for elf in elves:
    elf_tally = 0
    for item in elf:
        elf_tally += item

    elf_tallies.append(elf_tally)

elf_tallies.sort()
elf_tallies.reverse()

total = 0
for x in elf_tallies[:3]:
    total += x
print(total)
