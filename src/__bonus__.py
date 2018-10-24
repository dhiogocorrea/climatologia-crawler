angels = [{ 'indx': '1', 'name': 'Bom', 'lies': False, 'takesToHeaven': True, 'takesToHell': False },
{ 'indx': '2', 'name': 'Mal', 'lies': True, 'takesToHeaven': False, 'takesToHell': True }]

def doQuestion():
    angel_responses = []
    print('É verdade que você pode me levar para o céu ou para o inferno?')
    for a in angels:
        resp = (a['takesToHeaven'] or a['takesToHell']) and (a['lies'] is False)
        angel_responses.append({ 'indx': a['indx'], 'name': a['name'], 'response': resp })

    return angel_responses

response = doQuestion()

print(response, '\n-----------------')
yes = list(filter(lambda x: x['response'] is True, response))[0]
finalresponse = ''.join(['O anjo que está dizendo a verdade é o anjo ', str(yes['indx'])])
print(finalresponse)