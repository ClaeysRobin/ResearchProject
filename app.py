from flask import *
import VQGAN


app = Flask(__name__)


@app.route("/")
def  HomePage():
    # shows the index.html file in the templates folder
    return render_template("Index.html")

@app.route("/runscript/<InputText>", methods=['GET'])
def ScriptPage(InputText):
    # VQGAN.run_model(username)
    print(InputText)
    return redirect(url_for("HomePage"))


if __name__ == "__main__":
    app.run(debug=True)