from .mapperdata import get_users
import yaml
  
def write_params(usermapping,parameters,indent):
    indent = indent + (" " *4)
    for name in parameters:
        if name == 'protocol':
            usermapping.append(f'{indent}<protocol>{parameters[name]}</protocol>\n')
        else:
            usermapping.append(f"{indent}<param name=\"{name}\">{parameters[name]}</param>\n")
    indent = indent[:-4]
    return indent

def write_dev(usermapping,lab,indent):
    indent = indent + (" " * 4)
    for device in lab:
        usermapping.append(f"{indent}<connection name=\"{device}\">\n")	    
        write_params(usermapping,lab[device],indent)       
        usermapping.append(f"{indent}</connection>\n")	
    indent = indent[:-4]

def write_student(usermapping,students_dir):
    indent = " " * 4
    for student in students_dir:
        username=student["username"]
        password=student["password"]
        usermapping.append(f"{indent}<authorize username=\"{username}\" password=\"{password}\">\n")
		
        write_dev(usermapping,student["devices"],indent)
        
        usermapping.append(f"{indent}</authorize>\n")

def xmlwriter(students_dir,usermapping):
    usermapping.append(f"<user-mapping>\n")
    write_student(usermapping,students_dir)
    usermapping.append(f"</user-mapping>\n")



def xmlpage(students_dir,usermapping):

    usermapping.append(f"<user-mapping>\n")
    write_student(usermapping,students_dir)
    usermapping.append(f"</user-mapping>\n")
    return(usermapping)


def xmlfile(students_dir,usermapping):
    userfile = open('user-mapping.xml', 'w')
    userfile.writelines(xmlpage(students_dir,usermapping)) 
    userfile.close()


if __name__ == "__main__":
    usermapping = []
    stream = open('../config.yaml', 'r')
    configuration = yaml.safe_load(stream)
    print(configuration)
    structure = get_users(configuration)
    print()
    print(structure)
    print()
    print(xmlpage(structure,usermapping))
    xmlfile(structure,usermapping)
    

        
