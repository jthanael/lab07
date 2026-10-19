import pytest



message = "Helo world!"
encrypted_message = encrypt(message, 5)

assert decrypt(encrypted_message, 5) == message


from cryptlib import encrypt, decrypt

def test_encrypt():
     assert encrypt("ABC", 3) == "DEF"

def test_decrypt():
     assert decrypt("DEF", 3) == "ABC"

def test_wraparound():
    assert encrypt("XYZ", 3) == "ABC"

def test_lowercase():
    assert encrypt("abc", 2) == "cde"

def test_preserve_spaces_and_numbers():
    assert encrypt("Hello World 123!", 3) == "Khoor Zruog 123!"

def test_decrypt_restores_original():
    assert decrypt(encrypt("Hello World 123!", 3), 3) == "Hello World 123!"
