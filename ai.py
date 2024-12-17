import requests
from typing import Optional
from dotenv import load_dotenv
import os
import json

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = os.getenv('LANGFLOW_FLOW_ID')
APPLICATION_TOKEN_1 = os.getenv('LANGFLOW_TOKEN_1')
APPLICATION_TOKEN_2 = os.getenv('LANGFLOW_TOKEN_2')

def dict_to_string(obj, level=0):
    strings = []
    indent = "  " * level  # Indentation for nested levels
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                nested_string = dict_to_string(value, level + 1)
                strings.append(f"{indent}{key}: {nested_string}")
            else:
                strings.append(f"{indent}{key}: {value}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            nested_string = dict_to_string(item, level + 1)
            strings.append(f"{indent}Item {idx + 1}: {nested_string}")
    else:
        strings.append(f"{indent}{obj}")

    return ", ".join(strings)

def ask_ai(profile,question):
  TWEAKS = {
    "TextInput-jc24F": {
      "input_value": question
    },
    "TextInput-s34sI": {
      "input_value": dict_to_string(profile)
    },
  }
  return run_flow_1("",tweaks=TWEAKS,application_token=APPLICATION_TOKEN_1)

def run_flow_1(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/ask-ai"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]


def get_macros(profile,goals):
  TWEAKS = {
    "TextInput-1Alpi": {
        "input_value":", ".join(goals)
    },
    "TextInput-VcA17": {
        "input_value":dict_to_string(profile)
    },
  }
  return run_flow_2("",tweaks=TWEAKS,application_token=APPLICATION_TOKEN_2)

def run_flow_2(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/macros"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return json.loads(response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"])

# result = get_macros("height: 176cm, weight: 70 kg, gender: male,very active","muscle gain")
# print(result)