# Epoch in Deep Learning
---
### App Link : https://epoch-in-deep-learning.streamlit.app/
---
## Definition :

* An **epoch** is **one full cycle** through the **entire training dataset**.
* When training a model, the data is passed forward and backward **once** in an epoch.
* More epochs help the model **learn better**, but too many can cause **overfitting**.

---

## Why Are Epochs Important?

* They help the model **improve accuracy** step by step.
* With each epoch, the model **adjusts its weights** to make better predictions.
* The training does not happen all at once, it learns **bit by bit** over several epochs.

---

## Common Terms Related to Epochs

* **Batch Size** : How many samples are trained at once.
* **Iterations** : How many batches are there in one epoch.
* **Overfitting** : When a model learns **too much** and performs poorly on new data.

---
## Training Data

```python
X = [1, 2, 3, 4, 5]  # Inputs  
Y = [2, 4, 6, 8, 10]  # Outputs (X * 2)
```

We want the Model to **learn** 
> **Multiply input by 2**

---
## Expected Output
- We enter a number **25.00**, i.e., **`model.predict(np.array([25.00]))`**
- After training, the model will predict the **output** → approximately **≈ 50**
---
## Additional Insights :
- Most models are trained using **10 to 100 epochs**.
- Early stopping is used to **stop training** when the model **starts overfitting**.
- We can plot **loss** vs **epoch** to see how well a model is learning.
---
