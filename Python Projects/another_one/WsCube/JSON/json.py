#do on replit

import json 

file = open("post.json","r")
json_data = file.read()
final_data = json.loads(json_data)
print(final_data) 