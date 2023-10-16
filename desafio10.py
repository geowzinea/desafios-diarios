#1. Aprenda como a estrutura de hash funciona - veja o material de apoio
#2. Agora que você já sabe como um hash funciona, dado um hash com dados pessoais de um usuário, imprima esses valores na tela

d = {'nome': 'Geovanna', 'idade':25, 'profissão': 'programadora' }
for chave, valor in d.items():
   print(f'{chave}: {valor}') 