#JSON
'''
{
"azienda":"pippo srl",
"impiegati":[
    {'matricola':'123', 'nome':'mario rossi'}  ,
    {'matricola':'124', 'nome':'luigi bianchi'},
    {'matricola':'125', 'nome':'anna verdi'}
    ]
}   
'''

import json

with open('azienda.json', 'r') as f:
    obj = json.load(f)
    #print(azienda)
    print(obj['azienda'])
    print(obj['impiegati'][0]['nome'])
    

rub = dict()
rub['1234'] = {'nome':'Mario', 'cognome':'Rossi', 'data':'01/01/2000'}
rub['3456'] = 'Luigi'
rub['6789'] = 'Anna'

with open('rubrica1.json', 'w') as f:
    json.dump(rub, f)

