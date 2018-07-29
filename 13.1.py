import string

def read_file(filename):
    fin = open(filename, 'r', encoding='UTF-8')
    hist = {}
    for line in fin:
        word_list = line.split()
        for word in word_list:
            word = word.lower().strip(string.punctuation + string.whitespace)
            hist[word] = hist.get(word, 0) + 1
    return hist

def count_words(hist):
    return len(hist)

def most_frequence(hist, num):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t[0:num]

if __name__ == '__main__':
    hist = read_file('book.txt')
    print(count_words(hist))
    print(most_frequence(hist, 20))
