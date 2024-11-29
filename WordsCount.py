import csv

import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


'''Funzione per pulire il database togliendo numeri e punteggiatura e trasformando tutto in minuscolo'''
def clean_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha()]
    return tokens

'''Carico il dataset e lo preparo'''
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('realdonaldtrump.csv')
pd.set_option('display.max_rows', 1000000)
df = df.drop(df.columns[[0, 1,4,5,6,7]], axis=1)
df_restricted = df[['content', 'date']]
df_restricted['cleaned_words'] = df_restricted['content'].apply(clean_text)

'''Pulisco il dataset togliendo anche le stopwords'''

all_words = [word for words in df_restricted['cleaned_words'] for word in words]
stop_words = set(stopwords.words('english'))
all_words = [word for word in all_words if word not in stop_words]
all_words = [word for word in all_words if word != 'realdonaldtrump' and word != 'http' and word != 'https' and word != 'would' and word != 'get']
'''Studio la frequenza e stampo le parole con frequenza'''

word_freq = Counter(all_words)
file_name = "word_frequency.csv"
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['word', 'frequency'])
    for word, freq in word_freq.items():
        writer.writerow([word, freq])
most_common_words = word_freq.most_common(10)
words, counts = zip(*most_common_words)

'''Creo il grafico'''
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.title("Parole più frequenti nei Tweet")
plt.xlabel("Parole")
plt.ylabel("Frequenza")
plt.savefig("word_frequency.png", format='png', dpi=300)
plt.show()