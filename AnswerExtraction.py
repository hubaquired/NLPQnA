from deeppavlov import build_model, configs

model = build_model(configs.squad.squad, download=True)

def extractAnswer(query, passage):
    answer,num,num2 = model(passage, query)
    return answer


