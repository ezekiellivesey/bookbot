from collections import defaultdict

def count_chars(string):

    counter = dict() 

    for char in string:

        if char.isalpha():
            try:
                counter[char.lower()] +=  1
            except:
                counter[char.lower()] =  1 

    return counter

def print_report(num_words: int, char_count: dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print("%d words found in the document\n" % num_words)

    for letter in char_count:
        print("The '%c' character was found %d times" % (letter, char_count[letter]) )


    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = 0
        for word in file_contents.split():
            num_words +=1
        count : dict = (count_chars(file_contents))
        print_report(num_words, count)


main()
