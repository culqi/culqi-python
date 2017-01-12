import culqipy, requests

def jsonResult(key, url, data, method):
    headers = {"Authorization": "Bearer "+key, "content-type": "application/json"}
    r = ""
    if method.upper() == "POST":
        r = requests.post(culqipy.API_URL+url, headers=headers, data=data, timeout=60)
    return r.json()
