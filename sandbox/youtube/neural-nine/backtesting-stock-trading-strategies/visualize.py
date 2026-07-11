import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle("results.pickle")

df["portfolio_value"].plot()
plt.show()
