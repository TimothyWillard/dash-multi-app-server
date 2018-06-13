import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import importlib

from app import app
from config import config as cfg

apps_num = len(cfg["apps"])

apps_list = [None] * apps_num
for i in range(apps_num):
    apps_list[i] = importlib.import_module("apps."+cfg["apps"][i]["name"])

app.layout = html.Div([
    dcc.Location(id = "url", refresh = False),
    dcc.Link(
        children = html.H1(cfg["serverName"], style = {"textAlign": "center"}),
        href = "/"
    ),
    dcc.Link(
        children = html.H3(cfg["otherLinkName"], style = {
            "display": "block" if cfg["otherLinkName"] != None else "none",
            "textAlign": "center"
        }),
        href = cfg["otherLinkHref"]
    ),
    html.Hr(),
    html.Div(id = "page-content")
])

apps_link_list = [None] * apps_num
for i in range(apps_num):
    apps_link_list[i] = html.Li([
        dcc.Link(cfg["apps"][i]["title"], href = "/apps/"+cfg["apps"][i]["path"]),
        html.Span(" - "+cfg["apps"][i]["description"])
    ])

home_layout = html.Div([
    html.Ul(apps_link_list, style = {
        "listStyleType": "none"
    })
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if (pathname == "/") or (pathname == ""):
        return home_layout
    for i in range(len(cfg["apps"])):
        apps = cfg["apps"][i]
        if pathname == "/apps/"+apps["path"]:
            return apps_list[i].layout
    return html.H1("404 Error: Application Not Found")

if __name__ == '__main__':
    app.run_server(debug = cfg["debug"])