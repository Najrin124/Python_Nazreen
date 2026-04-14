import requests

# # get requests
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Failed to retrieve data")

# post requests
# new_post = {
#     'title':'foo',
#     'body':'bar',
#     'userid': 1
# }

# response = requests.post('https://jsonplaceholder.typicode.com/posts', json = new_post)
# if response.status_code == 201:
#     data = response.json()
#     print(data)
# else:
    # print("Failed to create post")

# put response
# updated_post = {
#     'id' : 111,
#     'title': 'suiuu',
#     'body' : 'bar_hjkh',
#     'userid':2
# }

# response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json = updated_post)
# if response .status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Failed to update post")    

# # patch request
# update_post = {
#     'title':'khan',
#     }
# response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=update_post)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Failed to update post")    

# delete request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print("Post delete successfully")
else:
    print("Failed to delete data")    

