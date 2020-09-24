import requests 
image_url = "https://picsum.photos/200/300" 
r = requests.get(image_url)
with open("1.jpg",'wb') as f: 
    f.write(r.content) 