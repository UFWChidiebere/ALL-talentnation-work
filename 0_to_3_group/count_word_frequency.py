def word_frequency(sentence: str)-> dict[str, int]:
    w_f = {}
    words = sentence.split()
    # word_count = 0
    for word in words:
    # for word in sentence:
        if word not in w_f:
            w_f[word] = 1
            # word_count +=1
        else:
            w_f[word] += 1
    return w_f

sentence = "the quick brown fox jumps over the lazy dog"
print(word_frequency(sentence))
