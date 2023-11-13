import requests

BASE_URL = "http://127.0.0.1:5000"

def get_cardapio():
    try:
        response = requests.get(f'{BASE_URL}/cardapio')
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
    
def registra_prato(data):
    try:
        response = requests.post(f"{BASE_URL}/cardapio",data=data)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
    