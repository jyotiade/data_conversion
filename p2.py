# =============================json to python conversion
import json

data='{"Name": "jyoti", "quali": "b.tech", "city_bhopal": true, "belongs": false, "activity": null}'
print(json.loads(data))
data='{"Name": "avi", "quali": "b.tech", "city_balaghat": true, "belongs": false, "activity": null}'
print(json.loads(data))