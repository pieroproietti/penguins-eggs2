import subprocess
class Utils:

   def vmlinuz:
      """
      Return the vmlinuz name 
      """
      result = subprocess.run(`cat /proc/cmdline|/usr/bin/cut -f1 -d ' ' |/usr/bin/cut -f2 -d '='`, stdout=subprocess.PIPE)
      return result.stdout
