# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:02:08 2022

@author: d935892
"""

import poplib  
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr 
 
def decode_str(s):
    if not s:
        return None
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
 
def get_mails(prefix):
    # host = 'pop.163.com'
    host = 'smtp.gmail.com'
    username = 'datosdeviento@gmail.com'  
    contraseña = 'eoladministrador'  
      
    server = poplib.POP3(host)
    server.user(username)
    server.pass_(password)
         # Conseguir el correo
    messages = [server.retr(i) for i in range(1, len(server.list()[1]) + 1)]  
    messages = [b'\r\n'.join(mssg[1]).decode() for mssg in messages]  
    messages = [Parser().parsestr(mssg) for mssg in messages]  
    print("===="*10)
    messages = messages[::-1]
    for message in messages:  
        subject = message.get('Ammonit Data Logger Meteo-40M D162042 P.E Palomas (unsigned)')
        subject = decode_str(subject)
                 #Si el título coincide
        if subject and subject[:len(prefix)] == prefix:
            value = message.get('datalog@tecnovex.com')
            if value:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
                print ("Desde:% s"% valor)
                print ("título:% s"% asunto)
            for part in message.walk():  
                fileName = part.get_filename()  
                fileName = decode_str(fileName)
                                 # Guardar archivo adjunto  
                if fileName:  
                    with open(fileName, 'wb') as fEx:
                        data = part.get_payload(decode=True) 
                        fEx.write(data)  
                        print ("El archivo adjunto% s se ha guardado"% fileName)
    server.quit()  
 
if __name__ == '__main__':
         prefix = input ("Ingrese el prefijo del título del correo a descargar:")
         get_mails(prefix)
