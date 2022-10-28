import requests

def getHotelsByName(name):
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {"q":name,"locale":"en_US","langid":"1033","siteid":"300000001"}

    headers = {
        "X-RapidAPI-Key": "f318e8573amsha7246f29e8d7de7p1c368fjsn5b4af82f4ba1",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if (response.status_code == 200):
        jsonResult = response.json()
        hotelDic = {}
        for hotel in jsonResult["sr"]:
            hotelDic[hotel["hotelId"]] = { 
                "name": hotel["regionNames"]["shortName"],
                "address": hotel["hotelAddress"]["street"],
                "city": hotel["hotelAddress"]["city"],
                "province": hotel["hotelAddress"]["province"]
            }
        return hotelDic
    return None 

def getReviewById(hotelId):
    url = "https://hotels4.p.rapidapi.com/reviews/v3/list"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotelId,
        "size": 20,
        "startingIndex": 0
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f318e8573amsha7246f29e8d7de7p1c368fjsn5b4af82f4ba1",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if (response.status_code == 200):
        jsonResult = response.json()
        #print(jsonResult)
        reviews = []
        for review in jsonResult["data"]["propertyInfo"]["reviewInfo"]["reviews"]:
            if (len(review["text"])>0):
                reviews.append(review["text"])
        return reviews
    return None

def getHotelDetailById(hotelId):
    url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotelId
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f318e8573amsha7246f29e8d7de7p1c368fjsn5b4af82f4ba1",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if (response.status_code == 200):
        jsonResult = response.json()
        #print(jsonResult)
        hotel = {
            "name":jsonResult["data"]["propertyInfo"]["summary"]["name"],
            "address": jsonResult["data"]["propertyInfo"]["summary"]["location"]["address"]["addressLine"],
            "city": jsonResult["data"]["propertyInfo"]["summary"]["location"]["address"]["city"],
            "province": jsonResult["data"]["propertyInfo"]["summary"]["location"]["address"]["province"],
            "value":jsonResult["data"]["propertyInfo"]["reviewInfo"]["summary"]["overallScoreWithDescriptionA11y"]["value"],
            "reviews":[]
        }
        return hotel
    return None
    
def getValue(hotelId):
    url = "https://hotels4.p.rapidapi.com/reviews/v3/get-summary"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotelId
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f318e8573amsha7246f29e8d7de7p1c368fjsn5b4af82f4ba1",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if (response.status_code == 200):
        jsonResult = response.json()
        #print(jsonResult)
        return jsonResult["data"]["propertyReviewSummaries"][0]["overallScoreWithDescriptionA11y"]["value"]
    return None
