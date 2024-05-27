# Exploratory Data Analysis of Adult Income Dataset

This project performs an Exploratory Data Analysis (EDA) on the Adult Income Dataset to uncover insights and patterns in the data. The goal is to understand the relationships between different features and the target variable, `income`.

## Dataset

The dataset contains 32,561 entries with the following columns:

| #  | Column           | Non-Null Count | Dtype  |
|----|------------------|----------------|--------|
| 0  | age              | 32561          | int64  |
| 1  | workclass        | 32561          | object |
| 2  | fnlwgt           | 32561          | int64  |
| 3  | education        | 32561          | object |
| 4  | educational-num  | 32561          | int64  |
| 5  | marital-status   | 32561          | object |
| 6  | occupation       | 32561          | object |
| 7  | relationship     | 32561          | object |
| 8  | race             | 32561          | object |
| 9  | gender           | 32561          | object |
| 10 | capital-gain     | 32561          | int64  |
| 11 | capital-loss     | 32561          | int64  |
| 12 | hours-per-week   | 32561          | int64  |
| 13 | native-country   | 32561          | object |
| 14 | income           | 32561          | object |

- **Total columns**: 15
- **Dtype distribution**: 6 columns of `int64`, 9 columns of `object`
- **Memory usage**: 3.7+ MB

## Prerequisites

To run this project, you will need:

- Python 3.6 or later
- Pandas
- NumPy
- Matplotlib
- Seaborn

You can install the required packages using:

1. Dependencies:

   ```bash
      pip install pandas numpy matplotlib seaborn
   ```

2. Clone the repository:
   ```bash
      git clone https://github.com/yourusername/adult-income-eda.git
      cd adult-income-eda
   ```
3. Load and preprocess the dataset:
   ```bash
      import pandas as pd

      # Load the dataset
      Data = pd.read_csv('adult.csv-Dataset/adult.data',header = None)
   ```

## Results
   The EDA reveals various insights into the data:

    - The age distribution shows a large number of individuals in the dataset are between 20 and 50 years old.
    - The income distribution indicates a class imbalance, with a higher number of individuals earning <=50K.
    - There are noticeable patterns between age and income, with higher age groups tending to have higher income.