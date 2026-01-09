import requests ,json

api=requests.get('https://solid-succotash-69xr6vvgx6gxf56vg-8000.app.github.dev/')
print(json.dump(api.json())) 