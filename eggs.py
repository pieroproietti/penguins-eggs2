'''
Usage:
eggs adapt [options]
eggs calamares [install]
eggs config [options]
eggs dad
eggs export [deb| iso| docs]
eggs info 
eggs install [--gui]
eggs kill [options]
eggs mom 
eggs produce [--basename=string], [--fast|--normal|--max],[--theme=string],[--pve],[--rsupport]
eggs tools [clean|locales|skel|yolk] [option]
eggs update [options]
eggs -h | --help| --version   
'''

import sys
from docopt import docopt

sys.path.append('./commands')
from adapt import adapt
from calamares import calamares
from config import config
from dad import dad
from export import export
from info import info
from install import install
from kill import kill
from mom import mom

def main():
   args = docopt(__doc__)

   if args['adapt']:
      adapt(args)
   elif args['calamares']:
      calamares(args)
   elif args['config']:
      config(args)
   elif args['dad']:
      dad(args)
   elif args['export']:
      export(args)
   elif args['info']:
      info(args)
   elif args['install']:
      install(args)
   elif args['kill']:
      kill(args)
   elif args['mom']:
      mom(args)
   else:
      print("command not found")

if __name__=='__main__':
   main()
