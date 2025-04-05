import requests
# response = requests.get("https://uaserials.pro/films/")
# print("response.content")
# print(type(response.content))
# response = requests.post("https://httpbin.org/get",data="Test data")
# headers = {'h1:'"Test title"}
# print(response.text)

respons = requests.get("https://coinmarketcap.com/")
responce_text = respons.text
responce_parse = responce_text.split("<span>")
for pars_elem_1 in responce_parse:
    if pars_elem_1.startwith('$'):
        for pars_elem_2 in pars_elem_1.split('<span>')
            print(pars_elem_1)