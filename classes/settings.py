
import os
config_file = '/etc/penguins-eggs.d/eggs.yaml'

class Settings:
    # Dict
    app = {
        author: "",
        homepage: "",
        mail: "",
        name: "",
        version: ""
    }

    # Dict
    config = {
        version: "",
        snapshot_dir: "",
        snapshot_basename: "",
        snapshot_prefix: "",
        snapshot_excludes: "",
        user_opt: "",
        user_opt_passwd: "",
        root_passwd: "",
        theme: "",
        force_installer: False,
        make_efi: False,
        make_md5sum: False,
        make_isohybrid: False,
        compression: False,
        ssh_pass: False,
        timezone: "",
        # List
        locales: [""],
        locales_default: "",
        pmount_fixed: False,
        netconfig_opt: "",
        ifnames_opt: "",
    }

    # Dict remix
    remix = {
        name: "",
        branding:  "",
        version_name: "",
        version_number: "",
        kernel: "",
        path_home: "",
        lowerdir: "",
        upperdir: "",
        workdir: "",
        merged: "",
        path_iso: "",
    }

    # Dict workdir
    workdir = {
        path: "",
        path_iso: "",
        lowerdir: "",
        upperdir: "",
        workdir: "",
        merged: "",
    }

    distro = {
        id: "",
        like: "",
        version_id: "",
        version_like: "",
        isolinux_path: "",
        syslinux_path: "",
        mountpoint: "",
        url_home: "",
        url_support: "",
        url_bugreport: ""
    }

    incubator = "" # Incubator

    i686 = false
    isLive = false
    efi_work = ''
    kernel_image = ''
    initrd_image = ''
    vmlinuz = ''
    initrdImg = ''
    session_excludes = ''
    isoFilename = ''

    def __init__(self, compressions="xz"):
        """ constructor """
        self.compression = compression

        self.app.author = 'Piero Proietti'
        self.app.homepage = 'https://github.com/pieroproietti/penguins-eggs'
        self.app.mail = 'piero.proietti@gmail.com'
        self.app.name = pjson.name as string
        self.app.version = pjson.version
        self.isLive = Utils.isLive()
        self.i686 = Utils.isi686()
        self.distro = new Distro(this.remix)

    def load(self):
        foundSettings = True
        if (!os.path.exists(self.config_file)):
            print("cannot find configuration file {self.config_file},")
            print("please generate it with: sudo eggs prerequisites.")
            raise config_not_found("cannot find configuation file")

        self.config = 
        

      this.config = yaml.load(fs.readFileSync(config_file, 'utf-8')) as IConfig

      self.session_excludes = ''
      if (!this.config.snapshot_dir.endsWith('/')) {
         this.config.snapshot_dir += '/'
      }
      self.work_dir.path = this.config.snapshot_dir + 'ovarium/'
      this.work_dir.lowerdir = this.work_dir.path + '.overlay/lowerdir'
      this.work_dir.upperdir = this.work_dir.path + '.overlay/upperdir'
      this.work_dir.workdir = this.work_dir.path + '.overlay/workdir'
      this.work_dir.merged = this.work_dir.path + 'filesystem.squashfs'

      this.efi_work = this.work_dir.path + 'efi/'
      this.work_dir.pathIso = this.work_dir.path + 'iso'

      if (this.config.snapshot_basename === 'hostname') {
         this.config.snapshot_basename = os.hostname()
      }
      if (this.config.make_efi) {
         if (!Utils.isUefi()) {
            Utils.error('You choose to create an UEFI image, but miss to install grub-efi-amd64 package.')
            Utils.error('Please install it before to create an UEFI image:')
            Utils.warning('sudo apt install grub-efi-amd64')
            Utils.error('or edit /etc/penguins-eggs.d/eggs.yaml and set the valuer of make_efi = false')
            this.config.make_efi = false
         }
      }

      this.kernel_image = Utils.vmlinuz()
      this.initrd_image = Utils.initrdImg()
      this.vmlinuz = this.kernel_image.substr(this.kernel_image.lastIndexOf('/'))
      this.initrdImg = this.initrd_image.substr(this.initrd_image.lastIndexOf('/'))


      /**
       * Use the login name set in the config file. If not set, use the primary
       * user's name. If the name is not "user" then add boot option. ALso use
       * the same username for cleaning geany history.
       */

      if (this.config.user_opt === undefined || this.config.user_opt === '') {
         // this.user_opt = shx.exec('awk -F":" \'/1000:1000/ { print $1 }\' /etc/passwd', { silent: true }).stdout.trim()
         if (this.config.user_opt === '') {
            this.config.user_opt = 'live'
         }
      }
      if (this.config.user_opt_passwd === '') {
         this.config.user_opt_passwd = 'evolution'
      }

      if (this.config.root_passwd === '') {
         this.config.root_passwd = 'evolution'
      }

      if (this.config.timezone === undefined || this.config.timezone === '') {
         this.config.timezone = shx.exec('cat /etc/timezone', { silent: true }).stdout.trim()
      }


      return foundSettings
