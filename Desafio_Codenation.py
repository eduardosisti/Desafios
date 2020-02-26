import requests
import string
import json
import hashlib

# token adquirido do site codenation
token = 'f3ccc82c6de7981014f4ea0d07557818a6d2e***'

# Adquirir dados [GET]
def get_challenge(token):
    url = f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={token}'
    data = requests.get(url)
    answer_content = json.loads(data.content)
    with open('answer.json', 'w') as f:
        json.dump(answer_content, f)
    return answer_content

# Descriptografar
def decifrar():
    with open('answer.json', 'r') as arq:
        data = json.load(arq)
        encoding = arq.encoding

    alfabeto = (list(string.ascii_lowercase))

    decifrado =[]
    for x in data['cifrado']:
        if x == " ":
            decifrado.append(" ")
        elif x == ".":
            decifrado.append(".")
        else:
            y = alfabeto.index(x)
            decifrado.append(alfabeto[y-2])

    decifrado_ajuste = ''.join(map(str, decifrado))
    data['decifrado'] = decifrado_ajuste

    resumo = hashlib.sha1(data['decifrado'].encode(encoding)).hexdigest()
    data['resumo_criptografico'] = resumo

    with open('answer.json', 'w') as arq:
    json.dump(data, arq)


# submeter [POST]
POST = f"https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={(token)}"
answer = {'answer': open('answer.json', 'rb')}
submit = requests.post(POST, files=answer)
print(submit.headers)