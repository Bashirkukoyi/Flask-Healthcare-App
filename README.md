# README

## Project Setup Instructions

### Prerequisites
- Python
- Flask
- MongoDB
- pandas
- matplotlib

### Instructions
1. Clone the repository or unzip the project files.
2. Ensure MongoDB is running on localhost.
3. Run the Flask application:
   ```bash
   python app.py

Open a web browser and navigate to http://localhost:5000.
Submit survey data using the form.
To process the data and generate the CSV file:
python process_data.py

Open the Jupyter notebook and run the cells to generate visualizations.

Deploy the Flask app on AWS EC2 following standard deployment steps.
Deployment on AWS
Launch an EC2 instance.
Install Python, Flask, and MongoDB on the instance.
Transfer the project files to the EC2 instance.
Run the Flask application on the EC2 instance.
