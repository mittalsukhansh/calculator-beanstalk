from flask import Flask, jsonify
import os

application = Flask(__name__)


@application.route('/')
def hello():
    return 'Hello AWS Beanstalk - version:0.0.5'


@application.route('/health')
def health():
    return jsonify(status="healthy")


@application.route('/info')
def info():
    return jsonify({
        "environment": os.getenv("APP_ENV", "local"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "debug": os.getenv("DEBUG", "false")
    })
