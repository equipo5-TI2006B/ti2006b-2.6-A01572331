"""Activity 2 - VS Code Python Workbench: quick environment check."""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Interpreter: {sys.executable}")
    print(f"pandas: {pd.__version__} | matplotlib: {matplotlib.__version__}")

    df = pd.DataFrame(
        {"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
         "sales": [120, 135, 150, 145, 170, 190]}
    )
    print(df.describe())

    out = Path("outputs")
    out.mkdir(exist_ok=True)
    ax = df.plot(x="month", y="sales", marker="o", legend=False, title="Sales by month")
    ax.set_ylabel("Sales")
    plt.tight_layout()
    plt.savefig(out / "sales.png")
    print("Workbench environment is ready - chart saved to outputs/sales.png")


if __name__ == "__main__":
    main()
