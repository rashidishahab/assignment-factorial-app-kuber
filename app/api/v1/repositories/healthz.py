# -*- coding: UTF-8 -*-
from flask import jsonify


def ms_health_check():
    return jsonify({"success": True})
