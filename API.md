# lets discuss about API in python and requests module
# lets do practical problems covering all commands with public api

import requests

API - application programming interface

client(you) - api - server(swggy kitchen, etc)

API methods - read or to transform any data in api, we can use these methods to fulfill the task

get - read data & gives you response
post - create new data
put - update the full/complete data
patch - update partial data
delete - removes or deletes the data completely

Authentication methods

api key - a unique key like password https:some api/data?api_key=123455
bearer token - a secret token used in headers
basic auth - username + password
oauth - advanced auth methods

status codes - api respons emessages 

200 - ok - success
404 - not found - wrong url
401 - unauthorized - no valid token
500 - server error - problems on server side



# # get request
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:    print("Failed to retrieve data")

# post request
# new_post = {
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1
# }
# response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
# if response.status_code == 201:
#     data = response.json()
#     print(data)
# else:    print("Failed to create post")

# put request
# updated_post = {
#     'id': 111,    
#     'title': 'suiuuu',
#     'body': 'bar_hjkh',  
#     'userId': 2 
# }
# response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=updated_post)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:    print("Failed to update post")

# patch request

# updated_post = {
#     'title': 'jena',
# }
# response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=updated_post)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:    print("Failed to update post")

# delete request

# response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
# if response.status_code == 200:
#     print("Post deleted successfully")
# else:    print("Failed to delete post")

# now lets


