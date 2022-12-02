def generate_array_of_elves():
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

    return elves