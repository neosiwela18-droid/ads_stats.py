import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\acer\Documents\MEGA\Programming\ASPIRE\Python\Economics\debt\nominal_gdp_usd_1960-2025.csv")


years = df.columns[1:]
japan = df.iloc[0,1:]
usa = df.iloc[1,1:]
china = df.iloc[2,1:]


plt.plot(years, japan, color="blue", label="Japan")
plt.plot(years, usa, color="green", label="United States")
plt.plot(years, china, color="red", label="China")

plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)
plt.title("Gross Domestic Product at Current Market Prices", fontweight="bold")
plt.xlabel("Years", fontweight="bold")
plt.ylabel("GDP", fontweight="bold")
plt.legend()
plt.tight_layout()
plt.show()

