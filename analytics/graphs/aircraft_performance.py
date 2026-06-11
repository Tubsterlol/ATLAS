import matplotlib.pyplot as plt
import pandas as pd


def plot_lift(csv_file: str):

    df = pd.read_csv(csv_file)

    plt.figure(figsize=(10, 5))

    plt.plot(df["time_s"], df["lift_n"])

    plt.xlabel("Time (s)")
    plt.ylabel("Lift (N)")
    plt.title("Aircraft Lift")

    plt.grid(True)

    plt.show()
