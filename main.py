import string

def main():
    book_contents = readbook("books/frankenstein.txt")
    letter_dict = letterFrequency(book_contents)
    numOfWords = wordCount(book_contents)


    print("______---|| Book Report of Frankenstein ||---_______\n")
    print(f"There are {numOfWords} words in the book.\n")

    for val in letter_dict:
        print(f"The '{val}' character was found {letter_dict[val]} times.")

    print("-------------- END OF REPORT --------------")
   


def readbook(path_to_book): # returns text file as string
    with open(path_to_book) as f:
        return f.read()

def wordCount(book): # returns number of words in string
    return len(book.split())

def letterFrequency(book): #returns a dictionary of lowercase letters as keys and fequency in book as values
    lowercaseBookNoSpaces = "".join(book.lower().split())
    miscCharRemoved = ''.join([char for char in lowercaseBookNoSpaces if char.isalpha()])

    letter_dict = {letter: 0 for letter in string.ascii_lowercase}
    for char in miscCharRemoved:
        letter_dict[char] += 1

    return letter_dict



main()
