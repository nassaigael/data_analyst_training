# 📊 Data Analyst Training Project

> A comprehensive data analysis training project with Python

![Badge Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Badge Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
![Badge License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📚 Table of Contents

- [🎯 Objective](#-objective)
- [📁 Project Structure](#-project-structure)
- [🗓️ Week 1](#️-week-1)
- [🛠️ Installation](#️-installation)
- [📝 Usage](#-usage)
- [✨ Features](#-features)

---

## 🎯 Objective

This project provides progressive training in data analysis with Python, covering the fundamentals of programming through advanced data manipulation techniques.

---

## 📁 Project Structure

```
data_analyst/
├── week_one/
│   ├── day_01/     ← Python Fundamentals
│   ├── day_02/     ← Data Structures
│   ├── day_03/     ← CSV & JSON Manipulation
│   └── day_04/     ← NumPy & Arrays
└── README.md
```

---

## 🗓️ Week 1

### 📅 Day 1 - Python Fundamentals

<table>
<tr>
<td width="50%">

**Exercise 1: Variable Types**
- Integer, float, string, and boolean variables
- Type checking with `type()`

**Exercise 2: Operations**
- Arithmetic operations
- String operations

**Exercise 3: Conditions**
- if/elif/else structures
- Comparisons and boolean logic

</td>
<td width="50%">

```python
# Day 1 Example
var_int = 156
var_float = 3.14
var_str = "Hello, World!"
var_bool = False

print(type(var_int))  # <class 'int'>
```

</td>
</tr>
</table>

---

### 📅 Day 2 - Data Structures

| Exercise | Description | Key Concepts |
|----------|-------------|--------------|
| **Exercise 1** | Lists and manipulations | append, remove, indexing |
| **Exercise 2** | Dictionaries | keys, values, items |
| **Exercise 3** | Tuples and sets | immutability, uniqueness |

---

### 📅 Day 3 - Data Manipulation (CSV & JSON) 🔥

<table>
<tr>
<td width="50%">

#### 📄 Exercise 1: CSV
CSV file processing:
- Reading and writing
- Calculating averages
- Filtering data
- Processing JSON files

**Data Files:**
- `students_rates.csv`
- `average_scores.csv`
- `config.json`
- `input.json`
- `news.json`

</td>
<td width="50%">

```python
# CSV Example
import csv

def calculate_average(input_file, output_file):
    scores = {"math": [], "reading": []}
    
    with open(input_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            scores["math"].append(float(row["math"]))
```

</td>
</tr>
</table>

#### 📋 Exercise 2 & 3
- Complex data parsing
- Data transformation and normalization
- Result export

---

### 📅 Day 4 - NumPy & Arrays 🚀

<table>
<tr>
<td width="50%">

#### 🔢 Exercise 1: NumPy Basics
- Random array generation
- Min/max operations
- Normalization between 0 and 1
- Descriptive statistics

**Concepts:**
```python
np.random.randint()
np.min(), np.max()
Normalization: (x - min) / (max - min)
```

</td>
<td width="50%">

```python
import numpy as np

# NumPy Example
array = np.random.randint(1, 1000, 100)
min_val = np.min(array)
max_val = np.max(array)

# Normalization
normalized = (array - min_val) / (max_val - min_val)
```

</td>
</tr>
</table>

#### 📊 Exercise 2: Advanced Operations
- Matrix manipulations
- Aggregations
- Data transformations

---

## 🛠️ Installation

### Requirements
- Python 3.8+
- pip or conda

### Dependencies

```bash
# Install packages
pip install numpy pandas matplotlib
```

### Verification

```bash
python --version
pip list | grep numpy
```

---

## 📝 Usage

### Run an Exercise

```bash
# Day 1, Exercise 1
python week_one/day_01/exercice_1/exo1.py

# Day 3, Exercise 1 (CSV manipulation)
python week_one/day_03/exercice_1/exo1_2.py

# Day 4, Exercise 1 (NumPy)
python week_one/day_04/exercice_1/exo1.py
```

---

## ✨ Features

- ✅ **Progressive**: From basic to advanced
- ✅ **Practical**: Hands-on exercises
- ✅ **Varied**: CSV, JSON, NumPy, statistics
- ✅ **Organized**: Clear structure by day/exercise
- ✅ **Realistic**: Real-world data manipulation

---

## 📊 Skills Summary

| Week | Day | Skill |
|------|-----|-------|
| 1 | 1 | Python Variables and Types |
| 1 | 2 | Data Structures |
| 1 | 3 | File Manipulation (CSV/JSON) |
| 1 | 4 | NumPy and Scientific Computing |

---

## 🎓 Notes

- Each exercise contains 1-4 files to complete
- Sample data is included in `day_03/exercice_1/data/`
- Complete exercises in the recommended order

---

## 💡 Tips

- Read the code comments
- Test your modifications immediately
- Use `print()` for debugging
- Consult official documentation when in doubt

---

## 📚 Resources

- [Python Documentation](https://docs.python.org/3/)
- [NumPy Docs](https://numpy.org/doc/)
- [CSV Module](https://docs.python.org/3/library/csv.html)
- [JSON Module](https://docs.python.org/3/library/json.html)

---

<div align="center">

### 🚀 Happy Learning! 🚀

**Created with ❤️ for data analysis education**

---

*Last updated: 2026*

**Author: Gaël RAMAHANDRISOA**

</div>
