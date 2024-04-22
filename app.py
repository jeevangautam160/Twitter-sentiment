import flask
from flask import Flask,  render_template , request
import joblib

# Load the sentiment analysis model
model = joblib.load("trainedModel.sav")

# Create a Flask app
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return render_template("index.html")
def analyze_sentiment(text):
    # Perform sentiment analysis on the input text
    # This function should include your logic for analyzing sentiment using your model
    # Replace this placeholder code with your actual sentiment analysis code
    if "happy" in text.lower():
        return "Positive"
    else:
        return "Negative"

# Define the route for sentiment analysis
@app.route("/analyze", methods=["POST"])
def analyze():
    # Get the text data from the form
    text = request.form["text"]
    
    # Perform sentiment analysis using the model
    sentiment = analyze_sentiment(text)
    
    # Render the result template with the sentiment analysis result
    return render_template("result.html", text=text, sentiment=sentiment)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
