import requests

url = "https://logos-download.com/wp-content/uploads/2016/10/Python_logo_wordmark.png"
response = requests.get(url)
# print(response) to check if a file store in response via url
# print(response.text)
# print(response.content)

with open("python.jpg", "wb") as file:
    file.write(response.content)