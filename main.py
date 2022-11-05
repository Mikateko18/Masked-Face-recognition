from flask import  Flask
from app import views
import matplotlib.pyplot as plt

app = Flask(__name__)
app.add_url_rule(rule='/',endpoint='home',view_func=views.faceApp)
app.add_url_rule(rule='/faceApp/',
                 endpoint='faceApp',
                 view_func=views.faceApp,
                 methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True)

