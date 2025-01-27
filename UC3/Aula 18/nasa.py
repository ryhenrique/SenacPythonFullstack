from flask import Flask, jsonify, request
import requests
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

NASA_API_URL = "https://api.nasa.gov/planetary/"
API_KEY = "kT4I2KtRN1RT3P8\KAY1H8zE10tvVDyn4uMNewpd"  # Substitua por sua própria chave de API

@app.route('/apod', methods=['GET'])
def get_apod():
    """
    Obter a imagem astronômica do dia (APOD) da NASA.
    ---
    responses:
      200:
        description: Retorna informações da imagem astronômica do dia
        schema:
          id: apod
          properties:
            title:
              type: string
              description: Título da imagem
            date:
              type: string
              description: Data da imagem
            explanation:
              type: string
              description: Descrição da imagem
            url:
              type: string
              description: URL da imagem
    """
    params = {
        'api_key': API_KEY,
    }

    response = requests.get(f"{NASA_API_URL}apod", params=params)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "title": data['title'],
            "date": data['date'],
            "explanation": data['explanation'],
            "url": data['url']
        })
    else:
        return jsonify({"error": "Não foi possível obter os dados da NASA."}), response.status_code

@app.route('/mars-weather', methods=['GET'])
def get_mars_weather():
    """
    Obter informações sobre o clima em Marte.
    ---
    responses:
      200:
        description: Retorna informações climáticas de Marte
        schema:
          id: mars_weather
          properties:
            sol:
              type: string
              description: Número do sol (dia marciano)
            temperature:
              type: string
              description: Temperatura média
            pressure:
              type: string
              description: Pressão atmosférica
    """
    params = {
        'api_key': API_KEY,
    }

    response = requests.get(f"{NASA_API_URL}insight_weather/", params=params)
    if response.status_code == 200:
        data = response.json()
        sol_keys = data.get("sol_keys", [])
        if sol_keys:
            latest_sol = sol_keys[-1]
            return jsonify({
                "sol": latest_sol,
                "temperature": data[latest_sol]["AT"]["av"],
                "pressure": data[latest_sol]["PRE"]["av"]
            })
        else:
            return jsonify({"error": "Nenhum dado disponível."})
    else:
        return jsonify({"error": "Não foi possível obter os dados climáticos de Marte."}), response.status_code

@app.route('/neo', methods=['GET'])
def get_near_earth_objects():
    """
    Obter informações sobre objetos próximos da Terra (NEOs).
    ---
    parameters:
      - name: start_date
        in: query
        type: string
        required: true
        description: Data de início no formato YYYY-MM-DD
      - name: end_date
        in: query
        type: string
        required: true
        description: Data de término no formato YYYY-MM-DD
    responses:
      200:
        description: Retorna uma lista de objetos próximos da Terra
        schema:
          id: neo
          properties:
            name:
              type: string
              description: Nome do objeto
            diameter:
              type: string
              description: Diâmetro estimado
            hazardous:
              type: boolean
              description: Se o objeto é potencialmente perigoso
    """
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Parâmetros start_date e end_date são obrigatórios."}), 400

    params = {
        'start_date': start_date,
        'end_date': end_date,
        'api_key': API_KEY,
    }

    response = requests.get(f"{NASA_API_URL}neo/rest/v1/feed", params=params)
    if response.status_code == 200:
        data = response.json()
        neos = []
        for date in data['near_earth_objects']:
            for neo in data['near_earth_objects'][date]:
                neos.append({
                    "name": neo['name'],
                    "diameter": neo['estimated_diameter']['meters']['estimated_diameter_max'],
                    "hazardous": neo['is_potentially_hazardous_asteroid']
                })
        return jsonify(neos)
    else:
        return jsonify({"error": "Não foi possível obter os dados dos NEOs."}), response.status_code


@app.route('/rovers', methods=['GET'])
def get_mars_rover_images():
    """
    Obter imagens capturadas pelos rovers em Marte.
    ---
    parameters:
      - name: rover
        in: query
        type: string
        required: true
        description: Nome do rover (curiosity, opportunity, spirit)
      - name: sol
        in: query
        type: integer
        required: true
        description: Sol (dia marciano) para as imagens
    responses:
      200:
        description: Retorna URLs de imagens capturadas pelos rovers
        schema:
          id: rover_images
          properties:
            images:
              type: array
              items:
                type: string
              description: Lista de URLs de imagens
    """
    rover = request.args.get('rover')
    sol = request.args.get('sol')

    if not rover or not sol:
        return jsonify({"error": "Parâmetros rover e sol são obrigatórios."}), 400

    params = {
        'sol': sol,
        'api_key': API_KEY,
    }

    response = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos", params=params)
    if response.status_code == 200:
        data = response.json()
        images = [photo['img_src'] for photo in data['photos']]
        return jsonify({"images": images})
    else:
        return jsonify({"error": "Não foi possível obter as imagens do rover."}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)