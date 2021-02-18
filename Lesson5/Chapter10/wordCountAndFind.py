def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words.")

def findWords(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.lower().count(word)
        print(f"The file {filename} has the word '{word}' in it {words} times.")

filenames = ['Lesson5\Chapter10\\thisIsJustToSay.txt', 'Lesson5\Chapter10\\theApplicant.txt' , 'Lesson5\Chapter10\stoppingByWoodsOnASnowyEvening.txt']
for filename in filenames:
    count_words(filename)
    
word = input('what word would you like to count within the poems? ')
for filename in filenames:
    findWords(filename, word)