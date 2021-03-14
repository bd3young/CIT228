import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly import offline

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
used = [376, 348, 153, 104, 19]
wedgeColors=('green','blue','yellow','orange', 'purple')

fig = go.Figure(data=[go.Pie(labels=labels, values=used)])
fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=20, 
    marker=dict(colors=wedgeColors,line=dict(color='black',width=2))
    )
fig.update_layout(
    title_text="Popular Image Files",
    title_font_color="darkgreen", 
    title_font_size=30, 
    title_font_family="Raleway", 
    title_xref="paper", 
    title_yref="paper",
    margin_l=200,
    margin_r=200
    )
fig.show()