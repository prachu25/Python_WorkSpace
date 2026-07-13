from flask import Flask   # import a flask lib..

# create a flask application
app =  Flask(__name__)

# Decorator
@app.route('/')   # home page url
def home():
    return 'Hello, Flask! '


if __name__ == '__main__':
    app.run(debug = True)

    

