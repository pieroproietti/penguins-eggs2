
def export(args):
   """
   This command export something
   """
   if args['deb']:
      print("run export deb packages")
   elif args['docs']:
      print("run export sources documents")
   elif args['iso']:
      print("run export iso images")
   else:
      print("You must specific that export")
