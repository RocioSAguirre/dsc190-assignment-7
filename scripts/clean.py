import pandas as pd
import os

df = pd.read_csv("data/raw/events.csv", dtype=str)
VALID_EVENT_TYPES = ["click", "view", "purchase", "scroll", "login"]

#keep non missing field
df = df.dropna()

#keep valid event types
df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

#keep positive durations
df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df = df[df["duration_seconds"] > 0]

#normalize timestamps
df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed", errors="coerce")
df = df.dropna(subset=["timestamp"])
df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

#convert to whole number
df["duration_seconds"] = df["duration_seconds"].astype(int)

#save cleaned data
os.makedirs("data/clean", exist_ok=True)
df.to_csv("data/clean/events.csv", index=False)