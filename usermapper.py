#!/usr/bin/env python3
from mapperdata import students, ip

def userloader(students_dir,ip_dir):
    for student in students_dir:
        for device in student["devices"]:
            student["devices"][device]["hostname"]=ip_dir[device]
    return students_dir
  
def write_params(filename,parameters,indent):
    indent = indent + (" " *4)
    for name in parameters:
        filename.write(f"{indent}<param name=\"{name}\">{parameters[name]}</param>\n")
    indent = indent[:-4]
    return indent

def write_dev(filename,lab,indent):
    indent = indent + (" " * 4)
    for device in lab:
        filename.write(f"{indent}<connection name=\"{device}\">\n")	    
        write_params(filename,lab[device],indent)       
        filename.write(f"{indent}</connection>\n")	
    indent = indent[:-4]

def write_student(filename,students_dir):
    indent = " " * 4
    for student in students_dir:
        username=student["username"]
        password=student["password"]
        filename.write(f"{indent}<authorize username=\"{username}\" password=\"{password}\">\n")
		
        write_dev(filename,student["devices"],indent)
        
        filename.write(f"{indent}</authorize>\n")

def xmlwriter(students_dir):
    usermapping = open('user-mapping.xml', 'w')
    usermapping.write(f"<user-mapping>\n")
    write_student(usermapping,students_dir)
    usermapping.write(f"</user-mapping>\n")
    usermapping.close()

if __name__ == "__main__":
    structure = userloader(students,ip)
    xmlwriter(structure)
    

        
