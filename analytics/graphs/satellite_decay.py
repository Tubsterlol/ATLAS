import pandas as pd
import matplotlib.pyplot as plt


def plot_altitude(
    csv_file: str
):

    df = pd.read_csv(
        csv_file
    )

    plt.figure(
        figsize=(10, 5)
    )

    plt.plot(
        df["time_s"],
        df["altitude_m"]
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title(
        "Satellite Altitude Decay"
    )

    plt.grid(True)

    plt.show()
