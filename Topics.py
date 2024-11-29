import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

'''Funzione per pulire tweet'''
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

'''Tolgo stopwords'''
stop_words = set(stopwords.words('english'))
def extract_topics_filtered(text):
    blob = TextBlob(text)
    # Filtra le frasi nominali rimuovendo le stopwords
    return [word for word in blob.noun_phrases if word not in stop_words]
df_restricted['topics'] = df_restricted['content'].apply(extract_topics_filtered)
df_topics = df_restricted[['content', 'date', 'topics']]

'''Tolgo outliers'''
all_topics = [topic for sublist in df_restricted['topics'] for topic in sublist]
all_topics = [topic for topic in all_topics if topic
              != '@realdonaldtrump' and topic != 'thank' and topic != 'thanks' and topic != "'s" and topic != 'donald trump' and topic !='@ realdonaldtrump' and topic != '@ realdonaldtrump @'
and topic != 'barackobama' and topic!='via' ]

'''Conto frequenza'''
topic_freq = Counter(all_topics)
sorted_topics = topic_freq.most_common()
topic_df = pd.DataFrame(sorted_topics, columns=['Topic', 'Frequency'])

'''grafico'''
plt.figure(figsize=(10,6))
plt.bar(topic_df['Topic'][:10], topic_df['Frequency'][:10], color='skyblue')
plt.title('Top 10 Topics Frequencies', fontsize=14)
plt.xlabel('Topics', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('topic_frequencies.png')
plt.show()
