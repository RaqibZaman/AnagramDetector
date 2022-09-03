"""
Anagram detector
Given a list of terms as input, group anagrams together and output a list of lists
list of lists - sub lists group the anagrams that use the same letters.
Anagrams basically mean different words that use the same letters. So you could organize all letters in a word
in alphabetic order before conducting a search in the dictionary to check if there is an anagram

I could have this alphabetic order as the key, and the value can be a list. Store the words that match in the dictionary
in the list, and let's ignore duplicates      

I: ["cat", "bag", "act", "tac", "top", "pot"]
O: [["cat", "act", "tac"], ["bag"], ["top", "pot"]]

I: ["cat", "act"]
O: [["cat", "act"]]

I: ["cat", "pot", "bag"]
O: [["cat"], ["pot"], ["bag"]]
"""



# 1. First organize a word input into alphabetical order <= search this in the dictionary
# 2. Search with the 1st character???
# dictionary
# 1. I can have alphabetically ordered keys for letter 
# I would have keys of letters, and values would be 

# input lists & setup
inputList1 = ["cat", "bag", "act", "tac", "top", "pot"]
inputList2 = ["cat", "pot", "bag"]
outputList1 = []
outputList2 = []
myDict = {}

# 1. iterate through list entries
# 2. sort letters in entry into alphabetic order
# 3. check if sorted entry is in dict
# 4. If not in dict, add to dict with sorted entry as key, and unsorted appended to value list
# 5. Check if value list already has the original word 1st. If it does, don't add. Else, add the word

def anagramDetector(inputList):
    for x in inputList:
        