import openai
from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<string:input>')

def chatgpt(input):
    openai.api_key = "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"
    message = "what's the decay time of {} in proper room temperature, character limit is 15, so be specific ".format(input)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    string = response.choices[0].text
    result = {
        "Input" : input,
        "output" : string

    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)