from string import ascii_lowercase
def is_pangram(sentence):
    for i in ascii_lowercase:
        if i not in sentence.lower():
            return False
    return True
