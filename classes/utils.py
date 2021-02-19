import subprocess
import glob
import os
import platform

import shlex
from datetime import date, datetime

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

    def getPackageName(self):
        return "eggs"

    def getSnapshotCount(self, snapshot_dir='.'):
        """ ritorna il numero degli snapshot esistenti """
        result = len(glob.glob(snapshot_dir + '/*.iso'))
        return result

    def getSnapshotSize(self, snapshot_dir='.'):
        """ ritorna il size degli snapshot"""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(snapshot_dir):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    if fp.endswith('.iso'):
                        total_size += os.path.getsize(fp)
        return total_size

    def getFilename(self, basename=''):
        """ Ritorna il nome del file iso """

        arch = platform.machine()
        if arch == 'x86_64':
            arch = 'x64'

        isoName = basename + '-' + arch + '_' + self.formatDate(datetime.now())
        print(isoName)
        if len(isoName) >= 20:
            isoName = isoName[0:28]

        isoName += '.iso'
        return isoName

    def getUsedSpace(self):
       """ ritorna lo spazio occupato nel disco """
       import psutil
 
       result = psutil.disk_usage('/').used
       return result

    getLiveRootSpace(type = 'debian-live'):
      squashFs = '/run/live/medium/live/filesystem.squashfs'
      if (type === 'mx') {
         squashFs = '/live/boot-dev/antiX/linuxfs'
      }
      result os.path.getsize(squashFs)
      return result