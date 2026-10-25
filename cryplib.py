def encrypt(message, shift):
    result = ""

    for character in message:
        if character.isupper():
            position = ord(character) - ord("A")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("A"))

        elif character.islower():
            position = ord(character) - ord("a")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("a"))

        else:
            result += character

    return result


def decrypt(message, shift):
    return encrypt(message, -shift)