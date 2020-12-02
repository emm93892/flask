import numpy as np
import matplotlib.pyplot as plt
from flask import make_response, Blueprint
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io


app = Blueprint('app_module', __name__)


# 円グラフを描画
@app.route("/graph.png")
def func():
    x = np.array([10, 450, 800, 200, 100])
    fig1, ax1 = plt.subplots()
    ax1.pie(x)

    canvas = FigureCanvasAgg(fig1)
    buf = io.BytesIO()
    canvas.print_png(buf)
    data = buf.getvalue()

    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response
