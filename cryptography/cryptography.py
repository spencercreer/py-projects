import time

def shiftChar(char, shift):
    ascii = ord(char) + shift
    if (ascii > 122):
        newChar = chr(ascii - 26)
    elif (ascii < 97):
        newChar = chr(ascii + 26)
    else:
        newChar = chr(ascii)

    return newChar

def encodeCaesarCipher(text, shift):
    text = text.replace(" ", "").lower()
    message = ""

    for char in text:
       message += shiftChar(char, shift)

    return message

def decodeCaesarCipher(text, shift):
    text = text.replace(" ", "").lower()
    message = ""

    for char in text:
        message += shiftChar(char, shift)

    return message


def encodeVigenereCipher(text, key):
    text = text.replace(" ", "").lower()
    key = key.lower()
    message = ""

    for index, char in enumerate(text):
        shift = ord(key[index % len(key)]) - 97
        message += shiftChar(char, shift)

    return message

def decodeVigenereCipher(text, key):
    text = text.replace(" ", "").lower()
    key = key.replace(" ", "").lower()
    message = ""

    for index, char in enumerate(text):
        shift = ord(key[index % len(key)]) - 97
        message += shiftChar(char, -shift)

    return message

def encodeAffineCipher(text, a, b):
    text = text.replace(" ", "").lower()
    message = ""

    for char in text:
        message += chr(((a * (ord(char) - 97) + b) % 26) + 97)

    return message

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % m

def decodeAffineCipher(text, a, b):
    text = text.replace(" ", "").lower()
    message = ""
    a_inv = mod_inverse(a, 26)

    for char in text:
        message += chr(((a_inv * (ord(char) - 97 - b)) % 26) + 97)

    return message

print(decodeVigenereCipher("eprfylscdxyjv", "sparky"))
print(decodeAffineCipher("Uqp Lds Gpmza xbabcl By jfcbbs fsg hbag abbr hcpfu", 9, 5))
print(decodeCaesarCipher("Jxu auo veh rhuqaydw oekh dunj syfxuh yi hywxj kdtuh oekh deiu", 10))
