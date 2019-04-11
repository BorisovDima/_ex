import socket, os
"""
C каждым сокет связываются три атрибута: домен, тип и протокол. 
Домен определяет пространство адресов, в котором располагается сокет,
 и множество протоколов, которые используются для передачи данных. 
 Чаще других используются домены Unix и Internet, задаваемые константами AF_UNIX и AF_INET 
 соответственно (префикс AF означает "address family" - "семейство адресов")
"""
socket.socket(socket.AF_UNIX)
socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) # default
"""
При задании AF_UNIX для передачи данных используется файловая система ввода/вывода Unix.
 В этом случае сокеты используются для межпроцессного взаимодействия на одном компьютере и не годятся для работы по сети
 но они более легковесны
"""


socket.socket(socket.AF_INET) #  Константа AF_INET соответствует Internet-домену.

"""
Тип сокета определяет протокол передачи данных по сети. Чаще других применяются:
TCP гарантирует доставку пакетов, их очередность, автоматически разбивает данные на пакеты 
и контролирует их передачу, в отличии от UDP. 

"""
socket.socket(socket.AF_INET, socket.SOCK_STREAM) #  TCP

socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #  UDP


"""
Адреса ( Порты )
"""

if os.path.exists('unix_file'):
    os.remove('unix_file')
socket.socket(socket.AF_UNIX).bind('unix_file') # В Unix-домене порт это имя файла, через который происходит обмен данными.

socket.socket(socket.AF_INET).bind(('0.0.0.0', 8006)) # В Internet-домене адрес - IP-адрес и номер порта

"""
Протоколы TCP и UDP используют различные пространства портов.
"""
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind(('0.0.0.0', 8006))

socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_udp.bind(('0.0.0.0', 8006))

##############################
