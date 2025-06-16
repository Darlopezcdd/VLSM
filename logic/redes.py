from logic.ip import Ip
class Red:
    def __init__(self, nombre, cantidad_hosts,hostsnesesarios=None,ip=None):
        self.nombre = nombre
        self.cantidad_hosts = cantidad_hosts
        self.ip = ip
        self.hostsnesesarios = hostsnesesarios
    def __str__(self):
        return f"Red: {self.nombre}, Hosts: {self.cantidad_hosts}, IP: {self.ip}"

    def asignar_ip(self, ip):
        if ip is not None:
            self.ip = ip
        else:
            print("no tiene una IP asignada.")
            self.ip = Ip(0, 0, 0, 0, 0)

    def calcular_hostsnesesarios(self):
        num = 0
        for i in range(32):
            posibles_hosts = (2 ** i) - 2
            if posibles_hosts >= self.cantidad_hosts:
                num = posibles_hosts
                break
        self.hostsnesesarios = num
