def response(hey):
    if hey.isupper():
        if hey.strip().endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    elif hey.strip().endswith("?"):
        return "Sure."
    elif any(map(str.isalnum, hey)):
        return "Whatever."
    return "Fine. Be that way!"