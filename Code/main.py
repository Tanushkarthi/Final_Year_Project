# Use a pipeline as a high-level helper
from transformers import pipeline
from flask import Flask
from flask_cors import CORS

pipe = pipeline("text-classification", model="Hate-speech-CNERG/deoffxlmr-mono-tamil")

app = Flask(__name__)
CORS(app, resources={r"/find/*": {"origins": "*"}})


@app.route('/find/<comment>')
def find(comment):
    return pipe(comment)


if __name__ == '__main__':
    app.run()
