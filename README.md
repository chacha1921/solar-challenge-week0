# Solar Challenge Week 0

This repository contains the setup and solution for **Week 0 of the Solar Challenge**. It includes:

- A Python virtual environment  
- Clean, modular code with reusable utility functions  
- Solar dataset analysis and visualization  
- GitHub Actions workflow for continuous integration

---

## 📁 Project Structure

```
solar-challenge-week0/
│
├── data/                  
│   ├── benin-malanville.csv
│   ├── sierraleone-bumbuna.csv
│   └── togo-dapaong_qc.csv
│
├── notebooks/               
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   └── togo_eda.ipynb
│
├── src/                     
│   └── utils.py
│
├── .github/workflows/       # GitHub Actions CI workflow
│   └── ci.yml
│
├── requirements.txt         # Project dependencies
├── README.md                # Project overview and instructions
└── venv/                    # Virtual environment (excluded in .gitignore)
```

---

## Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/chacha1921/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # On Linux/macOS
venv\Scripts\activate            # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Use

1. Open any Jupyter notebook from the `notebooks/` folder.
2. Each notebook (e.g., `benin_eda.ipynb`) imports utility functions from `src/utils.py`.
3. All common preprocessing and plotting logic is modularized to improve readability and reuse.

---

## Reusable Functions (`src/utils.py`)

Key reusable components include:

- `load_dataset(path)`  
  Loads a CSV file and parses the timestamp.

- `generate_missing_value_report(df)`  
  Returns a DataFrame showing missing value counts and percentages.

- `detect_outliers_zscore(df, cols, threshold=3)`  
  Detects outliers based on z-score method.

- `impute_median(df, cols)`  
  Replaces missing values in selected columns with the median.

- `plot_time_series(df, columns)`  
  Plots multiple columns as time series.

- `plot_correlation_heatmap(df, cols)`  
  Shows a heatmap of correlations among selected features.

- `plot_grouped_bars(df, group_col, value_cols, title)`  
  Useful for comparing sensor readings before/after cleaning.

- `plot_pairwise(df, x_vars, y_vars)`  
  Creates pair plots to visualize pairwise relationships.

- `plot_bubble(df, x, y, size_col)`  
  Bubble plot for RH vs Tamb with bubble size = RH.

---

## Notes

- Notebooks are organized per country (Benin, sierraeone, Togo).  
- The project emphasizes clean code, modular design, and EDA best practices.  
- Plots are generated using `matplotlib` and `seaborn`.  
- Cleaned data is saved under the `data/` folder.

---

## Contributors

- [@chacha1921](https://github.com/chacha1921)
