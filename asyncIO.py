# import time
# import asyncio


# def function1():
#     time.sleep(3)
#     print("Function1")
    
# def function2():
#     time.sleep(3)
#     print("Function2")
    
# def function3():
#     time.sleep(3)
#     print("Function3")
    
    
# function1()
# function2()
# function3()



# import time
# import asyncio

# async def function1():
#     time.sleep(3)
#     print("Function1")
    
# async def function2():
#     time.sleep(3)
#     print("Function2")
    
# async def function3():
#     time.sleep(3)
#     print("Function3")
    
   
# async def main(): 
#     await function1()
#     await function2()
#     await function3()
    

# asyncio.run(main())




# import time
# import asyncio

# async def function1():
#     await asyncio.sleep(1)
#     print("Function1")
    
# async def function2():
#     await asyncio.sleep(1)
#     print("Function2")
    
# async def function3():
#     await asyncio.sleep(4)
#     print("Function3")
    
   
# async def main(): 
#     task = asyncio.create_task(function1())
#     # await function1()
#     await function2()
#     await function3()
    

# asyncio.run(main())



# import time
# import asyncio
# import requests


# async def function1():
#     await asyncio.sleep(1)
#     print("Function1")
    
#     url = 'http://google.com/favicon.ico'
#     r = requests.get(url, allow_redirects=True)
#     open('F:/Python/CWH_Python/Python_Day96/google1.ico', 'wb').write(r.content)
    
#     return "Pranav"
    
# async def function2():
#     await asyncio.sleep(1)
#     print("Function2")
    
#     url = 'http://google.com/favicon.ico'
#     r = requests.get(url, allow_redirects=True)
#     open('F:/Python/CWH_Python/Python_Day96/google2.ico', 'wb').write(r.content)

#     return "Raj"
    
# async def function3():
#     await asyncio.sleep(4)
#     print("Function3")
    
#     url = 'http://google.com/favicon.ico'
#     r = requests.get(url, allow_redirects=True)
#     open('F:/Python/CWH_Python/Python_Day96/google3.ico', 'wb').write(r.content)
    
#     return "Jay"
    
   
# async def main(): 
#     # task = asyncio.create_task(function1())
#     # await function1()
#     # await function2()
#     # await function3()
    
#     L = await asyncio.gather(
#         function1(),
#         function2(),
#         function3()
#     )
#     print(L)
    

# asyncio.run(main())




import time
import asyncio
import requests


async def function1():
    print("Function1")
    # url = 'http://google.com/favicon.ico'
    url = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    r = requests.get(url, allow_redirects=True)
    open('F:/Python/CWH_Python/Python_Day96/google1.ico', 'wb').write(r.content)
    return "Raj"
    
async def function2():
    print("Function2")
    # url = 'http://google.com/favicon.ico'
    url = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    r = requests.get(url, allow_redirects=True)
    open('F:/Python/CWH_Python/Python_Day96/google2.ico', 'wb').write(r.content)
    return "Om"

    
async def function3():
    print("Function3")
    # url = 'http://google.com/favicon.ico'
    url = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    r = requests.get(url, allow_redirects=True)
    open('F:/Python/CWH_Python/Python_Day96/google3.ico', 'wb').write(r.content)
    return "Jay"
    
   
async def main(): 
    # task = asyncio.create_task(function1())
    await function1()
    await function2()
    await function3()
    return 3
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)
    

asyncio.run(main())