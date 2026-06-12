#pip install requests.
import requests

response = requests.get("https://example.com")

print(response.status_code)  # 200
print(response.text)         # HTML della pagina