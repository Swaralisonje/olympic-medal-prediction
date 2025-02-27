import matplotlib.pyplot as plt
import numpy as np

def generate_prediction_graph(top_countries, sport_name):
    """Generates a bar chart for predicted medal-winning percentages."""
    graph_path = "static/prediction_graph.png"
    plt.figure(figsize=(8, 5))
    plt.barh(top_countries['Country'], top_countries['Predicted_Percentage'], color='skyblue')
    plt.xlabel("Predicted Medal Percentage")
    plt.ylabel("Country")
    plt.title(f"Top 10 Countries for {sport_name.capitalize()}")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(graph_path)
    plt.close()
    return graph_path






