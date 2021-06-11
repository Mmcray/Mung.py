import file_loader as fl
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import plotly.express as px
import pandas as pd
import file_loader as fl
from file_loader import read_file

app = dash.Dash(__name__)


def main():
    df = read_file()
    print('step1: Info')
    fl.data_info()
    print('step2: Clean Columns')
    df_rc = fl.drop_cols()
    print('step3: Clean Nulls')
    df_rnc = fl.clean_nulls(df_rc)
    return df_rnc


dfg = main()
print(dfg.head())

figU = px.bar(
    dfg.nunique(axis=0), x=dfg.columns, y=dfg.nunique(axis=0),
    text=dfg.nunique(axis=0), title='Count of Uniques', )

figN = px.bar(
            dfg.nunique(axis=0), x=dfg.columns, y=dfg.isna().sum(),
            text=dfg.isna().sum(), title='Count of Nulls', )

app.layout = html.Div(
    [
        dcc.Graph(figure=figU),
        dcc.Graph(figure=figN),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i}
                     for i in dfg.columns],
            data=dfg.to_dict('records'),
            page_size=10,
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="paleturquoise"),
            style_data=dict(backgroundColor="lavender")
        ),
    ]
)

app.run_server(debug=False)

if __name__ == "__main__":
    print('This is Main')
