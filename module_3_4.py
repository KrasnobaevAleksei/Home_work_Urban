def single_root_words(root_word, *other_word):
    same_words = []
    for i in other_word:
        if (root_word.lower().count(i.lower()) != 0 or
            i.lower().count(root_word.lower()) != 0) :
            same_words.append(i)
    return same_words

result1 = single_root_words('rich',
                          'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement',
                            'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
