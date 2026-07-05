from app import create_app
from flask import render_template

app=create_app()

if __name__=="__main__":
    app.run(debug=True)


@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):

    return render_template(
        "errors/404.html"
    ),404


@app.errorhandler(403)
def forbidden(error):

    return render_template(
        "errors/403.html"
    ),403


@app.errorhandler(500)
def server_error(error):

    return render_template(
        "errors/500.html"
    ),500