


DevOps=["AWS", "Jenkins", "Python", "Ansible", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "AngularJs", "Java", ".net", "python")
cntr_emp1= {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code":1218}



usr_skill = input("Enter your desired skill: ")
print(usr_skill)

#check in the database if we have this skill
if usr_skill in DevOps:
    print(f"We have {usr_skill} in DevOps Team")
elif usr_skill in Development:
    print(f"We have {usr_skill} in Development team")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have {usr_skill} with contactors")
else:
    print("We do not have this skill here")