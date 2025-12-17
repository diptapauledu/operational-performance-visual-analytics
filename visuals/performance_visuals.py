import matplotlib.pyplot as plt
import seaborn as sns

def generate_visuals(df):
    sns.set_style("whitegrid")

    # Cycle Time Bar Chart
    plt.figure()
    sns.barplot(x="process_id", y="cycle_time_minutes", data=df)
    plt.title("Cycle Time Comparison Across Processes")
    plt.xlabel("Process ID")
    plt.ylabel("Cycle Time (Minutes)")
    plt.show()

    # Defect Trend Line
    plt.figure()
    sns.lineplot(x="process_id", y="defects", data=df, marker="o")
    plt.title("Defect Trend Across Processes")
    plt.xlabel("Process ID")
    plt.ylabel("Number of Defects")
    plt.show()

    # Cost vs Defects Scatter
    plt.figure()
    sns.scatterplot(x="defects", y="cost_usd", data=df, s=100)
    plt.title("Cost Impact vs Defects")
    plt.xlabel("Defects")
    plt.ylabel("Cost (USD)")
    plt.show()
