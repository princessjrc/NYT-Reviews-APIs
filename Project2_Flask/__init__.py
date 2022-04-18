from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "lsigjwe458aerjnor3r59"

from Project2_Flask import routes