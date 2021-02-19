import subprocess
import shlex
from datetime import date 

from colorama import Fore, Back, Style


class Utils:

   def isSystemd(self):
      output = self.bashExec("/usr/bin/ps -p 1 -o comm=")
      systemd = False
      if output == 'systemd\n':
         systemd = True

      return systemd

   def vmlinuz(self):
      """Ritorna il path di vmlinuz"""
      bashCmd1 = shlex.split("cat /proc/cmdline")
      bashCmd2 = shlex.split("/usr/bin/cut -f1 -d ' '")
      bashCmd3 = shlex.split("/usr/bin/cut -f2 -d =")

      # pipe di comandi
      process1 = subprocess.Popen(bashCmd1, stdout=subprocess.PIPE)
      process2 = subprocess.Popen(
          bashCmd2, stdin=process1.stdout, stdout=subprocess.PIPE)
      process3 = subprocess.Popen(
          bashCmd3, stdin=process2.stdout, stdout=subprocess.PIPE)
      result = process3.stdout.read()
      return result

   def initrdImg(self):
      """Ritorna il path per initrdImg"""
      vmlinuz = self.vmlinuz()
      path = vmlinuz[0: vmlinuz.rfind('/')] + '/'
      version = vmlinuz[vmlinuz.find('-'):]
      result = path + 'initrd.img' + version
      return result

   def warning(self, msg=''):
      """ Emette un messaggio di warning """
      print('eggs >>> ' + Fore.CYAN + msg + Style.RESET_ALL + '.')

   def error(self, msg=''):
      """ Emette un messaggio di errore """
      print('eggs >>> ' + Fore.RED + msg + Style.RESET_ALL + '.')

   def getPrimaryUser(self):
      # bashCommand = "echo $SUDO_USER"
      output = self.bashExec("/usr/bin/whoami")
      return output

   def uuid(self, device="/dev/sda1"):
      """ Ritorna uuid del device """
      output = self.bashExec("/usr/sbin/blkid -s UUID -o value " + device)
      return output

   def bashExec(self, cmd):
      """ Ritorna output del comando """
      process = subprocess.Popen(shlex.split(
          cmd), stdout=subprocess.PIPE)
      output = process.stdout.read()
      return output
   
   def formatDate(self, date):
      """ ritorna la stringa della data """
      return date.strftime("%Y-%m-%d_%H%M")

