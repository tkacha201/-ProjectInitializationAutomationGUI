# ProjectInitializationAutomationGUI

### Get project
```bash
git clone "https://github.com/tkacha201/ProjectInitializationAutomationGUI.git"
cd ProjectInitializationAutomationGUI
```


### Install modules
```bash
pip install selenium
pip install getpass
```

### SETUP to run in command line from anywhere

For windows go to "Environment Variables > System Variables > Path > Edit"
Add create.bat and repo.create.py's folder to list


### SETUP create.bat file changes
```bash
Change to location of repo_create.py, change project folder location
@python C:\Users\sample.user\my_python_scripts\repo_create.py %*
@cd "C:\Users\sample.user\somefolder\projects\my_projects\%1"
```


### SETUP repo_create.py file changes 
```bash
Change to credentials path and folder for projects path
cred_path = r'C:\Users\sample.user\my_python_scripts\git_credentials.txt'
path = r'C:\Users\sample.user\Documents\projects\my_projects'
```

### Usage:
```bash
To run the script type in 'create <name of your new project>'
```
