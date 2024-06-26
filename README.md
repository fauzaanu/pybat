# pybat

This is a dropin sort of script to a virtual environment when you need to use windows task sheduler,
which needs a .bat file to run a python script. This script simply generates that .bat file 
once you provide the python file to run.


### Running python through task sheduler

- Hidden more and highest previlages, make sure you get the password prompt
- Working directory should be current directory of the script
- Point to the .bat file to be the program that is to be run and then start the task
- see task-creation-powershell dir for a function that creates a task using subprocess and a powershell script

