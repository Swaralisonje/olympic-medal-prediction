from flask import Flask, render_template, request
import pickle
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go



app = Flask(__name__)

# Load trained model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load classification report
with open("classification_report.txt", "r") as f:
    class_report = f.read()

# Load dataset
df = pd.read_csv("processed_medal_predictions.csv")


def generate_prediction_graph(top_countries, sport_name):
    """Generates a bar chart for predicted medal-winning percentages."""
    graph_path = "static/prediction_graph.png"

    plt.figure(figsize=(8, 5))
    plt.barh(top_countries['Country'], top_countries['Predicted_Percentage'], color='skyblue')

    plt.xlabel("Predicted Medal Percentage")
    plt.ylabel("Country")
    plt.title(f"Top 10 Countries for {sport_name.capitalize()}")

    # Adding data labels
    for index, value in enumerate(top_countries['Predicted_Percentage']):
        plt.text(value, index, f"{value:.2f}%", va='center', fontsize=10)

    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(graph_path)
    plt.close()

    return graph_path


def generate_world_map(top_countries):
    """Generates a world map visualization of predicted medal percentages."""
    fig = go.Figure(data=go.Choropleth(
        locations=top_countries['Country'],  # Country names
        locationmode='country names',
        z=top_countries['Predicted_Percentage'],  # Color scale based on percentage
        colorscale='Blues',
        marker_line_color='darkgray',
        marker_line_width=0.5,
    ))

    fig.update_layout(title_text="Predicted Medal Percentages by Country",
                      geo=dict(showcoastlines=True))

    return fig.to_html(full_html=False)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sport_name = request.form["sport_name"].strip().lower()
        sport_code = df[df['Sport'].str.lower() == sport_name]['Sport_Code'].values

        if len(sport_code) == 0:
            return render_template("index.html", error="Sport not found! Please check the spelling.")

        sport_code = sport_code[0]
        sport_data = df[df['Sport_Code'] == sport_code][['Country', 'Total_Country_Medals']].copy()
        sport_data['Sport_Code'] = sport_code

        # Make predictions
        sport_data['Predicted_Percentage'] = model.predict(sport_data[['Sport_Code', 'Total_Country_Medals']])
        sport_data['Predicted_Percentage'] = sport_data['Predicted_Percentage'].clip(0, 100).round(2)

        top_countries = sport_data.sort_values(by='Predicted_Percentage', ascending=False).head(10)

        # Generate graphs
        prediction_graph = generate_prediction_graph(top_countries, sport_name)

        world_map = generate_world_map(top_countries)

        return render_template("result.html",
                               sport=sport_name.capitalize(),
                               countries=top_countries.to_dict(orient='records'),
                               classification_report=class_report,
                               prediction_graph=prediction_graph,
                               world_map=world_map,
                               timestamp=time.time())

    return render_template("index.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
