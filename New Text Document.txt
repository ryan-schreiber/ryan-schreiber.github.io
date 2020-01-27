
import os, time, datetime


flags = {
  "southwest-china" : datetime.datetime(2020, 1, 26, 15, 47, 0),
  "germany" : datetime.datetime(2020, 1, 26, 15, 48, 30),
  "slovenia" : datetime.datetime(2020, 1, 26, 15, 49, 30),
  "ghana" : datetime.datetime(2020, 1, 26, 15, 50, 30),
  "peru" : datetime.datetime(2020, 1, 26, 15, 51, 30),
  "china" : datetime.datetime(2020, 1, 26, 15, 52, 30),
}

pages = {
  "southwest-china" : "1.html",
  "germany" : "2.html",
  "slovenia" : "3.html",
  "ghana" : "4.html",
  "peru" : "5.html",
  "china" : "6.html",
}

while True:
  if len(flags.keys()) == 0:
    break
  for flag in list(flags.keys()):
    if flags[flag] < datetime.datetime.now():
      flags.pop(flag)
      with open("index.html","w") as i:
        with open(pages[flag], "r") as p:
          i.write(p.read())
      command = """git add . & git commit -m "Push from the main.py scheduler" & git push"""
      os.system(command)
      print("Popped " + flag)
  time.sleep(2)
  
print("Done")


'''

command = """git add . & git commit -m "Push from the main.py scheduler" & git push"""
os.system(command)
'''


