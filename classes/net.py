import netifaces
import socket

class Net:
    """ Utils net"""

    @staticmethod
    def net_device_name() -> str:
        """ return net_device_name """
        x = netifaces.interfaces()
        for i in x:
            if i != 'lo':
                result: str = i

        return result

    @staticmethod
    def net_address() -> str:
        
        hostname: str = socket.getfqdn()
        local_ip: str = socket.gethostbyname(hostname)
        return local_ip

    @staticmethod
    def net_mask(iface='vmbr0') :
        """ return the netmask """
     
        import fcntl
        import struct

        result = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', iface))[20:24])

        return result

    @staticmethod
    def net_dns() -> str:
        return "192.168.61.1"
