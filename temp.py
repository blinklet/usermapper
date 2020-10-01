#!/usr/bin/env python3
from mapperdata import students, ip

def userloader():
    for s in students:
        for d in s["devices"]:
            s["devices"][d]["hostname"]=ip[d]

      
def write_params(filename,parameters,indent):
    indent = indent + (" " *4)
    for name in parameters:
        filename.write(f"{indent}<param name=\"{name}\">{parameters[name]}</param>\n")
    indent = indent[:-4]
    return indent

        
def xmlwriter():
    usermapping = open('user-mapping.xml', 'w')
    usermapping.write(f"<user-mapping>\n")

    indent = " " * 4
    for student in students:
        username=student["username"]
        password=student["password"]
        lab = student["devices"]
        usermapping.write(f"{indent}<authorize username=\"{username}\" password=\"{password}\">\n")

        indent = indent + (" " * 4)
        for device in lab:
            usermapping.write(f"{indent}<connection name=\"{device}\">\n")
 #           write_params(usermapping,lab[device],indent)
            usermapping.write(f"{indent}</connection>\n")
		
        indent = indent[:-4]
        usermapping.write(f"{indent}</authorize>\n")

    usermapping.write(f"</user-mapping>\n")
    usermapping.close()

if __name__ == "__main__":
    userloader()
    xmlwriter()
    

        
