from collections import deque
import csv
import matplotlib.pyplot as plt


maxlen = 20
window = deque(maxlen=maxlen)

with open('TRC01.csv') as f_input:
    csv_input = csv.reader(f_input, skipinitialspace=True)
    header = next(csv_input)

    freq = []
    x = []

    for Square, Amps in csv_input:
        Square = float(Square)
        window.append(Square)

        if len(window) == maxlen:
            x.append(Square)
            freq.append(maxlen / ((window[-1] - window[0])))

    plt.plot(x, freq)
    plt.show()