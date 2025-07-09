import time

name = input("Enter your name : ")
n = name.capitalize()
print(time.strftime('%H:%M:%S'))
recenttime = time.strftime('%H:%M:%S')
hournow = int(time.strftime('%H'))
if(4<=hournow<12):
    print('GOOD MORNING ',n,' its ',recenttime)
elif(12<=hournow<17):
    print('GOOD EVENING ',n,' its ',recenttime)
else:
    print('GOOD NIGHT ',n,' its ',recenttime)



# # print('Hii',name,'its',recenttime)
# # Morning Time : 04:00:00 to 11:59:59
# # Afternoon Time : 12:00:00 to 16:59:59
# # Evening Time : 17:00:00 to 20:59:59
# # Night Time : 21:00:00 to 03:59:59