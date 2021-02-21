from bash import bash



class Pacman:
    """ gestione dei pacchetti """

    @staticmethod
    def bash_exec(cmd) -> str:
        """ return output bash command """
        subprocess = bash(cmd)
        if subprocess.code == 0:
            stdout = subprocess.stdout.decode('utf-8').strip()
        return stdout

    @staticmethod
    def is_installed(deb_package) -> bool:
        """ return True if deb_package is installaed """
        cmd = "/usr/bin/dpkg -s " + deb_package + "|grep Status"
        stdout = Pacman.bash_exec(cmd)
        result = False
        if stdout == 'Status: install ok installed':
            result = True
        return result
