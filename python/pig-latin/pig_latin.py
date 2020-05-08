import re
def translate(texts):
    result=""
    for text in texts.split(" "):
        if(re.match('^(xr|yt)', text)):
            result += " "+text+'ay'
            continue
        if(re.match('^([^aeiou]*(qu))', text)):
            matches=re.findall('^([^aeiou]*(qu))', text)[0][0]
            text = re.sub('^([^aeiou]*(qu))',"", text)
            result += " "+ str(text)+str(matches)+'ay'
            continue
        if(re.match('^([^aeiouy]+)', text)):
            matches=re.findall('^([^aeiouy]+)', text)[0]
            text = re.sub('^([^aeiouy]+)',"", text)
            result += " "+ str(text)+str(matches)+'ay'
            continue
        if(re.match('^y', text)):
            matches=re.findall('^y', text)[0]
            text = re.sub('^y',"", text)
            result += " "+ str(text)+str(matches)+'ay'
            continue
        else:
            result += " "+ text+'ay'
            continue
    return result.strip()