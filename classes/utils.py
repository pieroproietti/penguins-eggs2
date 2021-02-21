from bash import bash
import subprocess
import glob
import os
import platform
import filetype
import shlex
from datetime import date, datetime
from colorama import Fore, Back, Style

from pacman import Pacman



class Utils:
    """ Utility generali"""

    @staticmethod
    def bash_exec(cmd) -> str:
        """ return output bash command """
        subprocess = bash(cmd)
        if subprocess.code == 0:
            stdout = subprocess.stdout.decode('utf-8').strip()
        return stdout

    @staticmethod
    def is_systemd() -> bool:
        """ return true if systemd """
        cmd = "/usr/bin/ps -p 1 -o comm="
        result = False
        stdout = Utils.bash_exec(cmd)
        if stdout == "systemd":
            result = True
        return result

    @staticmethod
    def kernerl_version() -> str:
        """ return kernel version """
        return platform.release()

    @staticmethod
    def vmlinuz() -> str:
        """ return path vmlinuz """
        cmd = "cat /proc/cmdline|/usr/bin/cut -f1 -d ' ' |/usr/bin/cut -f2 -d '='"
        result = Utils.bash_exec(cmd)
        return result

    @staticmethod
    def initrd_img():
        """ return path to initrdimg """
        vmlinuz = Utils.vmlinuz()
        path = vmlinuz[0: vmlinuz.rfind('/')] + "/"
        version = vmlinuz[vmlinuz.find('-'):]
        result = path + 'initrd.img' + version
        return result

    @staticmethod
    def get_primary_user() -> str:
        """ retrieve primary username """
        cmd = 'whoami'
        result = Utils.bash_exec(cmd)
        return result

    @staticmethod
    def get_author_name() -> str:
        """ just a thing """
        return "Piero Proietti piero.proietti@gmail.com"


    @staticmethod
    def uuid(device="/dev/sda1") -> str:
        """ return device uuid  """
        output = Utils.bash_exec("/usr/sbin/blkid -s UUID -o value " + device)
        return output

    @staticmethod
    def get_package_name():
        return "eggs"

    @staticmethod
    def get_snapshot_count(snapshot_dir='.'):
        """ return number of existing snapshot """
        result = len(glob.glob(snapshot_dir + '/*.iso'))
        return result

    @staticmethod
    def get_snapshot_size(snapshot_dir='.') -> int:
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

    @staticmethod
    def get_filename(basename='') -> str:
        """ return name iso file """
        arch = platform.machine()
        if arch == 'x86_64':
            arch = 'x64'
        now = datetime.now()
        iso_name = basename + '-' + arch + '_' + now.strftime("%Y-%m-%d_%H%M")
        if len(iso_name) >= 20:
            iso_name = iso_name[0:28]

        iso_name += '.iso'
        return iso_name

    @staticmethod
    def get_used_space() -> int:
        """ return used space in the disk  """
        import psutil

        result = psutil.disk_usage('/').used
        return result

    @staticmethod
    def get_live_space(type='debian-live') -> float:
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

    @staticmethod
    def is686() -> bool:
        """ return True if 386 """
        arch = platform.machine()
        if arch == 'i386':
            return True

    @staticmethod
    def is_uefi() -> bool:
        """ return True if uefi system """
        result = False
        arch = platform.machine()
        if arch == 'x86_64':
            if Pacman.is_installed('grub-efi-amd64'):
                result = True

        return result


    @staticmethod
    def is_deb_package() -> bool:
        """ eggs2 is alwayays installed as deb"""
        return True

    @staticmethod
    def is_sources() -> bool:
        """ eggs2 is alwayays installed as deb"""
        return False

    @staticmethod
    def root_penguins():
        """ return eggs root """
        return __dirname

    @staticmethod
    def get_friend_name() -> str:
        """ just a thing """
        return "eggs"

    @staticmethod
    def get_package_version():
        """ just a thing """
        return "0.0.1"

    @staticmethod
    def get_debian_version() -> str:
        """ return debian version: 9, 10, 11 """
        cmd = "cat /etc/debian_version|/usr/bin/cut -f1 -d'.'"
        stdout = Utils.bash_exec(cmd)
        return stdout

    @staticmethod
    def is_live() -> bool:
        """ return True on live system """
        result = False
        paths = ['/lib/live/mount',  # debian-live
                 '/lib/live/mount/rootfs/filesystem.squashfs',  # ubuntu bionic
                 '/live/aufs'  # mx-linux
                 ]
        for path in paths:
            if Utils.is_mountpoint(path):
                result = True

        return result

    @staticmethod
    def is_mountpoint(path='') -> bool:
        """ return True if path is a mountpoint """
        result = False
        stdout = Utils.bash_exec("mountpoint -q " + path)
        if stdout == '0':
            result = True
        return result

    @staticmethod
    def is_root(command='nada') -> bool:
        """ return True if eggs run with root privileges """
        result = True
        if os.geteuid() != 0:
            result = False
            Utils.warning(
                command + ', need to run with root privileges. Please, prefix it with sudo')

        return result

    @staticmethod
    def warning(msg='') -> None:
        """ Emit a warning message """
        print('eggs >>> ' + Fore.CYAN + msg + Style.RESET_ALL + '.')

    @staticmethod
    def error(msg='') -> None:
        """ emit an error message  """
        print('eggs >>> ' + Fore.RED + msg + Style.RESET_ALL + '.')
