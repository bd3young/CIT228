import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly import offline

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
ageRange=["Over 20","20-39","40-59","Over 60"]
barWidth = .25

fig = go.Figure()
fig.add_trace(go.Bar(
    x=ageRange,
    y=men,
    name='Men',
    marker_color='rgb(247, 7, 127)'
))
fig.add_trace(go.Bar(
    x=ageRange,
    y=women,
    name='Women',
    marker_color='rgb(7, 87, 247)'
))
fig.add_trace(go.Bar(
    x=ageRange,
    y=total,
    name='Total',
    marker_color='green'
))

layout = fig.update_layout(
    title='Fast Food Consumption Per Day',
    title_font_color='darkblue',
    title_font_size=30,
    xaxis=dict(
        title='Age Categorys',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='Percentages',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

#fig.show()
offline.plot({'data': fig, 'layout':layout}, filename='bar.html')





# labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
# used = [376, 348, 153, 104, 19]
# wedgeColors=('green','blue','yellow','orange', 'purple')

# fig = go.Figure(data=[go.Pie(labels=labels, values=used)])
# layout = fig.update_traces(
#     hoverinfo='label+percent',
#     textinfo='value',
#     textfont_size=20, 
#     marker=dict(colors=wedgeColors,line=dict(color='black',width=2))
#     )
# fig.update_layout(
#     title_text="Popular Image Files",
#     title_font_color="darkgreen", 
#     title_font_size=30, 
#     title_font_family="Raleway", 
#     title_xref="paper", 
#     title_yref="paper",
#     margin_l=200,
#     margin_r=200
#     )
# #fig.show()
# offline.plot({'data': fig, 'layout':layout}, filename='pie.html')