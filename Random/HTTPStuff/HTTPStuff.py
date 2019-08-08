import requests


def plainExample(url, response):
    plainResponse = requests.get(url, headers={"Accept": "text/plain"})
    print(f"Your request to {url} came back with status code {response.status_code}.")
    print(plainResponse.text)
    return

def jsonExample(url, response):
    jsonResponse = requests.get(url, headers={"Accept": "application/json"})
    data = jsonResponse.json()
    print(data)
    # json requests retrieve a python dictionary of data
    print(data["joke"])
    print(f"stats: {data['status']}")
    return

def jsonParameters():
    # Can put the search term in the url or params
    #url = "https://icanhazdadjoke.com/search?term=cat"
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": "cat"}
    )
    data = response.json()
    print(data["results"])
    print(f"status: {data['status']}")
    return

def main():

    url = "https://icanhazdadjoke.com/"
    response = requests.get(url)

    #plainExample(url, response)
    #jsonExample(url, response)
    jsonParameters()













if __name__ == "__main__":
    main()