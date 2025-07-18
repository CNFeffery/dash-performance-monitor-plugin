import dash
from dash import html

# Import the performance monitor plugin
from dash_performance_monitor_plugin import setup_performance_monitor_plugin

# Enable the performance monitor plugin for the current app
setup_performance_monitor_plugin()

app = dash.Dash(__name__)

app.layout = html.Div("Test App.", style={"padding": 50})

if __name__ == "__main__":
    app.run(debug=True)
