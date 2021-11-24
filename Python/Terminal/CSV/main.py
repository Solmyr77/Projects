import pandas as pd

data = pd.read_csv('TRC01.csv')

print(round(data['Amps'].mean(), 5))

#Notepad++
#Ctrl+H
#Find what:          .*?,(.*)
#Replace with:       \1
#Wrap around:        checked
#Regular expression: selected
#. matches newline:  unchecked
#Alt+A
