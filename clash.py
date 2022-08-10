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
         self.NotifyOrNot=self.c.get("RenewNotify")
       else:
         self.c = False
       self.Cpath=os.getcwd()+ "/" +Folder
       folder = os.path.exists(self.Cpath)
       if not folder:
          os.makedirs(self.Cpath)
          print("Create New Folder:" +self.Cpath)
   def sendNotify(self,infoo,prt=False):
      print(infoo)
      if self.NotifyOrNot and not prt:
         import notify2
         notify2.init('ClashRenew')
         n = notify2.Notification('ClashRenew', infoo)
         n.show()
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
          self.sendNotify("Error occur:\n"+str(e))
       else:
          self.count.append(A)
          if A == self.target:
             try:
                with open(os.getcwd() +"/.config/clash/config.yaml", 'w+',encoding='utf-8') as f:
                   f.write(r.text)
                   f.flush()
                   os.fsync(f.fileno())
             except Exception as e:
                self.sendNotify("Error updating run file "+str(e))

   def Finally(self):
       info=("Update completed-"+time.strftime("%Y-%m-%d %H:%M:%S")+" Total:"+str(len(self.content)) + " ,Succesful Renew:"+str(len(self.count)))
       #self.sendNotify(info,prt=True)
       if self.aR:
          info2=("The running configuration file has been replaced ,use:"+self.target)
          infos="Use config:"+targetPath+"\n"+info+"\n"+info2
       else:
          infos="Use config:"+targetPath+"\n"+info
       self.sendNotify(infos)


# main
try:
    f = open(targetPath, 'r')
except Exception as e:
    App("").sendNotify(e)
else:
    content = f.read()
    f.close()
    time.sleep(12)
    App(content).run()


