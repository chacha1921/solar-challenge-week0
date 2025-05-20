import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_country_data(countries):
    data_frames = []
    for country in countries:
        path = f"../data/{country.lower().replace(' ', '_')}_clean.csv"
        try:
            df = pd.read_csv(path, parse_dates=["Timestamp"])
            df["Country"] = country
            data_frames.append(df)
        except FileNotFoundError:
            pass
    return pd.concat(data_frames, ignore_index=True) if data_frames else pd.DataFrame()

def plot_metric_boxplot(df, metric):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x="Country", y=metric, palette="Set2")
    plt.title(f"{metric} Distribution Across Countries")
    plt.tight_layout()
    return plt.gcf()

def generate_summary_table(df):
    metrics = ["GHI", "DNI", "DHI"]
    summary = []
    for country in df["Country"].unique():
        country_df = df[df["Country"] == country]
        for metric in metrics:
            summary.append({
                "Country": country,
                "Metric": metric,
                "Mean": round(country_df[metric].mean(), 2),
                "Median": round(country_df[metric].median(), 2),
                "Std Dev": round(country_df[metric].std(), 2)
            })
    return pd.DataFrame(summary)

def plot_country_ranking(df, metric):
    avg_metric = df.groupby("Country")[metric].mean().sort_values(ascending=False)
    plt.figure(figsize=(6, 4))
    avg_metric.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.ylabel(f"Average {metric}")
    plt.title(f"Average {metric} by Country")
    plt.tight_layout()
    return plt.gcf()
