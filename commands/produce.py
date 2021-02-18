def produce(args):
   if args['--basename']!='':
      basename=args['--basename']
      print('basename: ' + basename)

   if args['--fast']:
      compression = 'lz4'
   elif args['--max']:
      compression = 'xz -Xbcj x86'
   else:
      compression = 'xz'

   if args['--theme']!='':
      theme=args['--theme']
   else:
      theme='eggs'

   if args['--prefix']!='':
      prefix = args['--prefix']
   else:
      prefix=''

   option=''
   if args['--pve']:
      option +='--pve'

   if args['--adapt']:
      option +='--adapt'

   if args['--rsupport']:
      option +='--rsupport'

   if args['--final']:
      option +='--final'

   if args['--script']:
      option +='--script'

   if args['--yolk']:
      option +='--yolk'


   print('produce iso')
