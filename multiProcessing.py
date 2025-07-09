import multiprocessing
import requests
import concurrent.futures
# from concurrent.futures import ProcessPoolExecutor

def downloadFile(url, name):
    try:
        print(f"Starting downloading {name}")
        r = requests.get(url)
        open(f'F:/Python/CWH_Python/Python_Day98/files/{name}.jpg', 'wb').write(r.content)
        print(f"Finished downloading {name}")
    except Exception as e:
        print("Error Found!")


# if __name__ == "__main__":
#     url = "https://picsum.photos/2000/3000"
#     pros = []
#     for i in range(50):
#         # downloadFile(url, i)
#         p = multiprocessing.Process(target=downloadFile, args=[url, i])
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()
        
        
if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [i for i in range(60)]
        results = executor.map(downloadFile, l1, l2)
        for result in results:
            print(result)