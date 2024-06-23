import csv
from pymongo import MongoClient

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    def to_dict(self):
        return {
            'age': self.age,
            'gender': self.gender,
            'total_income': self.total_income,
            'utilities': self.expenses['utilities'],
            'entertainment': self.expenses['entertainment'],
            'school_fees': self.expenses['school_fees'],
            'shopping': self.expenses['shopping'],
            'healthcare': self.expenses['healthcare']
        }

def fetch_data_from_mongodb():
    client = MongoClient('localhost', 27017)
    db = client['survey_db']
    collection = db['responses']
    data = collection.find()
    return data

def save_to_csv(data, filename):
    fieldnames = ['age', 'gender', 'total_income', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            user = User(
                age=entry['age'],
                gender=entry['gender'],
                total_income=entry['total_income'],
                expenses=entry['expenses']
            )
            writer.writerow(user.to_dict())

if __name__ == '__main__':
    data = fetch_data_from_mongodb()
    save_to_csv(data, 'survey_data.csv')
