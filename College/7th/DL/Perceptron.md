```markdown
# 🔹 Conceptual Questions

**Q1: Define a perceptron. What are its components?**  
A1: A perceptron is the simplest type of artificial neural network, used for binary classification. It consists of:
- Inputs (features)  
- Weights (associated with each input)  
- Bias (a constant term)  
- Activation function (usually step or sign function)  
- Output (0 or 1)  

---

**Q2: Explain the working of the perceptron algorithm with an example.**  
A2: The perceptron calculates the weighted sum of inputs plus bias and passes it through an activation function.  
If the result is greater than 0, it outputs 1; otherwise, 0.  
During training, it adjusts weights based on the prediction error using the rule:  
`w_i ← w_i + η (y - ŷ) x_i`

---

**Q3: What are the limitations of a single-layer perceptron?**  
A3: It can only solve linearly separable problems. It cannot solve problems like XOR that are not linearly separable.

---

**Q4: What is the difference between perceptron and logistic regression?**  
A4: Both are linear classifiers, but:  
- Perceptron uses a step function (hard threshold) for binary output.  
- Logistic regression uses the sigmoid function and outputs probabilities.  
- Logistic regression uses gradient descent; perceptron uses simple error-based updates.  

---

**Q5: Why can’t a single-layer perceptron solve the XOR problem?**  
A5: XOR is not linearly separable, meaning no straight line can divide the classes. A single-layer perceptron only models linear decision boundaries.

---

**Q6: What is the role of the activation function in a perceptron?**  
A6: The activation function decides the output of the perceptron. It introduces non-linearity and helps map the input to the output class.

---

**Q7: What is linear separability? Why is it important in perceptron learning?**  
A7: Linear separability means the data can be separated by a straight line (or hyperplane).  
The perceptron algorithm converges only if the data is linearly separable.

---

# 🔹 Mathematical/Algorithmic Questions

**Q8: Derive the weight update rule for the perceptron learning algorithm.**  
A8: The perceptron updates its weights when it makes a mistake using:  
```

w_i ← w_i + η (y - ŷ) x_i
b ← b + η (y - ŷ)

````
Where η is the learning rate, y is the actual label, and ŷ is the predicted output.

---

**Q9: Explain the perceptron learning algorithm step-by-step.**  
A9:
1. Initialize weights and bias to zero or small random numbers.  
2. For each training sample:  
   - Compute the weighted sum: `z = w·x + b`  
   - Apply activation function: output = 1 if z > 0 else 0  
   - Update weights if prediction is wrong:  
     ```
     w_i ← w_i + η (y - ŷ) x_i  
     b ← b + η (y - ŷ)
     ```
3. Repeat for multiple epochs or until convergence.

---

**Q10: Given a small dataset, perform one iteration of the perceptron learning algorithm manually.**  
A10: For example, with inputs x1=1, x2=0, weights w1=0.5, w2=0.5, bias=0, learning rate η=1, target y=1:  
- z = (0.5 * 1) + (0.5 * 0) + 0 = 0.5  
- output = 1 (since z > 0)  
- ŷ = 1, y = 1 → No update needed  

---

**Q11: What is the convergence theorem of perceptron? State the conditions under which perceptron converges.**  
A11: The Perceptron Convergence Theorem states that if the data is linearly separable, the perceptron algorithm will converge to a solution in a finite number of steps.

---

**Q12: Given a truth table (like AND or OR), construct a perceptron model with suitable weights and bias.**  
A12: For AND gate:  
- Inputs: x1, x2  
- Weights: w1 = 1, w2 = 1  
- Bias: b = -1.5  
- Activation: Step function  

This gives correct output for all combinations of x1 and x2.

---

# 🔹 Practical/Code-Based Questions

**Q13: Write a Python function to implement the perceptron learning algorithm.**  
A13:
```python
def perceptron(X, y, lr=1, epochs=10):
    w = [0] * len(X[0])
    b = 0
    for _ in range(epochs):
        for xi, target in zip(X, y):
            z = sum(wi * xi_i for wi, xi_i in zip(w, xi)) + b
            y_pred = 1 if z > 0 else 0
            error = target - y_pred
            w = [wi + lr * error * xi_i for wi, xi_i in zip(w, xi)]
            b = b + lr * error
    return w, b
````

---

**Q14: How can you implement a perceptron using scikit-learn? Explain with code.**
A14:

```python
from sklearn.linear_model import Perceptron
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]  # AND gate
clf = Perceptron(max_iter=1000, eta0=1, random_state=0)
clf.fit(X, y)
print(clf.predict([[1, 1]]))  # Output: [1]
```

---

**Q15: Compare the output of a perceptron model for different learning rates.**
A15: Learning rate affects how fast the model learns:

* Small η → slow convergence, but more stable
* Large η → faster, but may overshoot or fail to converge

It's ideal to test different η values (e.g., 0.01, 0.1, 1) and compare accuracy and convergence speed.

---

# 🔹 Short Answer / Objective Type

**Q16: Which activation function is used in the basic perceptron?**
A16: Step function or sign function.

---

**Q17: What happens if the learning rate is too high or too low?**
A17:

* Too high → unstable learning, overshooting.
* Too low → very slow learning.

---

**Q18: What type of problems can be solved by a single-layer perceptron?**
A18: Linearly separable binary classification problems (e.g., AND, OR).

---

**Q19: What are weights and bias in a perceptron?**
A19:

* Weights control the influence of each input.
* Bias shifts the activation threshold.

---

**Q20: State true or false: A perceptron can learn any binary function.**
A20: False. It can only learn linearly separable functions.

```
```