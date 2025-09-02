from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# A simple in-memory structure to store tasks
tasks = []

@app.route('/', methods=['GET'])
def home():
    # Display existing tasks and a form to add a new task
    html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Todo List</title>
</head>
<body>
    <h1>Todo List</h1>
    <form action="/add" method="POST">
        <input type="text" name="task" placeholder="Enter a new task">
        <input type="submit" value="Add Task">
    </form>
    <ul>
        {% for task in tasks %}
        <li>{{ task }} <a href="/delete/{{ loop.index0 }}">x</a></li>
        {% endfor %}
    </ul>
</body>
</html>
'''
    return render_template_string(html, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    # Add a new task from the form data
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return home()

@app.route('/delete/<int:index>', methods=['GET'])
def delete_task(index):
    # Delete a task based on its index
    if index < len(tasks):
        tasks.pop(index)
    return home()



import tensorflow as tf
from pytorch_tabnet.tab_model import TabNetClassifier
import joblib

#from flask_cors import CORS


# Load model and scaler
#model = joblib.load('random_forest_model.joblib')
#scaler = joblib.load('scaler.joblib')

model = tf.keras.models.load_model('ncd_models/hypertension/deep-model1.keras')
scaler = joblib.load('ncd_models/hypertension/deep-scaler.joblib')
csv_name = "ncd_models/hypertension/c2.csv"

model2 = tf.keras.models.load_model('ncd_models/arthritis/deep-model1.keras')
scaler2 = joblib.load('ncd_models/arthritis/deep-scaler.joblib')
csv_name2 = "ncd_models/arthritis/selected.csv"

model3 = tf.keras.models.load_model('ncd_models/lung_cancer/deep-model1.keras')
scaler3 = joblib.load('ncd_models/lung_cancer/deep-scaler.joblib')
csv_name3 = "ncd_models/lung_cancer/selected.csv"

model4 = TabNetClassifier()
model4.load_model('ncd_models/asthma/tabnet_asthma_model.zip')
scaler4 = joblib.load('ncd_models/asthma/tabnet_scaler.joblib')
csv_name4 = "ncd_models/asthma/selected.csv"

model5 = TabNetClassifier()
model5.load_model('ncd_models/diabetes/tabnet-model1.keras.zip')
#model5 = tf.keras.models.load_model('ncd_models/diabetes/deep-model1.keras')
scaler5 = joblib.load('ncd_models/diabetes/deep-scaler.joblib')
csv_name5 = "ncd_models/diabetes/selected.csv"





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
