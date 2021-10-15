"""
--- Day 4: The Ideal Stocking Stuffer ---
"""

# ------ Part One ------ #

# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)
import hashlib

# Initialize string
with open("2015/day04.txt", "r", encoding="utf-8") as f:
    secret_key = f.read()
decimal_number = 0
print(secret_key)

# encoding  using encode()
# then sending to md5()
result = hashlib.md5(secret_key.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())

while True:
    decimal_number += 1
    # create hash with key-number concat
    hash_str = secret_key + str(decimal_number)
    # encode and then send to md5
    md5_str = hashlib.md5(hash_str.encode())
    # convert MD5 hash to hexadecimal
    hex_str = md5_str.hexdigest()
    if (hex_str[0:5]) == "00000":
        print(decimal_number)
        break

# ------ End of Part One ------ #


# ------ Part Two ------ #

while True:
    decimal_number += 1
    # create hash with key-number concat
    hash_str = secret_key + str(decimal_number)
    # encode and then send to md5
    md5_str = hashlib.md5(hash_str.encode())
    # convert MD5 hash to hexadecimal
    hex_str = md5_str.hexdigest()
    if (hex_str[0:6]) == "000000":
        print(decimal_number)
        break

# ------ End of Part Two ------ #
