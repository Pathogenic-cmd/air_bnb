import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def summarize_numeric_distributions(df, log_transform=False, exclude_zeros=False):
    numeric_cols = df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        print(f"\n📊 Summary for '{col}':")
        if exclude_zeros:
            data = df[df[col] > 0][col]
        else:
            data = df[col].dropna()

        print(data.describe())
        print(f"Skewness: {data.skew():.2f}")

        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        sns.histplot(data, kde=True, bins=50)
        plt.title(f"Histogram of {col}")

        plt.subplot(1, 2, 2)
        sns.boxplot(x=data)
        plt.title(f"Boxplot of {col}")
        plt.show()

        if log_transform and (data > 0).all():
            log_data = np.log(data)
            print(f"🔁 Log-transformed summary for '{col}':")
            print(log_data.describe())
            plt.figure(figsize=(12, 4))
            sns.histplot(log_data, kde=True, bins=50, color='green')
            plt.title(f"Log-Transformed Histogram of {col}")
            plt.show()









def save_num_distributions(df, column, save=False, prefix="plot"):
    # Drop missing and zero values for log
    data = df[column].dropna()
    log_data = np.log(data[data > 0])

    # Histogram
    plt.figure(figsize=(10, 4))
    sns.histplot(data, kde=True, bins=50)
    plt.title(f"{column} Distribution")
    if save:
        plt.savefig(f"{prefix}_{column}_hist.png", bbox_inches='tight')
    plt.show()

    # Boxplot
    plt.figure(figsize=(10, 2))
    sns.boxplot(x=data)
    plt.title(f"{column} Boxplot")
    if save:
        plt.savefig(f"{prefix}_{column}_box.png", bbox_inches='tight')
    plt.show()

    # Log histogram
    plt.figure(figsize=(10, 4))
    sns.histplot(log_data, kde=True, bins=50)
    plt.title(f"Log-{column} Distribution")
    if save:
        plt.savefig(f"{prefix}_log_{column}_hist.png", bbox_inches='tight')
    plt.show()

    # Log boxplot
    plt.figure(figsize=(10, 2))
    sns.boxplot(x=log_data)
    plt.title(f"Log-{column} Boxplot")
    if save:
        plt.savefig(f"{prefix}_log_{column}_box.png", bbox_inches='tight')
    plt.show()



def classify_price(price):
    if price < 50:
        return 'Budget'
    elif 50 <= price < 100:
        return 'Low-mid'
    elif 100 <= price < 200:
        return 'Mid-range'
    elif 200 <= price < 500:
        return 'Premium'
    else:
        return 'Luxury'




def get_price_quantiles(df):
    """Compute price quantiles for a given DataFrame."""
    return df['price'].quantile([0.25, 0.5, 0.75])

def classify_by_quantile(price, quantiles):
    """Classify price into budget categories based on quantiles."""
    if price < quantiles[0.25]:
        return 'Budget'
    elif price < quantiles[0.5]:
        return 'Low-mid'
    elif price < quantiles[0.75]:
        return 'Mid-range'
    else:
        return 'Premium'
