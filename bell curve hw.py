import pandas as pd
import plotly.express as px
import math
import csv
import plotly.figure_factory as ff
import statistics
df=pd.read_csv(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\bell curve hw.csv")
mb=df["Mobile Brand"].tolist()
avgrating=df["Avg Rating"].tolist()

fig=ff.create_distplot([avgrating],["Avg Rating"],show_hist=False)
fig.show()