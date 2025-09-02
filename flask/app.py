from flask import Flask, request, jsonify
from flask_cors import CORS

from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import tensorflow as tf
from pytorch_tabnet.tab_model import TabNetClassifier


# ---------------- App Setup ----------------
app = Flask(__name__)
CORS(app)  # replaces FastAPI CORS middleware




   

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
























