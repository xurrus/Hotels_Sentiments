def getScoreTag(review):
    import requests

    url = "https://api.meaningcloud.com/sentiment-2.1"

    payload={
        'key': 'c047dad9729fadcb06818fee1c21e79c',
        'txt': review,
        'lang': 'en',  # 2-letter code, like en es fr ...
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        myjson = response.json()
        estadocompleto = (myjson["score_tag"],myjson["agreement"],myjson["confidence"])
        return estadocompleto
    return None