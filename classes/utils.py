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
      bashCmd1 = "cat /proc/cmdline"
      bashCmd2 = "/usr/bin/cut -f1 -d ' '"
      bashCmd3 = "/usr/bin/cut -f2 -d ="

      #bashCommand ="cat /proc/cmdline|/usr/bin/cut -f1 -d ' ' |/usr/bin/cut -f2 -d '='"
      output1 = subprocess.Popen(bashCmd1.split(), stdout=subprocess.PIPE)
      print('output1')
      print(output1.stdout)
      print('output2')
      output2 = subprocess.Popen(bashCmd2.split(), stdout=subprocess.PIPE, stdin=output1.stdout)
      print('output3')
      print(output2.stdout)
      output3 = subprocess.Popen(bashCmd3.split(), stdout=subprocess.PIPE, stdin=output2.stdout) 
      print(output3.stdout)
      return output3