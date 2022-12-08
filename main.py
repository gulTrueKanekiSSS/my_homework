import json
import flask

def load_candidates():
    with open("candidates.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_all():
    candidates = []
    data = load_candidates()
    for i in data:
        candidates.append(i)
    return candidates



def get_by_pk(pk):
    data = load_candidates()
    for i in data:
        if i['pk'] == pk:
            return i


def get_by_skill(skill_name):
    data = load_candidates()
    scientist = []
    for i in data:
        if skill_name.lower() in i['skills'].lower():
            scientist.append(i)
    return scientist

app = flask.Flask(__name__)

@app.route("/")
def main_page():
    text = ''
    for i in get_all():
        text += f'<pre>Имя кандината - {i["name"]}\n{i["position"]}\n{i["skills"]}'
    return text

@app.route("/candidates/<int:x>")
def candidates(x):
    hoy = get_by_pk(x)
    url = "http://mypictures.me/123"
    text = f'<img src="{url}">\n<pre>Имя кандидата - {hoy["name"]} \nПозиция кандидата - {hoy["position"]}"\nНавыки через запятую{hoy["skills"]}</pre>\n'
    return text
@app.route("/skills/<x>")
def skills(x):
    text = ""
    hate = get_by_skill(x)
    for i in hate:
        text += f'<pre>Имя кандината - {i["name"]}\n{i["position"]}\n{i["skills"]}'
    return text

app.run(host='0.0.0.0', port=8000)

