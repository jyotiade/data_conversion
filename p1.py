#============python to json conversion=============using dumps================

import json
python_data={'Name':'jyoti',
             'quali':"b.tech",
             'city_bhopal':True,
             'belongs':False,
             'activity':None}

print(json.dumps(python_data))
print(type(json.dumps(python_data)))

#==the datatype of json is string============

