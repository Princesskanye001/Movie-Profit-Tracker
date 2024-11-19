from flask import Flask, render_template, request
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the transformed data
DATA_FILE = "profits.csv"
df = pd.read_csv(DATA_FILE)

@app.route("/")
def home():
    # Display the first 10 rows by default
    data = df.head(10).to_dict(orient="records")
    return render_template("index.html", data=data)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query", "")
    results = df[df['name'].str.contains(query, case=False)] if query else df
    data = results.head(10).to_dict(orient="records")
    return render_template("index.html", data=data, query=query)

if __name__ == "__main__":
    app.run(debug=True)
