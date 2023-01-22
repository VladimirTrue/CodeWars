def in_array(array1, array2):
    res = set()
    [[res.add(word_1) for word_2 in array2 if word_1 in word_2] for word_1 in array1]
    return sorted(res)
