Tasks left to do: 
- Document how to run tests in your README.md

BONUS (if time)
- Make a hovereffect on blogpost to indicate that it is clickable. Currently only default cursor change shows that it is clickable
- Change the name of simple-variables to homepage or similar

- Optional Enhancements
Add login/logout features if you want to practice authentication.
Deleting blog posts and/or comments.
Better error handling: Custom HTTP status pages (404 not found etc.).
Flash: Give flash messages to users to confirm successful actions or give error messages


CSS Fixes: 
- simple-variables:
    - Add color behind tags, remove old hover function on them

- single_post_page:
    - Color behind tags
    - Fix comment section
        - How comments are shown
        - Comment field needs fixing

- Blog archive: 
    - Set sizing for all posts, might just change the elements to be named the same as on the main page

- tags page:
    - bigger search bar
    - tags are currently a mess


Using the SQLAlchemy's ORM (Object Relational Mapping) and query methods (like Post.query.get_or_404 and Tag.query.filter_by) should help protect against SQL Injection. 

Having Jinja2 templates should help avoid script injection, but using |safe is something one should be careful with.

Bonus: 
I can import bleach to help filter through word usage in the blog posts and comments.


How to run test: 
In the terminal, install pytest:
I used pip3 install pytest, depending on VSC, you might not add pip3.
Once that installment is good, you can type pytest in your terminal, and it should execute two files, test_app.py and test_integration.py. 

Saved in the instance folder, the blog.db document is. This can be deleted as the app.py, has code at the start of it that fetches blog.db from the folder, but if there is no file there, it creates it for you.