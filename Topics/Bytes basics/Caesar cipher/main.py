input = input()
new_string = ""
for letter in input:
    current_code_point = ord(letter)
    new_code_point = current_code_point + 1
    new_string = new_string + chr(new_code_point)
    # print(chr(new_code_point))

print(new_string)
