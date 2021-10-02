from flask import Flask, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# read file
with open('hot_news_uk112.json', 'r') as myfile:
    data = myfile.read()


@app.route("/")
def index():
    return render_template(data)


if __name__ == '__main__':
    app.run( port=8000, debug=True)