from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        user1 = replacer(user)
        return redirect(url_for("user", usr=user1))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

def replacer(istring):
    for r in (("Oracle", "Oracle©"), ("Google", "Google©"), ("Microsoft","Microsoft©"),("Amazon","Amazon©"),("Deloitte","Deloitte©"),("oracle", "Oracle©"), ("google", "Google©"), ("microsoft","Microsoft©"),("amazon","Amazon©"),("deloitte","Deloitte©")):
        istring = istring.replace(*r)
    return(istring)

if __name__ == "__main__":
    app.run(debug=True)




