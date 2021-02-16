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