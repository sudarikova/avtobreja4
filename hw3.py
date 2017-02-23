#!/usr/bin/python3
#-*- coding:utf-8-*-

import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab

with open('anna.txt', encoding='utf-8') as f:
    anna = f.read()
with open('sonets.txt', encoding='utf-8') as f:
    sonets = f.read()
anna = anna.lower()
sonets = sonets.lower()
anna_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', anna)
sonet_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', sonets)

def vowels (sentence):#количество гласных в предложении
	vow = u'ёуеыаоэяиюe'
	return sum(1 for i in sentence if i in vow)

def letters(sentence):#количество букв в предложении
	let = u'ёйцукенгшщзхъфывапролджэячсмитьбю'
	return sum(1 for j in sentence if j in let)

def unique_letters(sentence):#количество различных букв в предложении
	let = u'ёйцукенгшщзхъфывапролджэячсмитьбю'
	return len(set([k for k in sentence if k in let]))

def median_letters_word(sentence):#медиана числа букв в слове
	return np.median([len(word) for word in sentence.split()])

def median_vowels_word(sentence):#медиана числа гласных в слове
	return np.median([vowels(word) for word in sentence.split()])

anna_data = [(vowels(sentence), letters(sentence), unique_letters(sentence), median_letters_word(sentence), median_vowels_word(sentence)) for sentence in anna_sentences]
sonet_data = [(vowels(sentence), letters(sentence), unique_letters(sentence), median_letters_word(sentence), median_vowels_word(sentence)) for sentence in sonet_sentences]
anna_data = np.array(anna_data)
sonet_data = np.array(sonet_data)
plt.figure()
c1, c2 = 0, 1
plt.plot(anna_data[:,c1], anna_data[:,c2], 'og', 
         sonet_data[:,c1], sonet_data[:,c2], 'sb')
#plt.show()

data = np.vstack((anna_data, sonet_data))
p = mlab.PCA(data, True)
N = len(anna_data)
plt.plot(p.Y[:N,0], p.Y[:N,1], 'og', p.Y[N:,0], p.Y[N:,1], 'sb')
plt.show()

	

