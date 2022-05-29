import socket

target_host = "www.google.com"
target_port = 80

client = scoket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))