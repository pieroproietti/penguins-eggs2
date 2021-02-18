def tools(args):
    if args['clean']:
        print('eggs tools clean')
    elif args['locales']:
        print('eggs tools locales')
    elif args['skel']:
        print('eggs tools skel')
    elif args['yolk']:
        print('eggs tools yolk')
    else:
        print('no tool')

