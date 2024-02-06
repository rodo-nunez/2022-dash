import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from src.components import ids

MEDAL_DATA = px.data.medals_long()

def render(app: Dash) -> html.Div:
    
    fig = px.bar(MEDAL_DATA, x="medal", y="count", color="nation", text="nation")
    return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
