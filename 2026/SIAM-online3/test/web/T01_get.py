from urllib.request import urlopen

with urlopen("https://example.com") as response:
    html = response.read().decode("utf-8")
    print(html)