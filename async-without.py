import requests

def fun1():
    url = "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg?cs=srgb&dl=pexels-souvenirpixels-417074.jpg&fm=jpg"
    response = requests.get(url)
    open("img1.jpg","wb").write(response.content) 
    print("fun1 DONE - img1.jpg Saved.")
def fun2():
    url = "https://elviajerofeliz.com/wp-content/uploads/2015/09/paisajes-de-Canada.jpg"
    response = requests.get(url)
    open("img2.jpg","wb").write(response.content) 
    print("fun2 DONE - img2.jpg Saved.")
def fun3():
    url = "https://img2.wallspic.com/crops/9/6/5/2/0/102569/102569-reflection-apple_macbook_pro-sky-mountain-lake-2560x1440.jpg"
    response = requests.get(url)
    open("img3.jpg","wb").write(response.content) 
    print("fun3 DONE - img3.jpg Saved.")

print("This demo is without AsyncIO")
print(" ## Process STARTED...")
def main():
    fun1()
    fun2()
    fun3()
    
main()
print(" ## Process ENDED...")