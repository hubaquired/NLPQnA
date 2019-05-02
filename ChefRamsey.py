import sys
import json
import requests
from AnswerExtraction import extractAnswer

solr_core = 'ChefRamsey'

def answerQuery(query):
    query = query.replace('?', '')
    flags = queryAnalysis(query)
    passages,query = findPassages(query,10)
    answers = []
    for passage in passages:
        print('----------------------------------------------------------')
        print('Query: '+str(query)+'\nPassage: '+str(passage)+'\n')
        answers.append(extractAnswer(query, passage))
        print('----------------------------------------------------------')
    answer = best_answer(answers)
    return answer

def findPassages(query, max_resp=10):
    formatted_query = format_solr_query(query)
    results = requests.get(formatted_query).json() 
    response = [i['passage'] for i in results['response']['docs']]
    names = [i['name'][0].strip() for i in results['response']['docs']]
    print(names)
    for name in names: query = query.replace(name,'').strip()
    return response[0:max_resp],query

def format_solr_query(query):
    edismax_str = '/select?defType=edismax&'
    beginning_str = 'http://localhost:8983/solr/'+solr_core+edismax_str
    query = 'q='+query+'&'
    rows = '&rows=100'
    weight_str = 'qf=name^10 passage'
    new_qry = beginning_str+query+weight_str
    print(new_qry)
    return new_qry

def best_answer(answer_list):
    if len(answer_list) == 0: 
        print('ANSWER FAILURE')
        return None
    return answer_list[0]

def queryAnalysis(query):
    return None

