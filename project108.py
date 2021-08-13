import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("project.csv")

graph = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist = False)
graph.show()