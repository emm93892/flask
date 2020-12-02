from flask import Flask, request, render_template, Blueprint
import CircleGraph

app = Flask(__name__)

app.register_blueprint(CircleGraph.app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/surveyed')
def surveyed():
    return render_template('surveyed.html')


@app.route('/mypage')
def mypage():
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run(debug=True)
