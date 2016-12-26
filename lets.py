from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def he():
    return render_template('main.html')
@app.route("/name")
def hel():
    return render_template('name.html')
@app.route("/profile")
def hell():
    return render_template('profile.html')
@app.route("/blog")
def hello():
    return render_template('blog.html')
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run( port=5001, debug=True)
