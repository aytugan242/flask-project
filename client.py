import requests as rq

response = rq.post(
    "http://127.0.0.1:5000/advertisements",
    json={
        'header': 'Заголовок 2',
        "description": "Описание 2",
        "owner": "aitugan2"
    },

)
print(response.status_code)
print(response.text)

# response = rq.get(
#     "http://127.0.0.1:5000/advertisements/1",
#
#
# )
# print(response.status_code)
# print(response.text)


# response = rq.delete(
#     "http://127.0.0.1:5000/advertisements/1",
#
#
# )
# print(response.status_code)
# print(response.text)


