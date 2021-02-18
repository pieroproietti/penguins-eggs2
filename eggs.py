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
eggs produce [--prefix=string] [--basename=string] [--fast|--normal|--max] [--theme=string] [--adapt] [--pve] [--rsupport][--final][--script][--yolk]
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
from produce import produce
from tools import tools

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
   elif args['produce']:
      produce(args)
   elif args['tools']:
      tools(args)
   else:
      print("command not found")

if __name__=='__main__':
   main()
