def answerQuery(query):
    flags = queryAnalysis(query)
    passages = findPassages(query,1)
    answers = []
    for passage in passages:
        answers.append(extractAnswer(query, passage))
    answer = best_answer(answers)
    return answer

def best_answer(answer_list):
    return answer_list[0]

def queryAnalysis(query):
    return None


