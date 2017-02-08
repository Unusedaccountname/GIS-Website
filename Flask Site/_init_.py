from flask import Flask, render_template
#this is what is needed for the app

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")
    





if __name__ == "__main__":
    app.run(debug=True)
