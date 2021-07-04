@python C:\Users\sample.user\my_python_scripts\repo_create.py %*
@cd "C:\Users\sample.user\somefolder\projects\my_projects\%1"
@git init
@git remote add origin https://github.com/yourUsername/%1.git
@echo.> README.md
@git add .
@git commit -m "initial commit"
@git push -u origin master
@git status
@code .



