import plotly.graph_objects as go
import pandas as pd
import numpy as np

import plotly.io as pio
pio.templates.default = "simple_white"
data = pd.read_csv(r"https://raw.githubusercontent.com/datageekrj/ForHostingFiles/master/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")



numOfRows = data.shape[0] # No of Countries
numOfCols = data.shape[1] # No of years + one column for a country
numOfFrames = numOfCols - 1
xaxis_range = [0,numOfFrames + 2]

# While, testing the code, test with low numbers:
# Initial State of the data
# First we are just seeing it for afghanistan

x_init = np.array([1])


initial_data = []
for cont_ind in [75,35,184,83,140]:
    y_axis = np.array(data.iloc[cont_ind,0])
    initial_data.append(go.Scatter(x =x_init, y = y_axis,mode = "lines",name = data.country[cont_ind]))
initial_max = 600

# Frames
frames = []
for f in range(1,numOfFrames+1):
    x_axis = np.arange(1,f+1)
    curr_data = []
    title_names = []
    start = "For " + str(1800 + f + 1)
    for cont_ind in [75,35,184,83,140]:
        curr_country = data.country[cont_ind]
        y_axis = np.array(data.iloc[cont_ind,1:f+1])
        curr_data.append(go.Scatter(x = x_axis, y = y_axis,mode = "lines", name = curr_country))
        title_names.append(curr_country + ": " + str(y_axis[f-1]/1000) + "K Dollar. ")
    title = start + " " + " ".join(title_names)
    curr_frame = go.Frame(data = curr_data, layout = {"title":title})
    frames.append(curr_frame)
 
figure = go.Figure(
    data = initial_data,
    layout = {
        "title":"Line Chart Race",
        "xaxis":{"range":xaxis_range, "visible":False, "showline":False},
        "yaxis":{"type":"log", "visible":False, "showline":False},
        "updatemenus":[{"type":"buttons","buttons":[{"method":"animate","label":"play", "args":[None]}]}]
        },
    frames = frames
    )
figure.show()
