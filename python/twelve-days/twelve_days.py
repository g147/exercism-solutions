gifts = [
    'and a Partridge in a Pear Tree.',
    'two Turtle Doves',
    'three French Hens',
    'four Calling Birds',
    'five Gold Rings',
    'six Geese-a-Laying',
    'seven Swans-a-Swimming',
    'eight Maids-a-Milking',
    'nine Ladies Dancing',
    'ten Lords-a-Leaping',
    'eleven Pipers Piping',
    'twelve Drummers Drumming'
]
days = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]
line = 'On the {days} day of Christmas my true love gave to me: {gifts}'

def recite(start_verse, end_verse):
    return [joiner(index) for index in range(start_verse - 1, end_verse)]

def joiner(index):
    list = ', '.join(reversed(gifts[:index+1]))
    if list.startswith('and '):
        list=list[len('and '):]
    return line.format(days=days[index], gifts=list)