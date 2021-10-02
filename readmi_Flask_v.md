Flask Startup Guide to view top news

install library::

    from flask import Flask, render_template
    
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

we get data from the repository and read::

    with open('hot_news_uk112.json', 'r') as myfile:
        data = myfile.read()
    
    
Using the decorator, we serve for our ""localhost""::

    @app.route("/")
    def index():
        return render_template(data)
    
    
    if __name__ == '__main__':
        app.run( port=8000, debug=True)