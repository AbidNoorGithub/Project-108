import pandas as pd
import plotly_express as px
import plotly.figure_factory as pff
import csv

dataFrame = pd.read_csv("Rating.csv")


figure = pff.create_distplot([dataFrame["Avg Rating"].tolist()], ["Result"])
figure.show()
