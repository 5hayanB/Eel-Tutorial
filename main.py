from eel import init, start, expose
from json import dumps

init('web')

filePath = 'web/JSON/data.json'

@expose
def generate(core, bus, devices):
    json = dumps({"core": core, "bus": bus, "devices": devices})
    with open(filePath, 'w', encoding='UTF-8') as f:
        print(json)
        f.write(str(json))

start('index.html')
