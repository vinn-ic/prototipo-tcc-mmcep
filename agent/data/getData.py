
import psutil

import platform
import os

from datetime import datetime, timezone

disk = psutil.disk_usage('/')
pcName = platform.node()
userName = os.getlogin()

def getDataForJson():
   men = psutil.virtual_memory()
   
   print("puxando dados para json")
   data = {
      "pcName": pcName,
      "totalMen": (men.total) / 1024**3,
      "totalDisk": (disk.total) / 1024**3,
    }   
   return data



def getlastPidName():
   p = psutil.Process()
   tmpP1 = 0.0
   nameP1 = None
   
   for proc in psutil.process_iter(['pid', 'name', 'username', 'create_time']):
      
      if tmpP1 <= proc.info['create_time']:
         nameP1 = proc.info['name']
         tmpP1 = proc.info['create_time']
      else:
         pass
   
   return nameP1


def getDataForTeacher():
   men = psutil.virtual_memory()
   
   tmpStart = datetime.now(timezone.utc) - datetime.fromtimestamp(psutil.boot_time(), timezone.utc)

   pidNameLast = getlastPidName()
   menUsed = men.used
   cpu_percent = psutil.cpu_percent(interval=1)




   data = {
      'pcName': pcName,
      'tmpBoot': str(tmpStart),
      'pidNameLast': pidNameLast,
      'menUsed': (menUsed) / 1024**3,
      'cpu_percent': cpu_percent
   }

   return data



if __name__ == "__main__":
   print(getDataForTeacher())