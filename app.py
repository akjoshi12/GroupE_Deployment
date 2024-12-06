from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return redirect(url_for('visualize', filename=file.filename))

@app.route('/visualize/<filename>')
def visualize(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(file_path)

    # Example visualization: Plotting the first two numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) >= 2:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[numeric_columns[0]], df[numeric_columns[1]], alpha=0.5)
        plt.title(f"{numeric_columns[0]} vs {numeric_columns[1]}")
        plt.xlabel(numeric_columns[0])
        plt.ylabel(numeric_columns[1])

        # Save the plot to a BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

        return render_template('visualize.html', image=image_base64, columns=numeric_columns)
    else:
        return "Not enough numeric columns to generate a plot."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
