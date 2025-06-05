# My Backend driven Pink blog 
The task for this exam has been to create a blog application that allows you to list, create, update, and view posts. It also has a comment function. With more time and focus on this exam, I would have liked to add a delete option to elements, and allow users to edit their comments. 

## Setup
### 1. I have used Github, connected to Visual Studio Code(VSC), and I recommend it for this Repository.
### 2. Extentions I have downloaded in VSC for the project is:
   - flask-snippets
   - Github Codespaces
   - Pylance
### 3. How to Run Tests
In the terminal, type in:
```
pip3 install pytest:
```
I used pip3 install pytest, depending on your system, you might not add the number 3. <br/>
Once that installment is good, you can type:
```
pytest
```
in your terminal, and it should execute two files, test_app.py and test_integration.py. If you want to run the test again, you need to delete the current blog.db file. <br/>
Back in the terminal, you then type:
```
rm instance/blog.db
```
This deletes the current db file created and tested using my tests. The code on test_integration.py is trying to create a new tag to the db table, and running it a second time, that testtag will then already be available in the SQL table. This results in a fail in the terminal.
### 4. Run app.py
In your terminal, type:
```
python3 app.py
```
Again, the number 3 added to python is due to my version. Your setup might be different and require no number connected to python.

