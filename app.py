import dash
import dash_auth

from config import config as cfg

app = None
auth = None
if cfg["auth"]["required"]:
    app = dash.Dash("auth")
    auth = dash_auth.BasicAuth(app, cfg["auth"]["validPairs"])
else:
    app = dash.Dash()

server = app.server
app.config.suppress_callback_exceptions = True
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})