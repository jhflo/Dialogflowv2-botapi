
import json
from flask import Flask
from flask import request
from flask import jsonify
from nplv2 import nlpprocess

app = Flask(__name__)
#app.run(host='0.0.0.0')

#Ruta de flask que escucha el Webhook de Cisco Spark creado para el bot
@app.route('/dialogflow', methods=['POST'])
def index():
    """
    Recoleccion de la informacion del Webhook

    """
    webhook = request.data
    webhook = json.loads(webhook)
    datos = nlpprocess(webhook)
    return jsonify(datos.processdata())






####Variables fijas AbaCoXBot#####


if __name__ == "__main__":
    app.run()
