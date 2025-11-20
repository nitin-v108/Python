import asyncio
import requests


async def fun1():
    print("fun1() >> Init..")
    url = "https://images.pexels.com/photos/443446/pexels-photo-443446.jpeg?cs=srgb&dl=pexels-eberhardgross-443446.jpg&fm=jpg"
    response = requests.get(url)
    open("img1.jpg", "wb").write(response.content)
    print("fun1() >> Ended..")
    return "img1.jpg"


async def fun2():
    print("fun2() >> Init..")
    url = "https://wallpapercat.com/w/full/0/f/3/5815630-3840x2160-desktop-hd-4k-wallpaper-image.jpg"
    response = requests.get(url)
    open("img2.jpg", "wb").write(response.content)
    print("fun2() >> Ended..")
    return "img2.jpg"


async def fun3():
    print("fun3() >> Init..")
    url = "https://img2.wallspic.com/crops/9/6/5/2/0/102569/102569-reflection-apple_macbook_pro-sky-mountain-lake-2560x1440.jpg"
    response = requests.get(url)
    open("img3.jpg", "wb").write(response.content)
    print("fun3() >> Ended..")
    return "img3.jpg"


print("This demo is with AsyncIO : Asynchronous Programming")
print(" ## Process STARTED...")


async def main():
    // TODO :: Uncomment below code to check without async response.
    # await fun1()
    # await fun2()
    # await fun3()
    # return 1
    img = await asyncio.gather(fun1(), fun2(), fun3())
    return img


result = asyncio.run(main())
print("Final Result is :: ", result)

print(" ## Process ENDED...")
