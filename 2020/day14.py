with open("2020\day14.txt", "r") as f:
    program = [line.strip() for line in f]

# print(program)

#################### Part One ####################
entries = dict()
decimals = dict()
results = dict()
mask = ""
total = 0


for entry in program:
    # Get the mask for each group of memory entries
    if entry.startswith("mask"):
        mask = entry.lstrip("mask = ")
        # print(mask)
        continue

    # Get the memory address and the input value
    pos = entry.split("=")[0].lstrip("mem[").rstrip("] ")
    val = entry.split("=")[1].strip()
    entries.update({pos: val})

    # Convert the input value to binary
    binary = bin(int(val))[2:].zfill(36)
    decimals.update({pos: binary})

    # Apply the mask to the binary input value
    result = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            result += binary[i]
        else:
            result += mask[i]
    results.update({pos: result})

# Sum all our input values after converting them to decimals
for pos in results:
    total += int(results[pos], 2)
print(total)
#################### Part One ####################


#################### Part TWo ####################
import itertools

countX = 0
memory = dict()


for entry in program:
    # Get the mask for each group of memory entries, like in part one
    if entry.startswith("mask"):
        mask = entry.lstrip("mask = ")
        continue

    # Get the memory address integer and convert it to 36-bit binary
    pos = entry.split("=")[0].lstrip("mem[").rstrip("] ")
    pos_bin = bin(int(pos))[2:].zfill(36)
    # print(pos_bin)

    # Apply the bitmask to the binary address
    address = ""
    for i in range(len(mask)):
        if mask[i] == "0":
            address += pos_bin[i]
        elif mask[i] == "1":
            address += mask[i]
        else:
            address += "X"
            countX += 1
    # print(address)

    # Generate all the permutations of "1" and "0" for the number of "X" our address contains
    floatings = ["".join(seq) for seq in itertools.product("01", repeat=countX)]
    countX = 0
    # print(floatings)

    # Generate all the possible address permutations for each "0" and "1" permutation we calculated above
    result = address
    # print(result)
    results = []
    for floating in floatings:
        for char in floating:
            result = result.replace("X", char, 1)
            # print(result)
        results.append(result)
        result = address
    # print(results)

    # Get the value to be written and convert it to decimal
    val = int(entry.split("=")[1].strip())

    for result in results:
        memory.update({result: val})

# print(memory)
total = 0
for entry in memory:
    total += memory[entry]
print(total)
#################### Part TWo ####################