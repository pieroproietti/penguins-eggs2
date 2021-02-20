import subprocess
import glob
import os
import platform
# import filetype
import socket
import netifaces
import shlex
# from datetime import date, datetime
from colorama import Fore, Back, Style


class Utils:
    """ Utility generali"""

    def is_systemd(self) -> bool:
        """ return true if systemd """
        output = self.bashExec("/usr/bin/ps -p 1 -o comm=")
        result = False
        if output == 'systemd\n':
            result = True
        return result

    def vmlinuz(self) -> str:
        """ return path vmlinuz """
        bash_cmd1 = shlex.split("cat /proc/cmdline")
        bash_cmd2 = shlex.split("/usr/bin/cut -f1 -d ' '")
        bash_cmd3 = shlex.split("/usr/bin/cut -f2 -d =")

        # pipe di comandi
        process1 = subprocess.Popen(bash_cmd1, stdout=subprocess.PIPE)
        process2 = subprocess.Popen(
            bash_cmd2, stdin=process1.stdout, stdout=subprocess.PIPE)
        process3 = subprocess.Popen(
            bash_cmd3, stdin=process2.stdout, stdout=subprocess.PIPE)
        result = process3.stdout.read()
        return result

    def initrd_img(self):
        """ return path to initrdimg """
        vmlinuz = self.vmlinuz()
        path = vmlinuz[0: vmlinuz.rfind('/')] + "/"
        version = vmlinuz[vmlinuz.find('-'):]
        result = path + 'initrd.img' + version
        return result

    def warning(self, msg='') -> None:
        """ Emit a warning message """
        print('eggs >>> ' + Fore.CYAN + msg + Style.RESET_ALL + '.')

    def error(self, msg='') -> None:
        """ emit an error message  """
        print('eggs >>> ' + Fore.RED + msg + Style.RESET_ALL + '.')

    def get_primary_user(self) -> str:
        """ retrieve primary username """
        # bashCommand = "echo $SUDO_USER"
        output = self.bashExec("/usr/bin/whoami")
        return output

    def uuid(self, device="/dev/sda1") -> str:
        """ return device uuid  """
        output = self.bash_exec("/usr/sbin/blkid -s UUID -o value " + device)
        return output

    def bash_exec(self, cmd) -> str:
        """ return output bash command """
        process = subprocess.Popen(shlex.split(
            cmd), stdout=subprocess.PIPE)
        output = process.stdout.read()
        return output

    def format_date(self, date) -> str:
        """ return data as string  """
        return date.strftime("%Y-%m-%d_%H%M")

    def get_package_name(self):
        return "eggs"

    def get_snapshot_count(self, snapshot_dir='.'):
        """ return number of existing snapshot """
        result = len(glob.glob(snapshot_dir + '/*.iso'))
        return result

    def get_snapshot_size(self, snapshot_dir='.'):
        """ return size existing snapshot """
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(snapshot_dir):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    if fp.endswith('.iso'):
                        total_size += os.path.getsize(fp)
        return total_size

    def get_filename(self, basename='') -> str:
        """ return name iso file """
        arch = platform.machine()
        if arch == 'x86_64':
            arch = 'x64'
        now = datatime.now()
        iso_name = basename + '-' + arch + '_' + now.strftime("%Y-%m-%d_%H%M")
        if len(iso_name) >= 20:
            iso_name = isoname[0:28]

        iso_name += '.iso'
        return iso_name

    def get_used_space(self):
        """ return used space in the disk  """
        import psutil

        result = psutil.disk_usage('/').used
        return result

    def get_live_space(type='debian-live'):
        """ return extimated space used for the live systeme"""
        squashFs = '/run/live/medium/live/filesystem.squashfs'
        if (type == 'mx'):
            squashFs = '/live/boot-dev/antiX/linuxfs'

        if os.path.exists(squashFs):
            result = os.path.getsize(squashFs)
            # kind = filetype.guess(squashFs)

        else:
            result = 0.0

        return result

    def is686(self) -> bool:
        """ return True if 386 """
        arch = platform.machine()
        if arch == 'i386':
            return True

    def is_uefi(self) -> bool:
        """ return True if uefi system """
        result = False
        arch = platform.machine()
        if arch == 'x86_64':
            if self.isInstalled('grub-efi-amd64'):
                result = True

        return result

    def is_installed(self, deb_package) -> bool:
        """ return True if deb_package is installaed """
        bash_cmd1 = "/usr/bin/dpkg -s " + deb_package
        bash_cmd2 = "grep Status"
        process1 = subprocess.Popen(
            shlex.split(bash_cmd1), stdout=subprocess.PIPE)
        process2 = subprocess.Popen(
            shlex.split(bash_cmd2), stdin=process1.stdout, stdout=subprocess.PIPE)

        output = process2.stdout.read()

        result = False
        if output == 'Status: install ok installed\n':
            result = True
        return result

    def is_deb_package(self) -> bool:
        """ eggs2 is alwayays installed as deb"""
        return True

    def is_sources(self) -> bool:
        """ eggs2 is alwayays installed as deb"""
        return False

    def root_penguins(self):
        """ return eggs root """
        return __dirname

    def get_friend_name(self) -> str:
        """ just a thing """
        return "eggs"

    def get_package_version(self):
        """ just a thing """
        return "0.0.1"

    def get_author_name(self) -> str:
        """ just a thing """
        return "Piero Proietti piero.proietti@gmail.com"

    def get_debian_version(self) -> str:
        """ return debian version: 9, 10, 11 """
        bash_cmd1 = "cat /etc/debian_version"
        bash_cmd2 = "/usr/bin/cut -f1 -d'.'"
        process1 = subprocess.Popen(
            shlex.split(bash_cmd1), stdout=subprocess.PIPE)

        process2 = subprocess.Popen(
            shlex.split(bash_cmd2), stdin=process1.stdout, stdout=subprocess.PIPE)
        output = process2.stdout.read()
        return output

    def is_live(self) -> bool:
        """ return True on live system """
        result = False
        paths = ['/lib/live/mount',  # debian-live
                 '/lib/live/mount/rootfs/filesystem.squashfs',  # ubuntu bionic
                 '/live/aufs'  # mx-linux
                 ]
        for path in paths:
            if self.isMountpoint(path):
                result = True

        return result

    def is_mountpoint(self, path='') -> boot:
        """ return True if path is a mountpoint """
        output = self.bashExec("mountpoint -q " + path)
        result = False
        if output == '0\n':
            result = True
        return result

    def is_root(self, command='nada') -> bool:
        """ return True if eggs run with root privileges """
        result = True
        if os.geteuid() != 0:
            result = False
            self.warning(command + ', need to run with root privileges. Please, prefix it with sudo')

        return result

    def kernerl_version(self) -> str:
        """ return kernel version """
        return platform.release()

    def net_device_name(self) -> str:
        """ return net_device_name """
        x = netifaces.interfaces()
        for i in x:
            if i != 'lo':
                result: str = i

        return result

    def net_address(self) -> str:
        hostname: str = socket.gethostname()
        local_ip: str = socket.gethostbyname(hostname)
        return local_ip

    def net_mask(self, iface='vmbr0') -> str:
        """ return the netmask """
        import fcntl
        import struct

        result: str = ""  # socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', iface))[20:24])
        return result

    def net_dns(self) -> str:
        return "192.168.61.1"
