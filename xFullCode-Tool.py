################################################################
#                                                              #
#                        [ Creditos ]                          #
#                                                              #
################################################################
#                                                              #
#                 Codigo hecho por xNetting                    #
#                                                              #
#                Dev: xNetting / Grupo: Panic Squad            #
#                                                              #
################################################################

# CodedByxNetting / xFullCode
# PanicSquad
# Version - 1.0.0

import nmap
import requests
import hashlib
import time
import random
import pyautogui
import os
import sys

os.system('color 4')
print('''


    ▒██   ██▒  █████▒ █    ██  ██▓     ██▓     ▄████▄   ▒█████  ▓█████▄ ▓█████ 
    ▒▒ █ █ ▒░▓██   ▒  ██  ▓██▒▓██▒    ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ 
    ░░  █   ░▒████ ░ ▓██  ▒██░▒██░    ▒██░    ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   
     ░ █ █ ▒ ░▓█▒  ░ ▓▓█  ░██░▒██░    ▒██░    ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ 
    ▒██▒ ▒██▒░▒█░    ▒▒█████▓ ░██████▒░██████▒▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒
    ▒▒ ░ ░▓ ░ ▒ ░    ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░
    ░░   ░▒ ░ ░      ░░▒░ ░ ░ ░ ░ ▒  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░
     ░    ░   ░ ░     ░░░ ░ ░   ░ ░     ░ ░   ░        ░ ░ ░ ▒   ░ ░  ░    ░   
     ░    ░             ░         ░  ░    ░  ░░ ░          ░ ░     ░       ░  ░
                                              ░                  ░             

                   Dev: xNetting / xFullCode // Grupo: Panic Squad
                                                                                                                                                
    ''')

def metascanner():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │           Ponga la IP que desea escanear            │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')
    target_1 = input('''
    
    root@xnetting: ~# ''')

    nm = nmap.PortScanner()
    results = nm.scan(hosts=target_1, arguments='-sT -n -Pn -T4')
    open_ports = '-p '

    num = 0

    print('''

    Host: %s''' % target_1)
    print('''

    Estado: %s''' % nm[target_1].state())

    for protocolo in nm[target_1].all_protocols():
        print('''
        
    Protocolo: %s''' % protocolo)
        puerto = nm[target_1][protocolo].keys()
        sorted(puerto)

        for port in puerto:
            print('''
            
    Puerto: %s, Estado: %s''' % (port, nm[target_1][protocolo][port]['state']))
            if num == 0:
                open_ports = open_ports+str(port)
                num = 1
            else:
                open_ports = open_ports+", "+str(port)

    print(f'''
    
  \nPuertos abiertos: {open_ports} en {target_1}''')     

def TanTania():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Eliga el metodo que quiere para su encriptacion   │                      
    │                                                     │
    │        1 - MD5                                      │
    │                                                     │
    │        2 - SHA1                                     │                     
    │                                                     │
    │        3 - SHA256                                   │
    │                                                     │
    │        4 - SHA224                                   │
    │                                                     │
    │        5 - blake2b                                  │
    │                                                     │
    │        6 - SHA3_256                                 │
    │                                                     │
    │        10 - Todos los Algoritmos                    │
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    opcion = input('''
    
    root@xnetting: ~# ''')

    if opcion == '1':
        encode_md5()
    elif opcion == '2':
        encode_sha1()
    elif opcion == '3':
        encode_sha256()
    elif opcion == '4':
        encode_sha224()
    elif opcion == '5':
        encode_blake2b()
    elif opcion == '6':
        encode_sha3_256()
    elif opcion == '10':
        algoritmos()
    else:
        sys.exit()  

def encode_sha3_256():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │ Escriba el texto que quiere encriptar en SHA3_256   │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    sha3_256_crypt = hashlib.sha3_256()

    sha3_256_encrypted = input('''

    root@xnetting: ~# ''')

    sha3_256_crypt.update(b'sha3_256_encrypted')

    print(f'''

    root@xnetting: ~# ''' + sha3_256_crypt.hexdigest())

def encode_blake2b():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │  Escriba el texto que quiere encriptar en blake2b   │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    blake2b_crypt = hashlib.blake2b()

    blake2b_encrypted = input('''

    root@xnetting: ~# ''')

    blake2b_crypt.update(b'blake2b_encrypted')

    print(f'''

    root@xnetting: ~# ''' + blake2b_crypt.hexdigest())

def algoritmos():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │        Aqui tiene la lista de algoritmos            │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    print(f'{hashlib.algorithms_available}')

def encode_sha224():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │  Escriba el texto que quiere encriptar en SHA224    │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    sha224_crypt = hashlib.sha224()

    sha224_encrypted = input('''

    root@xnetting: ~# ''')

    sha224_crypt.update(b'sha224_encrypted')

    print(f'''

    root@xnetting: ~# ''' + sha224_crypt.hexdigest())

def encode_sha256():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │  Escriba el texto que quiere encriptar en SHA265    │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    sha256_crypt = hashlib.sha256()

    sha256_encrypted = input('''

    root@xnetting: ~# ''')

    sha256_crypt.update(b'sha256_encypted')

    print(f'''

    root@xnetting: ~# ''' + sha256_crypt.hexdigest())

def encode_sha1():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Escriba el texto que quiere encriptar en SHA1     │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    sha1_crypt = hashlib.sha1()

    sha1_encrypted = input('''

    root@xnetting: ~# ''')

    sha1_crypt.update(b'sha1_encrypted')

    print(f'''

    root@xnetting: ~# ''' + sha1_crypt.hexdigest())


def encode_md5():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Escriba el texto que quiere encriptar en MD5      │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    md5_crypt = hashlib.md5()

    md5_encrypted = input('''

    root@xnetting: ~# ''')

    md5_crypt.update(b'md5_encrypted')

    print(f'''

    root@xnetting: ~# ''' + md5_crypt.hexdigest())  

def webhookspam():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │           Ingrese la URL de su webhook              │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    webhookurl_1 = input('''

    root@xnetting: ~# ''')

    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │          Ingrese el nombre para su webhook          │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    webhooknombre_1 = input('''

    root@xnetting: ~# ''')

    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │          Ingrese el contenido de su webhook         │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    webhookcontenido_1 = input('''

    root@xnetting: ~# ''')  

    url = webhookurl_1

    data = {
        "content" : webhookcontenido_1,
        "username" : webhooknombre_1
    }

    def send(i):
        res = requests.post(webhookurl_1, data=data)
        try:
            print(f'Tiempo en rehabilitacion, espere {str(res.json()["retry_after"])} ms.')
            
            time.sleep(res.json()["retry_after"]/1000)
            res = f'Espere {str(res.json()["retry_after"])} ms'
        except:
            i += 1
            res = f"El mensaje {webhookcontenido_1} se envio correctamente"
        print(f'{res} Cantidad de mensajes enviados: {str(i)}')
        return i
    i = 0
    while True:
        i = send(i)



def webhook():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │           Ingrese la URL de su webhook              │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    webhookurl = input('''

    root@xnetting: ~# ''')

    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │          Ingrese el nombre para su webhook          │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    webhooknombre = input('''

    root@xnetting: ~# ''')

    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │          Ingrese el contenido de su webhook         │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    webhookcontenido = input('''

    root@xnetting: ~# ''')    

    url = webhookurl

    data = {
        "content" : webhookcontenido,
        "username" : webhooknombre
    }

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print('''
        
    Mensaje WebHook enviado correctamente, codigo {}.'''.format(result.status_code))

def discord():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Eliga el tipo de mensaje webhook que quiere       │                      
    │                                                     │
    │        1 - Un solo mensaje                          │
    │                                                     │
    │        2 - Spammer                                  │                     
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    webhookop = input('''
    
    root@xnetting: ~# ''')

    if webhookop == '1':
        webhook()
    elif webhookop == '2':
        webhookspam()
    else:
        sys.exit()

def password():
    character = "1234567890abcdefghijkmñlnopqrstvwxyz"
    character_list = list(character)

    password = pyautogui.password("Ingrese su contraseña: ")

    adivina_password = ""
    while (adivina_password != password):
        adivina_password = random.choices(character_list, k=len(password))

        print(f'''
        
        >>>>> {str(adivina_password)} <<<<<''')

        if (adivina_password == list(password)):
            print(f'''
            
        Tu contraseña es: ''' +'' .join(adivina_password))
            break

def aboutme():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │      Solo programo tools cuando ando aburrido.      │                      
    │                                                     │
    │     Asi que no esperes Actualizaciones seguidas.    │
    │                                                     │
    │ Esta tool iba a tener dox, pero mejor pa la privada.│
    │                                                     │
    │  Si, xFullCode & xNetting son la misma persona. xD  │
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

def main():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Eliga la herramienta que quiere usar              │                      
    │                                                     │
    │        1 - MetaScanner Premium                      │
    │                                                     │
    │        2 - TanTania                                 │                     
    │                                                     │
    │        3 - WebHook Discord                          │
    │                                                     │
    │        4 - Brute Force Password                     │
    │                                                     │
    │        10 - Sobre mi (xNetting)                     │
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    opciones = input('''
    
    root@xnetting: ~# ''')

    if opciones == '1':
        metascanner()
    elif opciones == '2':
        TanTania()
    elif opciones == '3':
        discord()
    elif opciones == '4':
        password()
    elif opciones == '10':
        aboutme()
    else:
        sys.exit()

main()
