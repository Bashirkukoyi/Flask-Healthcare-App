from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Set up MongoDB connection
client = MongoClient('localhost', 27017)
db = client['survey_db']
collection = db['responses']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'age': request.form['age'],
        'gender': request.form['gender'],
        'total_income': request.form['total_income'],
        'expenses': {
            'utilities': request.form.get('utilities', '0'),
            'entertainment': request.form.get('entertainment', '0'),
            'school_fees': request.form.get('school_fees', '0'),
            'shopping': request.form.get('shopping', '0'),
            'healthcare': request.form.get('healthcare', '0')
        }
    }
    collection.insert_one(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
