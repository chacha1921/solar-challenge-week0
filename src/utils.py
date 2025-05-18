# src/utils.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

sns.set(style="whitegrid")

def load_dataset(path, parse_dates=["Timestamp"]):
    return pd.read_csv(path, parse_dates=parse_dates)

def generate_missing_value_report(df, threshold=5):
    missing = df.isna().sum()
    missing_percent = (missing / len(df)) * 100
    report = pd.DataFrame({"Missing": missing, "Percent": missing_percent})
    return report[report["Percent"] > threshold]

def detect_outliers_zscore(df, cols, threshold=3):
    z_scores = df[cols].apply(zscore)
    outliers = (np.abs(z_scores) > threshold)
    return outliers.sum()

def impute_median(df, cols):
    df_cleaned = df.copy()
    for col in cols:
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
    return df_cleaned

def plot_time_series(df, cols, title="Time Series Plot"):
    df.set_index("Timestamp")[cols].plot(subplots=True, figsize=(15, 10))
    plt.suptitle(title)
    plt.show()

def plot_bar_grouped_means(df, group_col, value_cols, labels, title):
    grouped = df.groupby(group_col)[value_cols].mean().reset_index()
    grouped.plot(x=group_col, kind="bar", figsize=(8, 5), title=title)
    plt.ylabel("W/m²")
    plt.xticks(ticks=[0, 1], labels=labels, rotation=0)
    plt.show()

def plot_corr_heatmap(df, cols):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

def plot_pairplot(df, x_vars, y_var, title):
    sns.pairplot(df, vars=x_vars, y_vars=[y_var], height=4)
    plt.suptitle(title, y=1.02)
    plt.show()

def plot_scatter(df, x, y, hue=None, title="Scatter Plot"):
    sns.scatterplot(data=df, x=x, y=y, hue=hue, palette="coolwarm")
    plt.title(title)
    plt.show()

def plot_histograms(df, cols, bins=30):
    for col in cols:
        df[col].hist(bins=bins, alpha=0.7, label=col)
    plt.legend()
    plt.title("Histogram")
    plt.show()

def plot_bubble(df, x, y, size_col, color="orange", title="Bubble Chart"):
    plt.figure(figsize=(10,6))
    plt.scatter(df[x], df[y], s=df[size_col], alpha=0.5, c=color, edgecolors="black")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.grid(True)
    plt.show()
