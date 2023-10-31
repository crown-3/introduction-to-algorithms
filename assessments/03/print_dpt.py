import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def save_dp_table_as_image(arr, dp_table, filename="dp_table.png"):
    # If the file already exists, delete it
    if os.path.exists(filename):
        os.remove(filename)

    # Convert the DP table to a DataFrame for visualization
    df = pd.DataFrame(dp_table)

    # Set column and row names for the DataFrame
    max_sum = sum([x for x in arr if x > 0])
    min_sum = sum([x for x in arr if x < 0])
    df.columns = list(range(min_sum, max_sum + 2))
    df.index = ["-"] + arr  # Include all numbers in the array for the row labels

    # Plot the heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df, cmap="Blues", cbar=False, annot=True, fmt="d")
    plt.title("Dynamic Programming Table")
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()


