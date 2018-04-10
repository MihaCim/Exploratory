# import libraries
import pandas as pd
import numpy as np

# plotting
import matplotlib.pyplot as plt

# Data is loaded in df. dataDir tell us folder of file.
dataDir = "../Data/Reims/"
df = pd.read_csv(dataDir + "170830-noheader.csv")

# Data in list are unuseful so we can delete them. ALso data from CH21 to CH40 are unuseful.

list_unused = ["Logic", "Alarm1-10", "Alarm11-20", "Alarm21-30", "Alarm31-40", "AlarmLP", "AlarmOut"]

for element in list_unused:
    df.drop(element, 1, inplace=True)
    
for i in range(21, 41):
    df.drop("CH" + str(i), 1, inplace=True)

# In firs line we have units. We can delete them. 
df.drop(0, 0, inplace=True)