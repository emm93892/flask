from flask import Flask, request, render_template
import CircleGraph

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph.png')
def graph():
    return CircleGraph.func()

@app.route('/surveyed')
def surveyed():
    return render_template('surveyed.html')

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

if __name__ == '__main__':
    app.run(debug=True)