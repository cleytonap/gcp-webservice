from flask import Flask, render_template


app=Flask(__name__)
print(__name__)

@app.route('/')
def home():
    # return "Hello World, Flask 2!"
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


# Start script
if __name__ == "__main__":
    app.run(debug=True)