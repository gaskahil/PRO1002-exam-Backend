How to run test: 
In the terminal, install pytest:
I used pip3 install pytest, depending on VSC, you might not add pip3.
Once that installment is good, you can type pytest in your terminal, and it should execute two files, test_app.py and test_integration.py. 
Before running pytest again, make sure it won't compare it's old test result with what it's trying to test with. The code on test_integration.py is trying to create a tag named TestTag, and if it tries to create TestTag again, it runs into a problem of not being allowed to perform the test. This results in a fail in the terminal.

The blog.db SQL table that the app is built for, is saved in the instance folder. This can be deleted as the app.py, has code at the start of it that fetches blog.db from the folder, but if there is no file there, it creates it for you.

running:
rm instance/blog.db 
deletes the current saved SQL table, currently the comments table is empty.

Tasks left to do: 
- Document how to run tests in your README.md


Using the SQLAlchemy's ORM (Object Relational Mapping) and query methods (like Post.query.get_or_404 and Tag.query.filter_by) should help protect against SQL Injection. 

Having Jinja2 templates should help avoid script injection, but using |safe is something one should be careful with.

Bonus: 
I can import bleach to help filter through word usage in the blog posts and comments.

