# encoding: utf-8
# auto clash config file renew prog

# config?You need to fill in the configuration file path
Name="RewnewConfig.yaml"

#data
Folder="Clash"


import os
import requests
import yaml
import time


targetPath = os.getcwd()+ "/" + Name
print("使用配置文件: "+targetPath)


class App(object):
   def __init__(self, C) -> None:
       if not C == "":
         self.count=[]
         self.c = yaml.load(C)
         self.aR=self.c.get('RenewConfig')
         self.target=self.c.get('RenewTargetKey')
         self.content=self.c.get("content")
       else:
         self.c = False
       self.Cpath=os.getcwd()+ "/" +Folder
       folder = os.path.exists(self.Cpath)
       if not folder:
          os.makedirs(self.Cpath)
          print("Create New Folder:" +self.Cpath)

   def run(self):
       if all([self.c,self.aR,self.target,self.content]):
          for k,v in self.content.items():
              self.Worker(k,v)
          self.Finally()
       else:
          print("Error: Argument missing or invalid")
   def Worker(self, A, B):
       try:
          r=requests.get(B[0])
          r.raise_for_status()  #如果不是200，产生异常requests.HTTPError
          r.encoding='utf-8'
          rpath=self.Cpath+'/'+str(A)
          if not os.path.exists(rpath):
            os.makedirs(rpath)
          if len(r.text)>500:
            with open(rpath +"/"+time.strftime("%Y%m%d%H%M%S")+'.yaml', 'w+',encoding='utf-8') as f:
                f.write(r.text)
                f.flush()
                os.fsync(f.fileno())
          else:
            raise ValueError("Content less than 500 words, skip for safety")
       except Exception as e:
          print("Error occur..."+str(e))
       else:
          self.count.append(A)
          if A == self.target:
             try:
                with open(os.getcwd() +"/.config/clash/config.yaml", 'w+',encoding='utf-8') as f:
                   f.write(r.text)
                   f.flush()
                   os.fsync(f.fileno())
             except Exception as e:
                print("Error updating run file "+str(e))

   def Finally(self):
       print("Update completed-"+time.strftime("%Y-%m-%d %H:%M:%S")+" Total:"+str(len(self.content)) + " ,Succesful Renew:"+str(len(self.count)))
       if self.aR:
          print("The running configuration file has been replaced ,use:"+self.target)


# main
try:
    f = open(targetPath, 'r')
except:
    print("IO Error： Pleas Make sure that file really exist!")
else:
    content = f.read()
    f.close()
    time.sleep(10)
    App(content).run()



