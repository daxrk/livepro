from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load data from JSON file
with open('lawsociety_data.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = articles[article_id]
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True)
