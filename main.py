import easygui

#User Inputs
domainname = easygui.enterbox("Please input the domain: ")
ouname = easygui.enterbox("Please input the OU: ")
newname = easygui.enterbox("Please input the desired name of the new script: ")

#Breaking inputs into format for -searchbase parameter
splitdomain = domainname.split(".")
DCString = ""
for item in splitdomain:
    if item == splitdomain[-1]: #LAST ITEM IN LIST DOES NOT PUT COMMA
        DCString = DCString + "DC=" + item
    else:
        DCString = DCString + "DC=" + item + ","
OUString = "OU=" + ouname
Total = OUString+DCString


#Naming New File
nameps1 = newname + ".ps1"

#Copying template data to new script, then replacing necessary parameters
with open("TEMPLATE.ps1", "r") as template, open(nameps1, "w") as newfile:
    #for line in template:
        #newfile.write(line) #COPIES TEMPLATE TO NEW.PS1
    data = template.read()
    data = data.replace("OUCHANGE", OUString)
    data = data.replace("DCCHANGE", DCString)
    newfile.write(data)
    