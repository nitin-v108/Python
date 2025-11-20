import multiprocessing
import requests

# https://picsum.photos/2000/3000


def downloadImages(url, name):
    print(f"Download started for : {name}")
    res = requests.get(url)
    open(f"downloads/file-{name}.jpg", "wb").write(res.content)
    print(f"Download ended for : {name}")


if __name__ == "__main__":
    proc = []
    url = "https://picsum.photos/2000/3000"
    for i in range(5):
        p = multiprocessing.Process(target=downloadImages, args=[url, i])
        p.start()
        proc.append(p)

    for p in proc:
        p.join()
