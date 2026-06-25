# dummy_NumPy-MLP

A lightweight Command Line Interface (CLI) tool that simulates the mathematical "forward pass" of a Multi-Layer Perceptron (MLP) from scratch using Python and NumPy.

## 📌 Project Overview
This project was built as a personal logic exercise to explore matrix multiplication chains and dynamic data structures before officially starting my machine learning journey. 

Instead of using deep learning frameworks (like PyTorch or TensorFlow), this script uses pure programming logic and basic array manipulation to handle dimensions dynamically, initialize random weights, and simulate neural layer operations.

## ⚙️ How It Works
The script runs in the terminal and executes the following pipeline:
1. **Dynamic Input:** Takes a sequence of integers from the user to establish a "dimension chain" (representing layer sizes).
2. **Weight Generation:** Uses NumPy (`np.random.randn`) to automatically initialize matrices with random positive and negative decimals based on the dimension pairs.
3. **Chained Processing:** Runs an $O(n)$ loop to multiply the matrices sequentially while keeping a flat memory footprint (overwriting the tracking variable rather than saving every intermediate step).
4. **Activation Masking:** Implements an element-wise NumPy mask (`matrix[matrix < 0] = 0`) after each multiplication step to simulate a **ReLU (Rectified Linear Unit)** activation function.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** NumPy

## 🧠 What I Learned From This Build
* How to manage and manipulate multidimensional data arrays efficiently.
* How to prevent "off-by-one" index boundary errors when handling sliding-window pairs in a loop.
* The foundational math underlying how data moves forward through a multi-layer neural network architecture.