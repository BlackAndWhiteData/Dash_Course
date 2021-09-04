from configs.config import config_dict
import os
import sys
from app import create_app

get_config_mode = os.environ.get('CONFIG_MODE','Debug')

try:
    config_object = config_dict[get_config_mode.capitalize()]
except KeyError:
    sys.exit('Error: Invalid CONFIG_MODE env. variable')

app = create_app(config_object)

if config_object.DEBUG:
    if __name__ == "__main__":
        app.run(port=5001,debug=True,threaded=False)