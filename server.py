#!/usr/bin/env python3

import socket
import requests
import time

mylist=[]
mydata=""
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while 1:
            data = conn.recv(1024)
            if not data:
                time.sleep(10)
            mydata= data.decode("utf-8")
            mylist=mydata.split(',')
            if mylist[0]=="add":
                r=requests.get("http://127.0.0.1:5000/add?num={}&numone={}".format(mylist[1],mylist[2]))
                answer=(r.text).encode()
            conn.sendall(answer)