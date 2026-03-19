# day_5_random_distributions.py

import numpy as np

# ===============================
# 1. Random Number Generation
# ===============================

print("=== Random Numbers ===")
print("Uniform (0 to 1):", np.random.rand(3))
print("Standard Normal:", np.random.randn(3))


# ===============================
# 2. Using Seed (Reproducibility)
# ===============================

print("\n=== Seed Example ===")
# np.random.seed(12)
print("Seed 12:", np.random.rand(3))

# np.random.seed(42)
print("Seed 42:", np.random.rand(3))


# ===============================
# 3. Uniform Distribution
# ===============================

print("\n=== Uniform Distribution Stats ===")
uniform_data = np.random.rand(1000)

print("Mean (Uniform):", np.mean(uniform_data))
print("Std (Uniform):", np.std(uniform_data))


# ===============================
# 4. Normal Distribution
# ===============================

print("\n=== Normal Distribution Stats ===")
normal_data = np.random.randn(1000)

print("Mean (Normal):", np.mean(normal_data))
print("Std (Normal):", np.std(normal_data))


# ===============================
# 5. Random Integers
# ===============================

print("\n=== Random Integers ===")
print("Single integer (0 - 9):", np.random.randint(0, 10))
print("Array of integers:", np.random.randint(0, 10, size=3))


# ===============================
# 6. Seed Behavior Demonstration
# ===============================

print("\n=== Seed Sequence Behavior ===")
# np.random.seed(42)
print("First call:", np.random.randint(1, 10, size=5))
print("Second call (same seed, next sequence):", np.random.randint(1, 10, size=5))


# ===============================
# 7. Custom Normal Distribution
# ===============================

print("\n=== Normal Distribution (Custom Mean & Std) ===")

# Mean = 50, Std = 10
data = np.random.normal(50, 10, size=10)
print("Mean=50, Std=10:", data)

# Smaller spread
print("Mean=50, Std=2:", np.random.normal(50, 2, size=10))

# Larger spread
print("Mean=50, Std=20:", np.random.normal(50, 20, size=10))



# =================
# Random Choice 
# =================
#np.random.choice(array,size)

arr=[1,2,3,4,5,6]
print(np.random.choice(arr,2))



# ======================
# Binomial Distribution
# ======================
#n= number of trials
#p= probabilty (which's can't be greater than 1)
#size= size of an array
print(np.random.binomial(n=10, p=0.5, size=5))



