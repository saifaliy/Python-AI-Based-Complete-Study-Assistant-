import tensorflow as tf
import numpy as np

# Updated and expanded dataset
questions = np.array([
    # Easy
    "What is 2 + 2?",
    "Name the capital of Italy.",
    "What color is the sky?",
    "What does CPU stand for?",

    # Medium
    "Explain the difference between RAM and ROM.",
    "What is a for loop used for in programming?",
    "Define the term 'function' in Python.",
    "What are HTTP methods?",

    # Hard
    "Explain the backpropagation algorithm in deep learning.",
    "What is the difference between supervised and unsupervised learning?",
    "How does the TCP 3-way handshake work?",
    "Describe the bias-variance tradeoff in machine learning."
])

labels = np.array([
    0, 0, 0, 0,      # easy
    1, 1, 1, 1,      # medium
    2, 2, 2, 2       # hard
])

# Convert text to sequences
vectorizer = tf.keras.layers.TextVectorization(max_tokens=1000, output_mode='int', output_sequence_length=10)
vectorizer.adapt(questions)

# Prepare dataset
X = vectorizer(questions)
y = tf.keras.utils.to_categorical(labels, num_classes=3)

model = tf.keras.Sequential([
    tf.keras.Input(shape=(10,)),
    tf.keras.layers.Embedding(input_dim=1000, output_dim=16),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X, y, epochs=50, verbose=0)

def classify_question(question: str) -> str:
    classes = ['easy', 'medium', 'hard']
    input_seq = vectorizer(np.array([question]))
    prediction = model.predict(input_seq)
    return classes[np.argmax(prediction)]

def classify_batch(questions: list[str]) -> list[str]:
    classes = ['easy', 'medium', 'hard']
    sequences = vectorizer(np.array(questions))
    predictions = model.predict(sequences)
    return [classes[np.argmax(p)] for p in predictions]
