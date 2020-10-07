"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Open the file and turn it into one long string
    #input_text = open_and_read_file(input_path)
    input_text = open(file_path)
    string = ''
    for line in input_text:
        line = " ".join(line.split())
        string = f'{string} {line}'
        string = string.strip()
    input_text.close()
    return string

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    string = open_and_read_file(file_path)
    string.append(None)
    chains = {}
    words = text_string.split(' ')
    words.append(None)
    for i in range(len(words)-2):
        bi_gram = text_string.split(' ')[i:i+2]
        chains[tuple(bi_gram)] = [] 

    return chains


def make_text(chains):
    """Return text from chains."""
    keys = sorted(chains)
    string = open_and_read_file(file_path)
    words = string.split()
    words.append(None)
    for i in range(len(words)):
        if i + 2 == len(words):
            break
        key = (words[i], words[i+1])
        chains[key].append(words[i+2])
    random_start = choice(keys)
    
    words = [random_start[0], random_start[1]]
    key = (random_start[0], random_start[1])
    word = choice(chains[key])
    
    while word is not None:
        key = (key[1], word)
        words.append(word)
    
    return ' '.join(output_list)

input_path = 'green-eggs.txt'
file_path = input_path
# Get a Markov chain

# Produce random text
#random_text = make_text(chains)


#print(random_text)
string = open_and_read_file('green-eggs.txt')
chains = make_chains(string)
make_text(chains)