from flask import Flask, request, jsonify, render_template
from pydantic import BaseModel
from openai import OpenAI
import re
import json

client = OpenAI()

app = Flask(__name__, template_folder='public')

@app.route('/')
def main_page():
   return render_template('index.html')



@app.route('/generate', methods=['POST'])
def generate_response():
  data = request.json  # POST로 보낸 데이터를 JSON 형식으로 받음
  user_chat = data.get("chat")
  print(user_chat)
  if not user_chat:
    return jsonify({"error": "No chat provided"}), 400
    
  completion = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[
      {
          "role": "system", 
          "content": '''당신은 주어진 재료를 이용하며 맛있는 요리 레시피를 작성하는 AI입니다.
              주어진 역할에 충실하게 단계적으로 음식을 만드는 과정을 쉽고 자세히 설명합니다.
              요리를 처음 하는 사람도 따라 할 수 있는 친절한 설명이 필요합니다.
              한국어로 단계에 맞춰 설명해주세요.
            '''
          },
      {"role": "user", "content": f"{user_chat}"}
    ],
    response_format={
      "type": "json_schema",
      "json_schema": {
        "name": "recipes",
        "schema": {
          "type": "object",
          "properties": {
            "title" : {"type": "string"},
            "summary" : {"type": "string"},
            "ingredients" : {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": {"type": "string"},
                  "ea": {"type": "string"}
                },
                "required": ["name", "ea"],
                "additionalProperties": False
              }
            },
            "steps": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "step": {"type": "string"},
                },
                "required": ["step"],
                "additionalProperties": False
              }
            },
            "tips": {"type": "string"}
          },
          "required": ["title","summary","ingredients","steps", "tips"],
          "additionalProperties": False
        },
        "strict": True
      }
    }
  )

  generated_text = completion.choices[0].message.content

  print(generated_text)
  response_data = json.loads(generated_text)

  return jsonify(response_data)


@app.route('/generate_img', methods=['POST'])
def generate_img():
  data = request.json  # POST로 보낸 데이터를 JSON 형식으로 받음
  user_img = data.get("img")
  if not user_img:
    return jsonify({"error": "No chat provided"}), 400

  image = client.images.generate(
    model="dall-e-3",
    prompt=f"{user_img}",
    n=1,
    size="1024x1024",
    response_format='url'
  )
  generated_img = image.data[0].url

  return  jsonify({'image' : generated_img})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

