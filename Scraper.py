import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

'''Funzione per avere il sentiment'''
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity


'''Carico il dataset'''
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('realdonaldtrump.csv')
pd.set_option('display.max_rows', 1000000)
df = df.drop(df.columns[[0, 1,4,5,6,7]], axis=1)
df_restricted = df[['content', 'date']]

'''Ottengo il sentiment'''
df_restricted['sentiment'] = df_restricted['content'].apply(get_sentiment)

'''Preparo il dataframe per analisi temporale'''
df_restricted.to_csv('sentiment.csv', index=False, encoding='utf-8', sep=';', quoting=1)
df_restricted = df_restricted.dropna(subset=['sentiment'])
df_restricted['sentiment'] = df_restricted['sentiment'].apply(pd.to_numeric, errors='coerce')
df_restricted['date'] = pd.to_datetime(df_restricted['date'])
df_restricted['month_year'] = df_restricted['date'].dt.to_period('M')  # Usa la forma M per avere solo mese e anno
df_monthly_sentiment = df_restricted.groupby('month_year')['sentiment'].mean().reset_index()
df_monthly_sentiment['date'] = df_monthly_sentiment['month_year'].dt.to_timestamp()
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_monthly_sentiment, x='date', y='sentiment', marker='o', color='blue')
plt.title('Media Mensile del Sentiment nei Tweet')
plt.xlabel('Mese')
plt.ylabel('Sentiment Medio')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("sentiment.png", format='png', dpi=300)
plt.show()