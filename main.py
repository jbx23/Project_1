from flask import Flask, render_template, request, session, redirect, url_for
# from flask_socketio import  SocketIO
app = Flask(__name__, template_folder="D:/CITS 3403/test", static_url_path="/static")
app.secret_key = "1234"

@app.route("/", methods=["GET", "POST"])
def cover():
    return render_template("cover.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    # Check if the session variable is set
        if request.method == 'POST':
            # Render the home page template
            return render_template('home.html')
        else:
            # Redirect to the cover page if the session variable is not set
            return redirect(url_for('cover'))
            
@app.route("/todo", methods=["GET", "POST"])
def todo():
    return render_template("todo.html")
@app.route("/GPAConverter", methods=["GET", "POST"])
def GPAConverter():
    return render_template("GPAConverter.html")
@app.route("/debtTracker", methods=["GET", "POST"])
def debtTracker():
    return render_template("debtTracker.html")
@app.route("/currencyConverter", methods=["GET", "POST"])
def currencyConverter():
    return render_template("currencyConverter.html")

if __name__ == "__main__":
    app.run(debug=True)