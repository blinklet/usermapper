#!/usr/bin/env python3
from copy import copy, deepcopy

sshparams = {
    "protocol" : "ssh",
    "hostname" : "",
    "port" : "22",
    "username" : "root",
    "password" : "root",
    "color-scheme" : "black-white",
    "enable-sftp" : "true",
    "sftp-root-directory" : "/"
}

r1params = copy(sshparams)
r2params = copy(sshparams)
r3params = copy(sshparams)
r4params = copy(sshparams)
r5params = copy(sshparams)

devices = {
    "Router01" : r1params,
    "Router02" : r2params,
    "Server01" : r3params,
    "Server02" : r4params,
    "Server03" : r5params
}

s1device = deepcopy(devices)
s2device = deepcopy(devices)
s3device = deepcopy(devices)
s4device = deepcopy(devices)



student01 = dict(
    username="student01",
    password="lI62d4WUDKNv",
    devices=s1device
)

student02 = dict(
    username="student02",
    password="UwBF9HJ3Astu",
    devices=s2device
)

student03 = dict(
    username="student03",
    password="passwortdddd",
    devices=s3device
)

student04 = dict(
    username="student04",
    password="ppasswword",
    devices=s4device
)

students = [student01, student02, student03, student04]

ip = {
    "Router01" : "10.0.20.1",
    "Router02" : "10.0.20.2",
    "Server01" : "10.0.20.101",
    "Server02" : "10.0.20.102",
    "Server03" : "10.0.20.103"
}
            

if __name__ == "__main__":
    print(students)
    print()
    print(ip)
    print()
    

