import json
from flaskr.db import get_db

db = get_db()

with open('data.json', encoding='utf-8') as f:
	data = json.load(f)

print(data)