import pandas as pd
import re
from keras.src.saving import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

'''Preparazione database, da togliere possibilmente'''
pd.set_option('display.max_colwidth', None)
df_musk = pd.read_csv('elon_musk_tweets_only.csv')
df_musk.rename(columns={'text': 'content'}, inplace=True)
df_trump = pd.read_csv('TrumpTweetsOnly.csv')
df_musk['label'] = 0
df_trump['label'] = 1
pd.set_option('display.max_rows', 1000000)
df_total = pd.concat([df_musk, df_trump], ignore_index=True)

'''Funzione di pulizia del testo'''

def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

'''Tokenizing'''

tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(df_total['content'])
sequences = tokenizer.texts_to_sequences(df_total['content'])
padded_sequences = pad_sequences(sequences, maxlen=50, padding='post', truncating='post')

'''Carico il modello'''

model = load_model('trump_musk_classifier.h5')

'''Test di input'''

input_phrase = input('Enter a tweet: \n')
new_tweet = input_phrase  # Inserisci un tweet di test
new_tweet_cleaned = preprocess_text(new_tweet)
new_tweet_sequence = tokenizer.texts_to_sequences([new_tweet_cleaned])
new_tweet_padded = pad_sequences(new_tweet_sequence, maxlen=50, padding='post')
prediction = model.predict(new_tweet_padded)
print("Tweet di Trump" if prediction[0][0] > 0.5 else "Tweet di Musk")