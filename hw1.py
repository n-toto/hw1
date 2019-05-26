import copy
import re
import collections

#import dictionary containing words whose word length is 16 or less
dic_16 = []
with open("dictionary.txt", 'r') as f:
    for line in f:
        dic_16.append(line.replace("\n", ""))

#make a small dictionary that contains words which is consisted of  only given characters
def mk_new_dic(s):
    new_dic = []
    match = ''.join(sorted(set(s)))
    for v in dic_16:
        if re.search("[^"+match+"]", v) == None:
            new_dic.append(v)
    return new_dic

#make a list of words which can be the answer
def mk_match(new_dic, s):
    counter = collections.Counter(s)
    l = []
    for word in new_dic:
        if all(map(lambda items: word.count(items[0]) <= items[1], counter.items())) == True:
            l.append(word)
    return l

def point(word):
    count = 0
    word = re.sub("QU", "Q", word, re.I)
    c3 = re.findall("[JKXZQ]", word, re.I)
    count += 3 * len(c3)
    c2 = re.findall("[CFHLMPVWY]", word, re.I)
    count += 2 * len(c2)
    c1 = re.findall("[^JKQXZCFHLMPVWY]", word, re.I)
    count += len(c1)
    return (count) ** 2

def mk_best_word(original):
    new_dic = mk_new_dic(original)
    word_list = mk_match(new_dic, original)
    d = {}
    for word in word_list:
        d[word] = point(word)
    d = sorted(d, key = lambda x : d[x], reverse = True)
    return d[0], point(d[0])

#receive16 characters
for i in range(10):
    original = list(input().lower().split())
    print(mk_best_word(original))