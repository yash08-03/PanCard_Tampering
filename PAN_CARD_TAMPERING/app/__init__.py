import os
from flask import Flask

app = Flask(__name__)

# Fetch the environment from your terminal/system settings
# Default to 'production' if nothing is set
env = os.environ.get("FLASK_ENV", "production")

if env == "production":
    app.config.from_object("config.ProductionConfig")
elif env == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app import views
