anjos = [{ 'indx': '1', 'name': 'Bom', 'lies': False, 'takesToHeaven': True, 'takesToHell': False },
{ 'indx': '2', 'name': 'Mal', 'lies': True, 'takesToHeaven': False, 'takesToHell': True }]

def doQuestion():
    response = []
    print('É verdade que você pode me levar para o céu ou para o inferno?')
    for anjo in anjos:
        if (anjo['takesToHeaven'] or anjo['takesToHell']) and (anjo['lies'] is False):
            response.append({ 'indx': anjo['indx'], 'name': anjo['name'], 'response': 'SIM' })
        else:
            response.append({ 'indx': anjo['indx'], 'name': anjo['name'], 'response': 'NÃO' })

    return response

response = doQuestion()

print(response, '\n-----------------')
yes = list(filter(lambda x: x['response'] == 'SIM', response))[0]
seq = ['O anjo que está dizendo a verdade é o anjo ', str(yes['indx'])]
finalresponse = ''.join(seq)
print(finalresponse)

    