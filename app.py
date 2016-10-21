from flask import Flask, redirect
import giphypop

app = Flask(__name__)

g = giphypop.Giphy()

@app.route("/")
def hello():
    return """
<!DOCTYPE html>
<html>
<head>
<script type="text/javascript" src="http://www.cornify.com/js/cornify.js"></script>
</head>
<body onload="javascript:cornify_add()">>
<img src="%s">
</body>
</html>
""" % g.random_gif().media_url

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=80)
