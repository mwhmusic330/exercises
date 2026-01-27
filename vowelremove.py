



def findvowel(charact):
    vowels = 'aieouAEIOU'
    return charact in vowels
def lastvowelindex(word):
    for i in range(len(word) - 1, -1, -1):
        if findvowel(word[i]):
            return i
    return -1
def pull_lastvowel(word):
    last_vowel = lastvowelindex(word)
    if last_vowel == -1:
        return word
    else:
        return word[:last_vowel] + word[last_vowel+1:]
def removeLastVowel(sentence):
    wrdlst = sentence.split()
    print([pull_lastvowel(word) for word in wrdlst])




removeLastVowel("Those who dare to fail miserably can achieve greatly.")

removeLastVowel("Love is a serious mental disease.")

removeLastVowel("Get busy living or get busy dying.")

removeLastVowel("If you want to live a happy life, tie it to a goal, not to people.")
