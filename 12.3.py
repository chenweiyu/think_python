import itertools

def read_file(s):
    words = {}
    fin = open(s)
    for word in fin:
        words.setdefault(''.join(sorted(word.strip())), []).append(word.strip())
    return words

def find_metatheisi(words):
    result = []
    for key in words:
        if len(words[key]) > 1:
            for word1, word2 in itertools.combinations(words[key], 2):
                if compare_words(word1, word2):
                    result.append([word1, word2])
    return result

def compare_words(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
            if count > 2:
                return False
    return True

if __name__ == '__main__':
    words = (read_file('words.txt'))
    print(find_metatheisi(words))