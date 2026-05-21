import os
import sys

sys.path.append(os.getcwd())

from flask import Flask
from backend.routes_extra import extra_bp

app = Flask(__name__)
app.register_blueprint(extra_bp)

with app.test_client() as client:
    print("Calling /api/classes...")
    res = client.get('/api/classes')
    print(f"Status: {res.status_code}")
    print(f"Data: {res.get_data(as_text=True)}")
