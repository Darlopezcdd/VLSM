from importlib.resources import open_binary

from logic.ip import Ip
from logic.redes import Red


class vlcm:
    def __init__(self, ip_objeto, redes_info):
        self.ip_objeto = ip_objeto
        self.redes_info = redes_info




    def organizar_redes(self):
        redes= self.redes_info
        for i in range(len(redes)):
            for j in range(len(redes) - 1):
                if redes[j].cantidad_hosts < redes[j + 1].cantidad_hosts:
                    redes[j], redes[j + 1] = redes[j + 1], redes[j]






    def vlcm(self):
        proceso = []

        lengredes = len(self.redes_info)
        chostip = self.ip_objeto.cantidad_hosts()

        self.redes_info[0].calcular_hostsnesesarios()

        chostsred = self.redes_info[0].hostsnesesarios
        if lengredes ==1 and chostip == chostsred:
            self.redes_info[0].asignar_ip(self.ip_objeto)
            proceso.append(self.ip_objeto.__str__() + "→" + self.redes_info[0].nombre)
            return proceso

        if not self.verificarVlcm():
            return "No hay suficientes direcciones IP para dividir entre todas las redes."

        redeslibres = []
        self.organizar_redes()

        ipa = self.ip_objeto.ip_redDecimal()
        ippadre = Ip(ipa[0], ipa[1], ipa[2], ipa[3], self.ip_objeto.mascara)

        iredes = 0
        Ipb = ippadre


        while self.redessinip():
            proceso.append(Ipb.__str__())
            rede = self.redes_info[iredes]
            rede.calcular_hostsnesesarios()

            ipdivi = self.dividirips(Ipb)

            if len(ipdivi) >= 2:

                if ipdivi[0].cantidad_hosts() == rede.hostsnesesarios and self.verificar_ips(ipdivi[0]):
                    self.redes_info[iredes].asignar_ip(ipdivi[0])
                    iredes += 1
                    Ipb = ipdivi[1]
                    proceso.append(ipdivi[0].__str__() + "→" + rede.nombre)
                elif ipdivi[0].cantidad_hosts() > rede.hostsnesesarios and self.verificar_ips(ipdivi[0]):
                    Ipb = ipdivi[0]
                    redeslibres.append(ipdivi[1])
                    continue

                if iredes < len(self.redes_info):
                    rede = self.redes_info[iredes]
                    rede.calcular_hostsnesesarios()

                    if ipdivi[1].cantidad_hosts() == rede.hostsnesesarios and self.verificar_ips(ipdivi[1]):
                        self.redes_info[iredes].asignar_ip(ipdivi[1])
                        proceso.append(ipdivi[1].__str__() + "→" + rede.nombre)
                        iredes += 1

                        if len(redeslibres) > 0:
                            Ipb = redeslibres.pop()
                        continue
                    elif ipdivi[1].cantidad_hosts() > rede.hostsnesesarios and self.verificar_ips(ipdivi[0]):
                        Ipb = ipdivi[1]
                        redeslibres.append(ipdivi[1])

            else:
                return "No es posible dividir la IP en subredes adecuadas."

        redeslibres.append(Ipb)

        for pro in redeslibres:
            proceso.append(pro.__str__())

        return self.proceso(proceso)

    def redessinip(self):
        for rede in self.redes_info:
            if rede.ip is None:
                return True
        return False

    def verificar_ips(self, ip):
        for rede in self.redes_info:
            if rede.ip.__str__() == ip.__str__():
                return False
        return True

    def dividirips(self, ip):
        mascara_nueva = ip.mascara + 1
        if mascara_nueva < 32:
            ippadre = ip
            ip1 = Ip(ippadre.ip_redDecimal()[0], ippadre.ip_redDecimal()[1], ippadre.ip_redDecimal()[2],
                     ippadre.ip_redDecimal()[3], mascara_nueva)

            ip_bin = ippadre.ip_a_bin()
            intb = list(ip_bin)
            intb[ippadre.mascara] = '1'
            ip_octbin = ippadre.binarioADecimal(ippadre.str_a_ip("".join(intb)))
            ip2 = Ip(ip_octbin[0], ip_octbin[1], ip_octbin[2], ip_octbin[3], mascara_nueva)

            return [ip1, ip2]
        return []

    def verificarVlcm(self):
        sum=0
        if len(self.redes_info) !=0:
            for rede in self.redes_info:
                rede.calcular_hostsnesesarios()
                sum+= rede.hostsnesesarios
        return sum<self.ip_objeto.cantidad_hosts()


    def proceso(self, ips):
        res=""


        for i in range(len(ips)):
            for j in range(len(ips) - 1):
                ip1 = self.ip_to_int(ips[j])
                ip2 = self.ip_to_int(ips[j + 1])
                if ip1 > ip2:
                    ips[j], ips[j + 1] = ips[j + 1], ips[j]
        num_tabs_base = self.ip_objeto.mascara
        for ipa in ips:
            ip_part = ipa.split("→")[0].strip()
            mask = int(ip_part.split("/")[-1])

            direccion = ip_part.split("/")[0]
            octetos = list(map(int, direccion.split(".")))

            ip_objeto = Ip(octetos[0], octetos[1], octetos[2], octetos[3], mask)



            tabs = max(0, mask - num_tabs_base)
            res += ("\t" * tabs) +ip_objeto.ip_a_bin()+" " +ipa.strip() + "\n"

        return res

    def ip_to_int(self,ip_string):
        ip_parte = ip_string.split("→")[0].strip().split("/")[0]

        octetos = ip_parte.split(".")

        octeto1 = int(octetos[0])
        octeto2 = int(octetos[1])
        octeto3 = int(octetos[2])
        octeto4 = int(octetos[3])

        valor_ip = octeto1 * 256 ** 3
        valor_ip += octeto2 * 256 ** 2
        valor_ip += octeto3 * 256
        valor_ip += octeto4

        return valor_ip
























































