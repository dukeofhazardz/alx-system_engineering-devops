import requests

api_key = "586d4b0fb6b7d82fd69766e00bda3218"
url = "https://api.datadoghq.com/api/v1/hosts/totals"

headers = {
    "Content-Type": "application/json",
    "DD-API-KEY": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    active_hosts = data["active"]
    print("Number of active hosts:", active_hosts)
else:
    print("Error:", response.status_code)
