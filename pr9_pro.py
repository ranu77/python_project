
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ITEMS = ['Open/Generate', 'Snapshot', 'Fix data', 'Numbers', 'Plot room', 'Stop']

class AirqualityTool:
    def __init__(self):
        self.df = pd.DataFrame()

    def quickstats(self, path):
        if not os.path.exists(path):
            d=pd.date_range("2023-03-01", periods=150, freq="D")
            tmp=pd.DataFrame({
                "date":d,
                "city":np.random.choice(["Alpha","Beta","Gamma","Delta"], len(d)),
                "AQI":np.random.randint(35,320,len(d)),
                "PM25":np.random.uniform(5,180,len(d)),
                "PM10":np.random.uniform(10,230,len(d)),
                "Temp":np.random.uniform(10,40,len(d))
            })
            tmp.to_csv(path,index=False)
        parse_cols = []
        if os.path.exists(path):
            cols = list(pd.read_csv(path, nrows=0).columns)
            if "date" in cols: parse_cols=["date"]
        self.df = pd.read_csv(path, parse_dates=parse_cols)
        if "date" in self.df.columns: self.df["date"] = pd.to_datetime(self.df["date"])

    def wash(self):
        if self.df.empty: 
            print("No data to show."); return
        print(self.df.head(3)); print(self.df.tail(3))
        print("Cols->", list(self.df.columns))
        print(self.df.dtypes)

    def loadit(self):
        if self.df.empty: return
        for c in self.df.columns:
            if self.df[c].dtype.kind in "biufc": self.df[c].fillna(self.df[c].median(), inplace=True)
            else: self.df[c].fillna("Unknown", inplace=True)

    def drawit(self):
        if self.df.empty: return
        print("AQI std:", round(float(self.df["AQI"].std()),2))

    def look(self):
        if self.df.empty: return
        plt.figure(); self.df.groupby("city")[["PM25","PM10"]].mean().plot(kind="bar"); plt.title("BAR view"); plt.tight_layout(); plt.savefig("airquality_02_bar.png"); plt.close()
        plt.figure(); self.df.groupby(self.df["date"].dt.to_period("W"))["AQI"].mean().plot(); plt.ylabel("AQI weekly avg"); plt.title("LINE view 2"); plt.tight_layout(); plt.savefig("airquality_02_line.png"); plt.close()

def build_map(app):
    return {"1": lambda: app.quickstats(input("Path (blank -> sample): ") or "airquality.csv"),
            "2": app.wash,
            "3": lambda: (app.loadit(), print("tidied")),
            "4": app.drawit,
            "5": lambda: (app.look(), print("saved images"))}

def main():
    app = AirqualityTool()
    actions = build_map(app)
    while True:
        print("\nMini Studio >> " + " | ".join([f"{i+1}:{it}" for i,it in enumerate(ITEMS)]))
        pick = input("choose: ").strip()
        if pick == "6": print("closing."); break
        action = actions.get(pick)
        action() if action else print("invalid")

if __name__ == "__main__":
    main()
