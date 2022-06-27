import re
import pandas as pd
import json

orders_id = []
dictionary = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
jsonString = json.dumps(dictionary, indent=4)
# print(jsonString)

#read the line structure into a variable
line_list = str(jsonString)
#assign the regex pattern to a variable
pattern = re.compile(r'"id":([^,]+\n)')

for match in re.finditer(pattern, line_list):
    orders_id.append(match.group(1))

# removing extra elemnts from the list and convert it into a DataFrame
orders_id = pd.DataFrame(orders_id)
orders_id[0] = orders_id[0].str.replace('\n', '') 
orders_id[0] = orders_id[0].str.replace('}', '') 
orders_id[0].str.strip()
print(orders_id)
