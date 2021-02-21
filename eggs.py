'''
Usage:
eggs test
eggs adapt
eggs calamares [install]
eggs config
eggs dad
eggs export [deb|iso|docs]
eggs info
eggs install [--gui]
eggs kill
eggs mom
eggs produce [--prefix=string] [--basename=string] [--fast|--normal|--max] [--theme=string] [--adapt] [--pve] [--rsupport][--final][--script][--yolk]
eggs tools [clean|locales|skel|yolk] [option]
eggs update
eggs -h | --help| --version
'''

import sys
from docopt import docopt
from datetime import datetime

sys.path.append('./commands')
sys.path.append('./classes')

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
from update import update
from utils import Utils


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
    elif args['update']:
        update(args)
    else:
        print(Utils.vmlinuz())
        print(Utils.initrd_img())
        # print("eggs command not found")


if __name__ == '__main__':
    main()
