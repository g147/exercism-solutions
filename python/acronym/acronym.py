import re
def abbreviate(words):
    return "".join(re.findall(r"\b[A-Za-z]",re.sub(r"[^a-zA-Z\W]|'",'',words))).upper()
