"""
This module starts the application
"""

from flask import Flask

APP = Flask(__name__)

from app import routes
