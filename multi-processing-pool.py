import concurrent.futures
import requests

# https://picsum.photos/2000/3000


def downloadImages(url, name):
    print(f"Download started for : {name}")
    res = requests.get(url)
    open(f"downloads/file-{name}.jpg", "wb").write(res.content)
    print(f"Download ended for : {name}")
    return f"downloads/file-{name}.jpg"


if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    with concurrent.futures.ProcessPoolExecutor() as executer:
        urls = [url for j in range(5)]
        i = [j for j in range(5)]
        print(urls)
        results = executer.map(downloadImages, urls, i)
        for result in results:
            print(result)
