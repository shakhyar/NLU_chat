model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(tf.keras.layers.AveragePooling1D())
model.add(tf.keras.layers.Conv1D(32, 4))
model.add(tf.keras.layers.Conv1D(16, 4))
model.add(tf.keras.layers.Flatten()) 
model.add(Dense(128, activation='elu'))
model.add(Dense(64, activation='elu'))
model.add(Dense(32, activation='elu'))
model.add(Dense(16, activation='elu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', 
              optimizer='adam', metrics=['accuracy'])

model.summary()