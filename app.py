from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():

    datos = request.get_json()

    valor = datos['valor']
    escala = datos['escala']

    if escala == "C":
        resultado = (valor * 9/5) + 32
        escala_resultado = "F"
    elif escala == "F":
        resultado = (valor - 32) * 5/9
        escala_resultado = "C"
    else:
        return jsonify({"error": "Escala no válida. Usa C o F"}), 400

    respuesta = {
        "valor_original": valor,
        "escala_original": escala,
        "resultado": resultado,
        "escala_resultado": escala_resultado
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)