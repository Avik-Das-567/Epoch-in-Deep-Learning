import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Data
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)

# Model
model = Sequential()
model.add(Dense(units=1, input_shape=[1]))

# Learning setup
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train with 100 repetitions (epochs)
model.fit(X, Y, epochs=100)

st.markdown("#### Training Data :-")
st.write("X =", X)
st.write("Y =", Y)

n = st.number_input("Please enter a floating-point number : ")
st.markdown(f"#### For Input {n}, the Predicted Output  is :-")
st.write(model.predict(np.array([n])))
