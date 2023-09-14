import requests

url = 'http://127.0.0.1:8000/housing/'
data = {
    'title': 'Название жилого объекта',
}

files = [
    ('images', ('image1.jpg', open('image1.jpg', 'rb'))),
    ('images', ('image2.jpg', open('image2.jpg', 'rb'))),
]

response = requests.post(url, data=data, files=files)
