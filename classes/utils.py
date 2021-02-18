import subprocess

class Utils:
 
   def isSystemd(self):
      bashCommand = "/usr/bin/ps -p 1 -o comm="
      process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
      output = process.stdout.read() # .communicate()
      systemd = False
      if output == 'systemd\n':
         systemd = True
 
      return systemd
   

   def ls(self):
      bashCommand = "ls ."
      process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
      output = process.communicate()
      return output
