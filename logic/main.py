from ip import Ip
from redes import Red
from vlcm import vlcm

ip = Ip(190, 16, 128, 0 ,23)
print(ip)
print("IP válida?", ip.verificarIp())
print("IP decimal:", ip.octetos)
print("Máscara decimal:", ip.mascaraDesimal())
print("IP en binario:", ip.decimalaBinario(ip.octetos))
print("Máscara en binario:", ip.mascaraBinario())
print("IP de red decimal:", ip.ip_redDecimal())
print("IP de red binario:", ip.ip_redBinario())
print(ip.verificarIpRed())
print(ip.ip_a_str())
print(ip.binarioADecimal(ip.str_a_ip(ip.ip_a_str())))
print("-------------------------------")
print(ip.ipBrodcast())

print("-------------------------------")
print(ip.primeraUtilizable())

print("-------------------------------")
print(ip.UltimaUtilizable())
print(ip.cantidad_hosts())
print("-----------------------")


ippadre = Ip(190, 16, 128, 0 ,17)
resultado = ""
proceso = ""
numtabs = 1
if numtabs <= 0:
    numtabs += 1

resultado += "Ip Padre: " + ippadre.__str__() + "\n"
proceso += "Ip Padre: " + ippadre.__str__() + "\n"

ip1 = Ip(ippadre.ip_redDecimal()[0], ippadre.ip_redDecimal()[1], ippadre.ip_redDecimal()[2],
         ippadre.ip_redDecimal()[3], ippadre.mascara + 1)
a="\t" * numtabs
proceso += a + ip1.__str__() + "\n"
ip_bin = ippadre.ip_a_str()
intb = list(ip_bin)
intb[ippadre.mascara] = '1'
ip_octbin = ippadre.binarioADecimal(ippadre.str_a_ip("".join(intb)))
ip2 = Ip(ip_octbin[0], ip_octbin[1], ip_octbin[2], ip_octbin[3], ippadre.mascara + 1)

proceso += a + ip2.__str__() + "\n"
print(proceso)


rede = Red("lan1",131072)
rede.calcular_hostsnesesarios()
print(rede.hostsnesesarios)
print("***************************************************")
#ip_objeto = Ip(135, 192, 0, 0, 10)
ip_objeto = Ip(192, 168, 12, 0, 24)
redes_info = [
    #Red("Red A", 131072),
    #Red("Red B", 50000),
    #Red("Red C", 25000),
    #Red("Red D", 20000),
    #Red("Red E", 3500),
    #Red("Red F", 3000),
    #Red("Red G", 2500),
    #Red("Red H", 1024),
    #Red("Red I", 500),
    #Red("Red J", 2)
    Red("Red A", 60),
    Red("Red A", 80),
    Red("Red A", 20),
    Red("Red A", 2),
    Red("Red A", 2),


]

vlcm_obj = vlcm(ip_objeto, redes_info)
vlcm_obj.redes_info[0].calcular_hostsnesesarios()
print(vlcm_obj.redes_info[0].hostsnesesarios)
print(vlcm_obj.verificarVlcm())
var=vlcm_obj.vlcm()
print(var)
print(vlcm_obj.dividirips(ip_objeto)[0].mascara)
for i in vlcm_obj.redes_info:
    print(i)
num=0
canthost=2
resultado=0
for i in range(32):
    cant=2**num
    if cant-2 > canthost:
        resultado=num
        break
    else:
        num+=1
print(num)


ipp = Ip(190, 16, 128, 0 ,30)
print(ipp.cantidad_hosts())
print(vlcm_obj.verificarVlcm())

