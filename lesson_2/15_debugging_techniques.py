def titlize(sentence):
    words = sentence.split()
    # print(words)
    new_words = []

    for word in words:
        # print(word)
        if len(word) > 2:
            # print(word)
            # word.capitalize()         # old code with bug
            # print(word)
            word = word.capitalize()    # new code
            # print(word)
            # new_words.append(word)    # old code with incorrect indentation
            # print(new_words)
        new_words.append(word)          # new code

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))
# titlize(title)        # to see only the debugging print() statements 