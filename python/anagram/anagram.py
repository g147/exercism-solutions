def find_anagrams(word, candidates):
    anagram = []
    word = word.lower()
    for i in range(len(candidates)):
        anag = candidates[i].lower()
        if word != anag:
            if sorted(word) == sorted(anag):
                anagram.append(candidates[i])
    return anagram