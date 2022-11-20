from flask import Flask, Blueprint, render_template
from website.views import website

import logging

server = Flask(__name__)
server.register_blueprint(website)

if __name__ == "__main__":
    logging.basicConfig(filename='Logs/activity.log')
    server.run(debug=True)