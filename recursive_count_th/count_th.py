'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word.find('th') == -1:
        return 0
    else:
        new_word = word[word.find('th') + 1:]
        return 1 + count_th(new_word)