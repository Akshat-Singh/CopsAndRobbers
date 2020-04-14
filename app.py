import plotly.graph_objects as pgo
import networkx
from flask import Flask

app = Flask(__name__)

Graph = networkx.random_geometric_graph(50, 10)
figure = pgo.Figure()


def ender():
    return 0


figure.on_click(ender)


@app.route('/')
def begin():
    figure.show()
