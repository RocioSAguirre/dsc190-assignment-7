import pandas as pd
import os

df = pd.read_csv("data/transformed/events.csv")
WEEKDAY_CONVERSION = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}

df["duration_minutes"] = df["duration_seconds"]/60
df["weekday"] = pd.to_datetime(df["timestamp"]).dt.weekday.map(WEEKDAY_CONVERSION)

os.makedirs("data/features/", exist_ok=True)
df.to_csv("data/features/events.csv", index=False)