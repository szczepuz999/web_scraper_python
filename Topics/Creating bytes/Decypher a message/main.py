message = input()
key = int(input())

second_number = (key).to_bytes(2, byteorder='little')
# print(second_number)  # b'\x00\x04'
sum = (second_number[0] + second_number[1])

# message_bytes = bytes('HlAdghmcXnt', encoding='utf-8')
# message_bytes = 'HlAdghmcXnt'.decode()
# print(message_bytes)  # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c'

for letter in message:
    letter = ord(letter)
    letter = letter + sum

    print(chr(letter), end="")