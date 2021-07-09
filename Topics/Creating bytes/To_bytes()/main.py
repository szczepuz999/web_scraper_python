
inp = (int(input()))
second_number = (inp).to_bytes(2, byteorder='little')
# print(second_number)  # b'\x00\x04'

print(second_number[0] + second_number[1])

