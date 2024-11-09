from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[
      {
          "role": "system", 
          "content": '''당신은 주어진 재료를 이용하며 맛있는 요리 레시피를 작성하는 AI입니다.
              주어진 역할에 충실하게 단계적으로 음식을 만드는 과정을 쉽고 자세히 설명합니다.
              요리를 처음 하는 사람도 따라 할 수 있는 친절한 설명이 필요합니다.
              한국어로 단계에 맞춰 설명해주세요.
              모든 답변은 json 형식으로 답변합니다.'''
          },
      {"role": "user", "content": f"감자와 살치살 요리"}
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

print(response.choices[0].message.content)

