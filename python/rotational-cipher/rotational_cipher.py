import string
lower=string.ascii_lowercase
upper=string.ascii_uppercase
def rotate(text, key):
    return "".join([lower[(lower.find(c)+key)%26] if c in lower else upper[(upper.find(c)+key)%26] if c in upper else c for c in text])