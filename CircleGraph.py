import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, make_response, jsonify, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

# 円グラフを描画
def func():
    x = np.array([100, 200, 300, 400, 500])
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