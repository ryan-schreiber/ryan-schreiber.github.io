
import os, time, datetime


flags = {
  "southwest-china" : datetime.datetime(2020, 2, 8, 8, 50, 0),
  "germany" : datetime.datetime(2020, 2, 8, 10, 30, 0),
  "slovenia" : datetime.datetime(2020, 2, 8, 12, 15, 0),
  "ghana" : datetime.datetime(2020, 2, 8, 14, 45, 0),
  "peru" : datetime.datetime(2020, 2, 8, 18, 0, 0),
  "china" : datetime.datetime(2020, 2, 8, 20, 0, 0),
  "done" : datetime.datetime(2020, 2, 8, 22, 0, 0),
}

pages = {
  "southwest-china" : "1.html",
  "germany" : "2.html",
  "slovenia" : "3.html",
  "ghana" : "4.html",
  "peru" : "5.html",
  "china" : "6.html",
  "done" : "7.html",
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


