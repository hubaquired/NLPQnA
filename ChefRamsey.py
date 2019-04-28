def answerQuery(query):
    flags = queryAnalysis(query)
    passages = findPassages(query,1)
    for passage in passages:
        extractAnswer(query, passage)
    pass
