from flask import  Flask
from app import views
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder='templates')


app.add_url_rule('/', 'faceApp',views.faceApp, methods=['GET','POST'])
if __name__ == "__main__":
    app.run(debug=True)
