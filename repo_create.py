import sys, os, getpass
from selenium import webdriver


#check project name present exists
try:
    project_name = sys.argv[1]
except IndexError:
    print("No project name supplied")
    print("Please enter a project name argument like 'create <your_project_name>'")
    sys.exit()


##############CHANGE THIS TO LOCATION OF git_credentials.txt FILE##############
cred_path = r'C:\Users\sample.user\my_python_scripts\git_credentials.txt'
credentials_list = []
try:
    with open(cred_path) as txt_file:
        for line in txt_file:
            line = line.strip()
            credentials_list.append(line)
            
except Exception as e:
    print (e)

#assign credentials to variable
try:
    user = credentials_list[0]
except IndexError:
    user = input("Username: ")

try:
    pswd = credentials_list[1]
except IndexError:
    pswd = getpass.getpass("Password: ")


#validate credentials variables not empty
if user != "":
    pass
else:
    user = input("Username: ")

if pswd != "":
    pass
else:
    pswd = getpass.getpass("Password: ")



##############CHANGE THIS TO YOUR NEW PROJECTS PATH##############
path = r'C:\Users\sample.user\Documents\projects\my_projects'
########################################################
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.get('https://github.com/login')

def create():
    folderName = '\\' + str(sys.argv[1])
    os.mkdir(path + folderName)

    #login UI elements needed
    username_field = browser.find_element_by_xpath('//*[@id="login_field"]')
    password_field = browser.find_element_by_xpath('//*[@id="password"]')


    #LogIn
    username_field.send_keys(user)
    password_field.send_keys(pswd)
    password_field.submit()

    #create a new repo
    browser.get('https://github.com/new')
    repo_name_field = browser.find_element_by_xpath('//*[@id="repository_name"]')
    repo_name_field.send_keys(folderName.replace('\\', ''))
    repo_name_field.submit()
    browser.quit()



if __name__ == "__main__":
    create()
    