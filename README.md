# 🔢 NumPy 7-Day Learning Journey

> **From zero to matrix operations** — a structured, project-based NumPy study plan covering everything from array creation to linear algebra, built while following a university AI course.

---

## 📌 About This Repository

This repo documents my **7-day hands-on journey** through NumPy — the foundational library for scientific computing and AI in Python. Each day has a focused topic, daily practice tasks, and a mini project that demonstrates what I learned.

No tutorials were passively watched. Every file here was written from scratch.

---

## 🗺️ Roadmap Overview

| Day | Topic | Concepts Covered | Project |
|-----|-------|-----------------|---------|
| 1 | Zero to Array | ndarray, creation functions, dtypes, attributes | Array Zoo Reporter |
| 2 | Indexing & Slicing | 1D/2D indexing, views vs copies, boolean masks | Student Grade Filter |
| 3 | Math & Vectorization | Arithmetic, ufuncs, broadcasting, np.where | Temperature Converter |
| 4 | Reshape, Stack & Stats | reshape, ravel, vstack, axis-wise statistics | Sales Data Analyzer |
| 5 | Random & Distributions | Seeding, distributions, Monte Carlo | Monte Carlo Pi Estimator |
| 6 | Linear Algebra | Matrix ops, np.linalg, normal equations | Linear Regression from Scratch |
| 7 | Consolidation | Review all concepts, fill gaps | Cricket Stats Analyzer |

---

## 📁 Project Files

```
numpy-journey/
│
├── day_1_array_zoo.py          # Array creation, dtypes, attributes
├── day_2_grade_filter.py       # Boolean indexing, slicing on student data
├── day_3_temperature.py        # Vectorized ops, np.where, broadcasting
├── day_4_sales_analyzer.py     # Reshape, stacking, axis-wise statistics
├── day_5_monte_carlo_pi.py     # Random module, simulation, π estimation
├── day_6_linear_regression.py  # Matrix ops, linalg, normal equation
├── day_7_cricket_stats.py      # Full consolidation — all concepts combined
└── README.md
```

---

## 📖 Day-by-Day Breakdown

### Day 1 — Zero to Array
**Goal:** Understand what NumPy is and why it exists. Create arrays of every kind.

Key things learned:
- `np.array()`, `np.zeros()`, `np.ones()`, `np.eye()`, `np.empty()`
- `np.arange()` vs `np.linspace()`
- Array attributes: `.shape`, `.ndim`, `.size`, `.dtype`
- Type casting with `.astype()`

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
matrix = np.zeros((3, 4))
seq = np.linspace(0, 1, 5)  # [0.0, 0.25, 0.5, 0.75, 1.0]

print(arr.shape, arr.dtype)
```

**Project:** Built a script that creates 1D, 2D, and 3D arrays and prints a formatted report of their shape, ndim, size, and dtype.

---

### Day 2 — Indexing & Slicing
**Goal:** Access, filter, and modify data inside arrays without loops.

Key things learned:
- Positive and negative indexing
- Slicing with `start:stop:step`
- Views vs copies — modifying a slice changes the original
- Boolean masking and fancy indexing
- Combining conditions with `&` and `|`

```python
arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[2:5])          # [30, 40, 50]
print(arr[arr > 25])     # [30, 40, 50, 60]
arr[arr < 20] = 0        # Replace values in-place
```

**Project:** A 2D array of 10 students × 5 subject scores — filtered failing students, extracted columns, replaced low scores.

---

### Day 3 — Math & Vectorization
**Goal:** Perform mathematical operations on entire arrays at once. No loops.

Key things learned:
- Element-wise arithmetic between arrays
- Broadcasting: how NumPy handles different shapes
- Universal functions (ufuncs): `np.sqrt`, `np.exp`, `np.abs`, `np.log`
- `np.where()` as a vectorized if-else
- `np.clip()` to bound values

```python
arr = np.array([1, 4, 9, 16, 25])
print(np.sqrt(arr))      # [1. 2. 3. 4. 5.]

temps = np.random.randint(-10, 40, 365)
labels = np.where(temps > 30, 'Hot', np.where(temps > 10, 'Mild', 'Cold'))
```

**Project:** 365-day temperature array — converted Celsius to Fahrenheit, labelled weather types, found hottest month.

---

### Day 4 — Reshape, Stack & Statistics
**Goal:** Transform array shapes and summarize data along axes.

Key things learned:
- `reshape()` — the `-1` trick for auto-calculating dimensions
- `ravel()` (view) vs `flatten()` (copy)
- `np.vstack()`, `np.hstack()`, `np.concatenate()`
- Statistics: `mean()`, `sum()`, `std()`, `var()`, `median()`, `percentile()`
- `axis=0` (column-wise) vs `axis=1` (row-wise)

```python
arr = np.arange(12).reshape(3, -1)   # 3×4 matrix

sales = np.random.randint(100, 500, (4, 7))
weekly_totals = sales.sum(axis=1)     # one total per week
daily_avg = sales.mean(axis=0)        # one avg per day of week
```

**Project:** Sales matrix (4 weeks × 7 days) — weekly totals, daily averages, best/worst days, month comparison.

---

### Day 5 — Random Module & Distributions
**Goal:** Generate random data and run simulations.

Key things learned:
- `np.random.seed()` for reproducibility
- `rand()`, `randn()`, `randint()`, `normal()`, `choice()`
- The Monte Carlo method — estimating π with random points

```python
np.random.seed(42)

# Estimate pi using Monte Carlo
n = 1_000_000
x, y = np.random.rand(n), np.random.rand(n)
inside = np.sum(x**2 + y**2 <= 1)
pi_estimate = 4 * inside / n
print(f"π ≈ {pi_estimate}")   # ~3.1416
```

**Project:** π estimation at 1K, 10K, 100K, 1M points — watched accuracy improve with scale.

---

### Day 6 — Linear Algebra
**Goal:** Understand the matrix operations that power machine learning.

Key things learned:
- `@` operator for matrix multiplication vs `*` for element-wise
- `.T` for transpose
- `np.linalg.det()`, `np.linalg.inv()`, `np.linalg.solve()`
- `np.linalg.eig()` for eigenvalues and eigenvectors
- Solving linear systems: `Ax = b`
- Normal equation for linear regression: `w = (XᵀX)⁻¹Xᵀy`

```python
# Solving a system of equations
A = np.array([[2, 1], [1, 3]])
b = np.array([8, 13])
solution = np.linalg.solve(A, b)   # [3. 2.]

# Verify
print(A @ solution)   # Should equal b
```

**Project:** Generated synthetic data, derived weights using the normal equation, predicted on test data, computed MSE.

---

### Day 7 — Consolidation
**Goal:** Review all 6 days by building one clean project using everything together.

What I practiced:
- 3D arrays, reshape, slicing (Day 1-2)
- Ufuncs and np.where (Day 3)
- vstack, axis-wise stats (Day 4)
- Random data, verified with mean/std (Day 5)
- Matrix inverse, identity check (Day 6)
- Min-max normalization, np.argsort, boolean masking

```python
# Cricket Stats Analyzer — the consolidation project
np.random.seed(0)
scores = np.random.randint(0, 150, (10, 5))   # 10 players, 5 matches

averages = scores.mean(axis=1)
top_3_idx = np.argsort(averages)[::-1][:3]
scores[scores < 20] = 0   # replace low scores

# Normalize to [0, 1]
normalized = (scores - scores.min()) / (scores.max() - scores.min())
```

---

## 🧠 Key Takeaways

**Vectorization is everything.** The biggest mindset shift in NumPy is learning to think in arrays, not loops. A for-loop that takes 3 seconds becomes 0.06 seconds with NumPy.

**Views vs copies will bite you.** Slicing returns a view — changing the slice changes the original. Always use `.copy()` when you need independence.

**Axis direction matters.** `axis=0` goes *down the rows* (column-wise result). `axis=1` goes *across columns* (row-wise result). Gets confusing — draw it out.

**Broadcasting is magic once you understand it.** NumPy automatically expands smaller arrays to match larger ones — but only when shapes are compatible.

---

## 🛠️ Setup

```bash
pip install numpy
python day_1_array_zoo.py
```

Requires Python 3.8+ and NumPy 1.20+.

---

## 📚 Resources Used

- [NumPy Official Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)
- Lecture slides: *Practical AI — Lecture 3, Numerical Python*

---

## 🗺️ What's Next

This repo covers NumPy fundamentals. The next steps in the journey:

- **Pandas** — data manipulation and analysis
- **Matplotlib / Seaborn** — data visualization  
- **Scikit-learn** — machine learning on top of NumPy arrays

---

*Built as part of a structured AI/ML learning path. Each project was coded independently without copying — the goal was understanding, not completion.*