from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_route_page_function():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run(debug=True)
