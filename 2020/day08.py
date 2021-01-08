with open('2020\day8.txt', 'r') as f:
    instructions = [line.strip() for line in f]

# print(instructions)

#################### Part One ####################
# index = 0
# accumulator = 0

# while(True):
#     print(instructions[index])
#     if instructions[index] == "VISITED":
#         print(accumulator)
#         break

#     operation = instructions[index].split(" ")[0]
#     argument = int(instructions[index].split(" ")[1])
#     instructions[index] = "VISITED"

#     if operation == "acc":
#         accumulator += argument
#         index += 1
#         continue
#     elif operation == "jmp":
#         index += argument
#         continue
#     else:
#         index += 1
#         continue
#################### Part One ####################


#################### Part Two ####################
def find_instruction_index():
    global instructions
    index = 0
    changed_idx = 0
    instructions_fresh = instructions.copy()

    while(True):
        if index > len(instructions) - 1:
            instructions = instructions_fresh.copy()
            return changed_idx

        # print(instructions[index])

        operation = instructions[index].split(" ")[0]
        argument = int(instructions[index].split(" ")[1])

        if changed_idx == 0 and (operation == "jmp" or operation == "nop"):
            changed_idx = index
            if operation == "jmp":
                index += 1
                continue
            else:
                index += argument
                continue

        if instructions[index].endswith(" VISITED"):
            instructions = instructions_fresh.copy()
            index = changed_idx
            changed_idx = 0
            operation = instructions[index].split(" ")[0]
            argument = int(instructions[index].split(" ")[1])

        instructions[index] += " VISITED"
        if operation == "acc":
            index += 1
            continue
        elif operation == "jmp":
            index += argument
            continue
        else:
            index += 1
            continue


print(find_instruction_index())


def count_accumulator(instruction_index):
    global instructions
    index = 0
    accumulator = 0

    while(True):
        if index > len(instructions) - 1:
            return accumulator

        # print(instructions[index])

        operation = instructions[index].split(" ")[0]
        argument = int(instructions[index].split(" ")[1])
        if index == instruction_index:
            operation = "nop"

        if operation == "acc":
            accumulator += argument
            index += 1
            continue
        elif operation == "jmp":
            index += argument
            continue
        else:
            index += 1
            continue

    return accumulator


print(count_accumulator(find_instruction_index()))
#################### Part Two ####################
