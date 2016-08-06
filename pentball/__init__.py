# -*- encoding: utf8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def Application():
    app = Flask(__name__)

    dev_cfg = os.path.abspath(os.path.join(
        os.path.basename(__file__), '../dev.cfg'))
    app.config.from_pyfile(dev_cfg)

    if 'ONLINE_CFG' in os.environ:
        app.config.from_envvar('ONLINE_CFG', silent=True)

    db.init_app(app)

    return app


app = Application()
