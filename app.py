from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/set-background/<mode>')
def set_background(mode):
    session['mode'] = mode
    return render_template('home.html')# redirect(url_for('/'))

@app.route('/', methods=['GET'])
def my_route_page_function():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run(debug=True)
