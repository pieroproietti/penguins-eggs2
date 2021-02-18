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
   

   def vmlinuz(self):
      bashCommand ="cat /proc/cmdline|/usr/bin/cut -f1 -d ' ' |/usr/bin/cut -f2 -d '='"
      process = subprocess.Popen(bashCommand.split(), shell=False, stdout=subprocess.PIPE)
      output = process.stdout.read() 
      return output
