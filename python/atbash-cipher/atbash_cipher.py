import string

lower=string.ascii_lowercase

def encode(plain_text):
    text = plain_text.lower()
    cipher = "".join([lower[-(lower.find(c)+1)] if c in lower else c if c.isnumeric() else "" for c in text])
    cipher = " ".join([(cipher[i:i+5]) for i in range(0, len(cipher), 5)])
    return cipher

def decode(ciphered_text):
    text = ciphered_text.lower()
    plain = "".join([lower[-(lower.find(c)+1)] if c in lower else c if c.isnumeric() else "" for c in text])
    return plain
