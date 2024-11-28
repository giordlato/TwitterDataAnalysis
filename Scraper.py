import pandas as pd
# Carica il dataset (modifica il percorso se necessario)
df = pd.read_csv('realdonaldtrump.csv')
print(df)
df = df.drop(df.columns[[0, 1,4,5,6,7]], axis=1)
# Esplora i dati (prima riga per capire la struttura)
print(df)
df=df.apply(str)
# Pre-elaborazione del testo: rimozione di simboli speciali, numeri, e stopwords
import re
from nltk.corpus import stopwords

# Carica le stopwords (se non lo hai fatto prima, puoi installarle con: nltk.download('stopwords'))
stop_words = set(stopwords.words('english'))

import re
df = df.apply(lambda x: re.sub(r'[^\w\s]', '', x))
text = text.lower()
print(df)
print(df)
# Esplora il risultato
#print(df[['text', ''''cleaned_text']].head())

