import sys
import json
import requests
from AnswerExtraction import extractAnswer

solr_core = 'ChefRamsey'

def answerQuery(query):
    flags = queryAnalysis(query)
    passages = findPassages(query,1)
    answers = []
    for passage in passages:
        answers.append(extractAnswer(query, passage))
    answer = best_answer(answers)
    return answer

def findPassages(query, max_resp=1):
    formatted_query = format_solr_query(query)
    print(formatted_query)
    results = requests.get(formatted_query).json() 
    response = [i['passage'] for i in results['response']['docs']]
    print(response[0])
    return response[0:max_resp]

def format_solr_query(query):
    edismax_str = '/select?defType=edismax&'
    beginning_str = 'http://localhost:8983/solr/'+solr_core+edismax_str
    query = 'q='+query+'&'
    rows = '&rows=100'
    weight_str = 'qf=name^10 passage^1'
    new_qry = beginning_str+query+weight_str+rows
    return new_qry

def best_answer(answer_list):
    if len(answer_list) == 0: 
        print('ANSWER FAILURE')
        return None
    return answer_list[0]

def queryAnalysis(query):
    return None

