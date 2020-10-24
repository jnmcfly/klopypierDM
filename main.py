import requests

#shopId = "951" # schwalmstadt
shopId = "2387"


articles = ["595420", "708997", "137425", "28171", "485698", "799358", "863567", "452740", "610544", "846857", "709006", "452753", "879536", "452744", "485695", "853483", "594080", "504606", "593761", "525943", "842480", "535981", "127048", "524535"]
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/517.66 (KHTML, like Gecko) Chrome/79.0.3945.88"}

def getPaper(articles, shopId):
    i = 0
    paper = 0
    while i < len(articles):
        currentArticle = articles[i]
        url = "https://products.dm.de/store-availability/DE/products/dans/" + articles[i] + "/stocklevel?storeNumbers=" + shopId
        req = requests.get(url, headers=headers)
        count = req.json()['storeAvailability'][0]['stockLevel']
        i += 1
        paper += count
        pass
    return paper

def getStoreInfo(shopId):
    url = 'https://store-data-service.services.dmtech.com/stores/item/de/' + shopId
    req = requests.get(url)
    info = req.json()["address"]["city"] + ", " + req.json()["address"]["street"]

    return info

sum = getPaper(articles, shopId)
info = getStoreInfo(shopId)

print("Noch " + str(sum) + " Packungen Klopapier in Filiale " + info)

