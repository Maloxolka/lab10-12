def split_syllables(word):
    morphemes = []
    phonemes = ['æ', 'ɒ', 'â', 'a', 'e', 'i', 'o', 'u', '0', '1', '2']

    word = word.replace('ei', '0')
    word = word.replace('ou', '1')
    word = word.replace('ye', '2')

    i = 0
    last_i = 0
    while i < len(word):
        if word[i] in phonemes:
            j = i + 1
            const_count = 0
            while j < len(word) and word[j] not in phonemes:
                const_count += 1
                if const_count > 1:
                    i += 1
                j += 1
            morphemes.append(word[last_i:i + 1])
            last_i = i+1
        i += 1
    morphemes[-1] += word[last_i:]

    for i in range(len(morphemes)):
        morphemes[i] = morphemes[i].replace('0', 'ei')
        morphemes[i] = morphemes[i].replace('1', 'ou')
        morphemes[i] = morphemes[i].replace('2', 'ye')

    return '-'.join(morphemes)
