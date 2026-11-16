import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    imports
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt

    return mo, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    data
    """)
    return


@app.cell
def _(mo, pd):
    df = pd.read_csv(mo.notebook_dir() / ".." / "data" / "features" / "events.csv")
    df.head()
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    plot
    """)
    return


@app.cell
def _(df, plt):
    fig, ax = plt.subplots()
    ax.hist(df["duration_minutes"], bins=30)
    ax.set_title("Distribution of event durations")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of events")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
