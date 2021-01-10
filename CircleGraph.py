import numpy as np
import matplotlib.pyplot as plt
from flask import make_response, Blueprint
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import file


app = Blueprint('app_module', __name__)


# 円グラフを描画
@app.route("/graph.png")
def func():

    All_index = len(file.Neu_list)
    Neu_count = 0
    Pos_count = 0
    Neg_count = 0
    Pos_list = file.Pos_list
    Neu_list = file.Neu_list
    Neg_list = file.Neg_list

    # それぞれのパーセンテージ計算
    for index in range(All_index):
        if Neu_list[index] > Pos_list[index] and Neu_list[index] > Neg_list[index]:
            Neu_count += 1
        elif Pos_list[index] > Neu_list[index] and Pos_list[index] > Neg_list[index]:
            Pos_count += 1
        elif Neg_list[index] > Neu_list[index] and Neg_list[index] > Pos_list[index]:
            Neg_count += 1

    Neu_per = Neu_count / All_index
    Pos_per = Pos_count / All_index
    Neg_per = Neg_count / All_index

    # グラフのimg化
    x = np.array([Pos_per, Neu_per, Neg_per])
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

