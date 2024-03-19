pessoas = {'Lucas':{'nome':'Lucas' , 'idade':28 , 'cidade':'Palhoça'},
          'Pessoa2':{'nome':'Pessoa2' , 'idade':56 , 'cidade':'São José'},
          'Pessoa3':{'nome':'Pessoa3' , 'idade':12 , 'cidade':'Arroio do Sal'}}

print(pessoas)

pessoas['Lucas'].update({'nome':'lucas gabriel'})

print(pessoas['Lucas'].values())

pessoas['Lucas'].update({'profissão':'estudante'})

print(pessoas['Lucas'].values())

pessoas.pop('Pessoa3')

print(pessoas)