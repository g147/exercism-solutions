def value(colors):
    x = ''
    for color in colors[:2]:
        x+=str(color_code(color))
    return int(x)

def color_code(color):
    return colors().index(color)

def colors():
    return ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]