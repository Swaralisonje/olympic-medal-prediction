🏅 Olympic Medal Prediction

📌 Project Overview

This project is a machine learning-based web application that predicts the likelihood of a country winning medals in the Olympics for a given sport. Users can enter a sport name, and the app will display the top 10 countries with the highest predicted medal-winning percentage.

🚀 Features

User Input: Enter a sport name to get predictions.

Top 10 Country Predictions: Displays the top 10 countries with the highest predicted medal-winning percentage.

Graphical Visualization:

Bar Chart: Shows the medal-winning percentages for the top countries.

World Map: Highlights predicted medal percentages across countries.

Classification Report: Shows model performance.

Flask Web Application: Built using Flask for the backend and HTML, CSS for the frontend.

📁 Project Structure

/olympic-medal-prediction
│── app.py  # Flask application
│── rf_model.pkl  # Trained Random Forest model
│── processed_medal_predictions.csv  # Processed dataset
│── classification_report.txt  # Classification report
│── templates/
│   │── index.html  # Homepage (user input form)
│   │── result.html  # Displays predictions & visualizations
│── static/
│   │── style.css  # Styling for web pages
│   │── prediction_graph.png  # Generated bar chart
│── README.md  # Project documentation
│── requirements.txt  # Required dependencies

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/olympic-medal-prediction.git
cd olympic-medal-prediction

2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Flask Application

python app.py

Visit http://127.0.0.1:5000/ in your browser.

📊 Machine Learning Model

Algorithm Used: Random Forest Regressor

Features:

Sport_Code

Total_Country_Medals

Target Variable:

Medal_Percentage

Performance Metrics:

Mean Absolute Error (MAE)

R² Score

Classification Report (for binary classification at 50% threshold)

🖼️ Example Output

User Input: Swimming

Output:

Top 10 countries & medal-winning percentages

Bar chart visualization

World map visualization

Classification report

📜 License

This project is open-source and available under the MIT License.
