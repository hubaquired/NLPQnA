from deeppavlov import build_model, configs

model = build_model(configs.squad.squad, download=True)

def extractAnswer(query, passage):
    print('**********')
    print(type(query))
    print(type(passage))
    print('**********')
    answer,num,num2 = model(passage, query)
    print('Answer:'+str(answer))
    print(num)
    print(num2)
    return answer[0]


