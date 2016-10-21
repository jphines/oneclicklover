from flask import Flask, redirect
import giphypop

app = Flask(__name__)

g = giphypop.Giphy()

@app.route("/")
def hello():
    return redirect(g.random_gif().media_url, code=302)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=80)
