# most frequent word from text
def freqWord(text):
    text_list = text.split()
    word_count = {}
    count = 1
    for i in range(len(text_list)):
        if text_list[i] not in word_count:
            word_count[text_list[i]] = count
        else:
            word_count[text_list[i]]+= 1
    get_value = list(word_count.values())
    return sorted(get_value)[len(get_value)-1]


print(freqWord("one fish two fish red fish blue fish"))
