
# A class Anagram should take a "word" and create an instance
# There should be a method that takes in a list of words and checks for a match with the "word"

# Match Method: 
# List interpretation: sorted(letter for letter in "word") == sorted(letter for letter in "words-list")
# return matched word

class Anagram:

    def __init__ (self, word):
        self.word = word

    def match(self, array):
        result = []
        for item in array:
            if sorted(item) == sorted(self.word):
                result.append(item)
        
        return result


word1 = Anagram("hello")

if __name__ == "__main__":

    print(word1.match(["loleh", "colombus", "serera"]))











