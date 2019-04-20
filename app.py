from deeppavlov import build_model, configs

model = build_model(configs.squad.squad, download=True)
context = 'DeepPavlov is library for NLP and dialog systems.'
question = 'What is DeepPavlov?'
response = model([context], [question])
print(response)
print('Done!')
