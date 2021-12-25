# ----------------------------------------------------------
# --------                 HW 9                   ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Name:
# Time spent on homework:
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

import string

def get_words(comment):
    """
    Get a list of words (in lowercase without punctuation) from a written 
    comment
     
    >>> get_words('A review without punctuation')
    ['a', 'review', 'without', 'punctuation']
    >>> get_words('This includes: punctuation.')
    ['this', 'includes', 'punctuation']
    """
    words = comment.strip().split()

    # Remove punctuation and convert to lowercase
    i = 0
    while i < len(words):
        cleaned = ''
        for ch in words[i]:
            if ch in string.ascii_letters or ch in string.digits:
                cleaned += ch.lower()
        if len(cleaned) == 0:
            del words[i]
        else:
            words[i] = cleaned
            i += 1

    return words

def train(filename):
    """
    Compute word scores from a file of training data

    >>> train('hw9_small_train.txt')
    {'this': 3.0, 'product': 3.0, 'is': 3.5, 'good': 5.0, 'well': 4.5, 'made': 5.0, 'functions': 4.0, 'a': 3.0, 'mediocre': 3.0, 'broke': 2.0, 'i': 2.0, 'am': 2.0, 'dissatisfied': 2.0, 'junk': 1.0, 'does': 1.0, 'not': 1.0, 'function': 1.0, 'as': 1.0, 'advertised': 1.0}
    """
    # TODO


def analyze(model, filename):
    """
    Compute numeric ratings for a file of written comments

    >>> analyze({'this': 3.0, 'product': 3.0, 'is': 3.5, 'good': 5.0, 'well': 4.5, 'made': 5.0, 'functions': 4.0, 'a': 3.0, 'mediocre': 3.0, 'broke': 2.0, 'i': 2.0, 'am': 2.0, 'dissatisfied': 2.0, 'junk': 1.0, 'does': 1.0, 'not': 1.0, 'function': 1.0, 'as': 1.0, 'advertised': 1.0}, 'hw9_small_analyze.txt')
    [(3.5, 'This product works very well.'), (2.7, 'This product is a piece of junk.'), (4.0, 'Very poorly made product!')]
    """
    # TODO


def main():
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
