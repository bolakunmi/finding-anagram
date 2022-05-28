# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()
    splited_word = [letter for letter in word]
    splited_anagram = [letter for letter in anagram] 

    splited_word_items={}
    for item in set(splited_word):
        splited_word_items[item] = splited_word.count(item)

    splited_anagram_items={}
    for item in set(splited_anagram):
        splited_anagram_items[item] = splited_anagram.count(item)
    

    print((splited_word_items) == (splited_anagram_items))
    return 

find_anagram('DEBIT CARD','bad credit')