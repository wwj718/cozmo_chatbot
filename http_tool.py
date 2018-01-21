import requests


# r = requests.post('http://httpbin.org/post', json={"key": "value"})

def post_content_to_cozmo(content):
    requests.post('http://127.0.0.1:5001/cozmo_say', json={"content": content})