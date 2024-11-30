import matplotlib.pyplot as plt
from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Define the model
model = Sequential([
    Embedding(input_dim=10000, output_dim=64, input_length=50),
    LSTM(64, return_sequences=True),
    Dropout(0.2),
    LSTM(32),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Save the model architecture as an image
plot_model(model, to_file='trump_musk_model.png', show_shapes=True)

# Optionally, display the image using matplotlib
img = plt.imread('trump_musk_model.png')
plt.imshow(img)
plt.axis('off')  # Hide axes for better presentation
plt.show()
