class Ip:
    def __init__(self,octeto1,octeto2,octeto3,octeto4,mascara):
        self.octetos = [octeto1, octeto2, octeto3, octeto4]
        self.mascara=mascara

    def a_str(self):
        return f"{self.ip_redDecimal()[0]}.{self.ip_redDecimal()[1]}.{self.ip_redDecimal()[2]}.{self.ip_redDecimal()[3]}/{self.mascara}"
    def __str__(self):
        return self.a_str()

    #--------CALCULOS-----------------------------------------#
    def ip_a_str(self):
        a=""
        for i in self.ip_redBinario():
            a+= str(i)
        return a
    
    def str_a_ip(self,stra):
        strb=stra
        octetos = []
        for i in range(0, 32, 8):
            grupo = strb[i:i+8]
            octetos.append(grupo)
        return octetos
    
    def decimalaBinario(self,decimal):
        binariosIp = []
        for i in decimal: 
            bin_octetoIp = ""
            num = i
            for j in range(8):
                residuo = num % 2
                bin_octetoIp = str(residuo) + bin_octetoIp  
                num = num // 2
            binariosIp.append(bin_octetoIp)                  
        return binariosIp
    
    def binarioADecimal(self, binarios):
        decimales = []
        for bin_octeto in binarios:
            decimal = 0
            potencia = 1

            for bit in reversed(bin_octeto):
                if bit == '1':
                    decimal += potencia
                potencia *= 2
            decimales.append(decimal)
        return decimales
    
    def and_binario(self, bin1, bin2):
        resultado = ''

        for i in range(len(bin1)):
            if bin1[i] == '1' and bin2[i] == '1':
                resultado += '1'
            else:
                resultado += '0'
        return resultado
    def verificarIp(self):
        mascara=False
        Ips=True
        if (self.mascara >= 0 and self.mascara <= 32):
            mascara=True

        for i in self.octetos: 
            if not ( i>=0 and i <= 255):
                Ips=False
                break
        return mascara and Ips

   #--------METODOS------------------------------------------#

    def mascaraDesimal(self):
        mascara_entera = self.mascara
        mascara_octetos = []
        bits_restantes = mascara_entera
        for _ in range(4):
            if bits_restantes >= 8:
                mascara_octetos.append(255)
                bits_restantes -= 8
            elif bits_restantes > 0:
                valor = 256 - 2**(8 - bits_restantes)
                mascara_octetos.append(valor)
                bits_restantes = 0
            else:
                 mascara_octetos.append(0)
        return mascara_octetos
   
    def ip_redDecimal(self):
        ip_red = []
        mascara_decimal = self.mascaraDesimal()
        for i in range(4):
            ip_red.append(self.octetos[i] & mascara_decimal[i])
        return ip_red
    
    def ip_redBinario(self):
        ip_red = []
        ip_binarios = self.decimalaBinario(self.octetos)
        mascara_binarios = self.decimalaBinario(self.mascaraDesimal())
        for i in range(4):
            resultado_and = self.and_binario(ip_binarios[i], mascara_binarios[i])
            ip_red.append(resultado_and)
        return ip_red

    def mascaraBinario(self):
        return self.decimalaBinario(self.mascaraDesimal())

    def verificarIpRed(self):
        if(self.octetos==self.ip_redDecimal()):
            return True
        else:
            return False

    def ipBrodcast(self):
        intb = list(self.ip_a_str())
        for i in range(self.mascara,32):
            intb[i]='1'
        return self.binarioADecimal(self.str_a_ip("".join(intb)))
    def primeraUtilizable(self):
        a=int(self.ip_a_str())
        return self.binarioADecimal(self.str_a_ip(str(a+1)))
    def UltimaUtilizable(self):
        intb = list(self.ip_a_str())
        for i in range(self.mascara,31):
            intb[i]='1'
        return self.binarioADecimal(self.str_a_ip("".join(intb)))

    def cantidad_hosts(self):
        bits_host = 32 - self.mascara
        if bits_host >= 2:
            return (2 ** bits_host) - 2
        else:
            return 0

