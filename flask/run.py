from flask import Flask
from configs.config import config_dict
import os
import sys

app = Flask(__name__)

get_config_mode = os.environ.get('CONFIG_MODE','Debug')

try:
    config_object = config_dict[get_config_mode.capitalize()]
except KeyError:
    sys.exit('Error: Invalid CONFIG_MODE env. variable')

app.config.from_object(config_object)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

if __name__ == "__main__":
    app.run(port=5001,debug=True,threaded=False)