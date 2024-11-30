import pandas as pd
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

'''Preparazione database'''
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
    text = re.sub(r'http\S+', '', text)  # Rimuovi URL
    text = re.sub(r'@\w+', '', text)    # Rimuovi menzioni
    text = re.sub(r'#\w+', '', text)    # Rimuovi hashtag
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Rimuovi punteggiatura e numeri
    text = text.lower()  # Converti in minuscolo
    return text

'''Pulizia'''

df_total['content'] = df_total['content'].apply(preprocess_text)

'''Tokenizing'''

tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(df_total['content'])
sequences = tokenizer.texts_to_sequences(df_total['content'])
padded_sequences = pad_sequences(sequences, maxlen=50, padding='post', truncating='post')

'''Costruzione rete'''

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, df_total['label'], test_size=0.2, random_state=42)
model = Sequential([
    Embedding(input_dim=10000, output_dim=64, input_length=50),
    LSTM(64, return_sequences=True),
    Dropout(0.2),
    LSTM(32),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')  # Classificazione binaria
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

'''Addestramento'''

model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test), batch_size=32)

'''Valutazione'''
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
model.save('trump_musk_classifier.h5')

'''Test'''

new_tweet = "Make America Great Again!"  # Inserisci un tweet di test
new_tweet_cleaned = preprocess_text(new_tweet)
new_tweet_sequence = tokenizer.texts_to_sequences([new_tweet_cleaned])
new_tweet_padded = pad_sequences(new_tweet_sequence, maxlen=50, padding='post')
prediction = model.predict(new_tweet_padded)
print("Tweet di Trump" if prediction[0][0] > 0.5 else "Tweet di Musk")