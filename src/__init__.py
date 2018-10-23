import libs.crawler as c
import json
import os

execution_path = os.getcwd()
outputFile = os.path.join(execution_path , 'output.csv')

try:
    os.remove(outputFile)
except OSError:
    pass

states = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']

f = open(outputFile, 'a')
f.write('Cidade,Estado,Mínimo Temperatura,Máximo Temperatura,Precipitação (mm)\n')
f.close()

def crawl():
    for state in states:
        r = c.getState(state)

        if r is not None:
            stateObj = json.loads(r.text)

            if (stateObj['success'] is True):
                cities = stateObj['data']

                for city in cities:
                    data = c.processCity(state, city)

                    if len(data):
                        strFinal = ''
                        for d in data:
                            list = d['city'], d['state'], d['month'], d['minTemp'], d['maxTemp'], d['precipitation']
                            strFinal = strFinal + ','.join(list)
                            strFinal = strFinal + ''.join('\n')
                        f = open(outputFile, 'a')
                        f.write(strFinal)
                        f.close()

crawl()
