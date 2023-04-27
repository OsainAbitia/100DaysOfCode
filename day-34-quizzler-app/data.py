""" Retrieve Quiz API call to get new questions. """
import requests

QUIZ_API_URL = "https://opentdb.com/api.php"

parameter = {"amount": 10, "type": "boolean"}
response = requests.get(QUIZ_API_URL, params=parameter)
question_data = response.json()["results"]

