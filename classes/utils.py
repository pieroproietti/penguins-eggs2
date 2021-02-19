import subprocess
import glob
import os
import platform
import filetype
import socket
import netifaces

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

    def getLiveRootSpace(type='debian-live'):
        squashFs = '/run/live/medium/live/filesystem.squashfs'
        if (type == 'mx'):
            squashFs = '/live/boot-dev/antiX/linuxfs'

        if os.path.exists(squashFs):
            result = os.path.getsize(squashFs)
            # kind = filetype.guess(squashFs)

        else:
            result = 0

        return result

    def is696(self):
        """ ritorna vero se 386"""
        arch = platform.machine()
        if arch == 'i386':
            return True

    def isUefi(self):
        """ Ritorna vero se uefi"""
        result = False
        arch = platform.machine()
        if arch == 'x86_64':
            if self.isInstalled('grub-efi-amd64'):
                result = True

        return result

    def isInstalled(self, debPackage):
        """ Ritorna vero se il pacchetto  installato """
        bashCmd1 = "/usr/bin/dpkg -s " + debPackage
        bashCmd2 = "grep Status"
        process1 = subprocess.Popen(
            shlex.split(bashCmd1), stdout=subprocess.PIPE)
        process2 = subprocess.Popen(
            shlex.split(bashCmd2), stdin=process1.stdout, stdout=subprocess.PIPE)

        output = process2.stdout.read()

        result = False
        if output == 'Status: install ok installed\n':
            result = True
        return result

    def isDebPackage(self):
        return True

    def isSources(self):
        return False

    def rootPenguins(self):
        return __dirname

    def getFriendName(self):
        return "eggs"

    def getPackageVersion(self):
        return "0.0.1"

    def getAuthorName(self):
        return "Piero Proietti piero.proietti@gmail.com"

    def getDebianVersion(self):
        bashCmd1 = "cat /etc/debian_version"
        bashCmd2 = "/usr/bin/cut -f1 -d'.'"
        process1 = subprocess.Popen(
            shlex.split(bashCmd1), stdout=subprocess.PIPE)

        process2 = subprocess.Popen(
            shlex.split(bashCmd2), stdin=process1.stdout, stdout=subprocess.PIPE)
        output = process2.stdout.read()
        return output

    def isLive(self):
      """ Ritorna vero se e una live """
      result= False
      paths = ['/lib/live/mount', # debian-live
              '/lib/live/mount/rootfs/filesystem.squashfs', # ubuntu bionic
              '/live/aufs' # mx-linux
              ]
      for path in paths:
        if self.isMountpoint(path):
          result=True

      return result

    def isMountpoint(self, path = ''):
      bashCmd = "mountpoint -q " + path
      output = self.bashExec(bashCmd)
      result = False
      if output == '0\n':
        result = True
      return result

    def isRoot(self, command='nada'):
      result = True
      if os.geteuid() != 0:
        result = False
        self.warning(command +', need to run with root privileges. Please, prefix it with sudo')

      return result

    def kernerlVersion(self):
      return platform.release()
    
    def netDeviceName(self)->str :
      x = netifaces.interfaces()
      for i in x:
        if i != 'lo':
          result: str = i

      return result

    def netAddress(self) ->str:
      hostname: str = socket.gethostname()
      local_ip: str = socket.gethostbyname(hostname)
      return local_ip

    def netMask(self, iface='vmbr0'):
      """ return the netmask """
      import fcntl
      import struct

      result: str = "" #socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', iface))[20:24])
      return result

    def netDns(self):
      return "192.168.61.1"

