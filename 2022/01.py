## AOC
################
## Year:    2022
## Day:     01

from tools.filereader import *

elves = generate_array_of_elves()

max_elf_tally = 0

for elf in elves:
    elf_tally = 0
    for item in elf:
        elf_tally += item
    if elf_tally > max_elf_tally:
        max_elf_tally = elf_tally

print(max_elf_tally)
