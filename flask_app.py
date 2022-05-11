import flask
from flask import Flask, request
from hackathon_script import get_pdf_id, scrape_url

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def get_url():
    if 'keyword' in request.args:
        keyword = str(request.args['keyword'])
    else:
        return "Error: No keyword provided. Please specify a keyword."

    id = get_pdf_id(keyword)
    url = scrape_url(id)

    return url

app.run()