encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

decrypted_message = encrypted_message + ""

start = 0
end = len(encrypted_message) - 1

while start < end:
    # swap the characters at the start and end indices
    decrypted_message = (
        decrypted_message[:start]
        + encrypted_message[end]
        + decrypted_message[start + 1 : end]
        + encrypted_message[start]
        + decrypted_message[end + 1 :]
    )
    start += 2
    end -= 2

decrypted_message = decrypted_message[::-1]
print(decrypted_message)
