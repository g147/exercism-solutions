import re
def is_isogram(string):
    string = re.sub("[^A-Za-z]", "", string).lower()
    return len(string)==len(set(string))
