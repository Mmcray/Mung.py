import file_loader as fl
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import plotly.express as px
import pandas as pd
import file_loader as fl

app = dash.Dash(__name__)

munging = fl.Mung(fl.read_file)
munging.data_info()
munging.clean_nulls()
munging.drop_cols()
df = munging.df

figU = px.bar(
    df.nunique(axis=0), x=df.columns, y=df.nunique(axis=0),
    text=df.nunique(axis=0), title='Count of Uniques', )

figN = px.bar(
    df.nunique(axis=0), x=df.columns, y=df.isna().sum(),
    text=df.isna().sum(), title='Count of Nulls', )

app.layout = html.Div(
    [
        dcc.Graph(figure=figU),
        dcc.Graph(figure=figN),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i}
                     for i in df.columns],
            data=df.to_dict('records'),
            page_size=10,
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender")
        ),
    ]
)

app.run_server(debug=True)

if __name__ == "__main__":
    munging
