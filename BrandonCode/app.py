from flask import Flask, request, render_template
from deeppavlov import build_model, configs
model = build_model(configs.squad.squad, download=True)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing():
    return 'This is the NLP Project 3 API service.'


@app.route('/answer', methods=['GET'])
def answer_form():
    return render_template('answerform.html')


@app.route('/answer', methods=['POST'])
def answer():
    print(request.form)
    context = request.form.get('context')
    question = request.form.get('question')
    response = model([context], [question])
    return render_template('answerform.html', ans=response[0])
