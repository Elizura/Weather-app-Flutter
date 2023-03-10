import requests
def get_profile_info(user_data): #{id}  
  url = "https://jsonplaceholder.typicode.com/posts/1"
  payload = {"id": user_data.id}
  response = requests.get(url, params=payload)
  response_json = response.json()    
  return response_json

def register(user_data, phoneNumber):
  user_data.phoneNumber = phoneNumber
  post_response = requests.post(url, json = user_data)  
  post_response_json = post_response.json()
  return post_response_json


