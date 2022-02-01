import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Square', 'Amps']

df = pd.read_csv('TRC01.csv', names=headers)

df.set_index('Square').plot()

plt.show()