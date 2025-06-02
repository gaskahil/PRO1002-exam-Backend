from dominate import document
from dominate.tags import *

#Creating the main page
with document(title='Home page') as page1:
    with page1.head:
        meta(charset='utf-8')
        meta(name='viewport', content='width=device-width, initial-scale=1.0')
        link(rel='stylesheet', href='style.css')
#       script(type='text/javascript', src='script.js')
    with nav(class_='navbar'):
        a('Home', href='index.html', class_='nav-link')
        a('Old blog Posts', href='blogposts.html', class_='nav-link')
        a('Tags', href='tags.html', class_='nav-link')
        a('Create New Post', href='create_post.html', class_='nav-link')
    with section(id='content'):
        h1('Hello, everyone!')
        p('Welcome to my blog!')
        with section(id='homePageCredentials'):
            p('These are the credentials for this page;')
            with ul( id='unoderedTasks', class_='homeList'):
                li('Lists all blog posts (show title, publishing date, excerpt (first paragraph or first 150 characters), and the tags).'),
                li('Order blog posts by dates, newest first.'),
                li('Link that allows users to read the whole blog post.'),
                li('Include at least 10 blog posts, you can use an LLM (e.g. ChatGPT) to generate them.'),
                li('Should provide a link to "Create New Blog Post" page.')

#Creating the blog post overview page 
with document(title='Blog posts') as page2:
    with page2.head:
        meta(charset='utf-8')
        meta(name='viewport', content='width=device-width, initial-scale=1.0')
        link(rel='stylesheet', href='style.css')
#       script(type='text/javascript', src='script.js')
    with nav(class_='navbar'):
        a('Home', href='index.html', class_='nav-link')
        a('Old blog Posts', href='blogposts.html', class_='nav-link')
        a('Tags', href='tags.html', class_='nav-link')
        a('Create New Post', href='create_post.html', class_='nav-link')
    with section(id='content'):
        h1('Blog posts')
        p('Here you can create new posts or alter old ones.')
        with section(id='blogpostCredentials'):
            p('These are the credentials for this page;')
            with ul(id='unoderedTasks', class_='blogList'):
                li('At a minimum consists of a title, publishing date, body and a list of tags.'),
                li('Link to edit the blog post.'),
                li('List of all the related comments.'),
                li('Comments have a title, date and the comment itself.'),
                li('Form to add new comments (with basic validation).')

with document(title='Tag Page') as page3:
    with page3.head:
        meta(charset='utf-8')
        meta(name='viewport', content='width=device-width, initial-scale=1.0')
        link(rel='stylesheet', href='style.css')
#       script(type='text/javascript', src='script.js')
    with nav(class_='navbar'):
        a('Home', href='index.html', class_='nav-link')
        a('Old blog Posts', href='blogposts.html', class_='nav-link')
        a('Tags', href='tags.html', class_='nav-link')
        a('Create New Post', href='create_post.html', class_='nav-link')
    with section(id='content'):
        h1('Tag Page')
        with section(id='main'):
            p('These are the credentials for this page;')
            with ul(id='unorderedTasks', class_='tagList'):
                li('Lists all blog posts based on a given tag.'),
                li('All tags in the app should be links that take the user to this page.')

with document(title='Create New Post') as page4:
    with page4.head:
        meta(charset='utf-8')
        meta(name='viewport', content='width=device-width, initial-scale=1.0')
        link(rel='stylesheet', href='style.css')
#       script(type='text/javascript', src='script.js')
    with nav(class_='navbar'):
        a('Home', href='index.html', class_='nav-link')
        a('Old blog Posts', href='blogposts.html', class_='nav-link')
        a('Tags', href='tags.html', class_='nav-link')
        a('Create New Post', href='create_post.html', class_='nav-link')
    with section(id='content'):
        h1('Create New Post')
        p('Here you can create new posts.')
        with section(id='createPostCredentials'):
            p('These are the credentials for this page;')
            with ul(id='unorderedTasks', class_='createPostList'):
                li('Form to create new blog post.'),
                li('Title, publishing date, body and a list of tags.'),
                li('Basic validation for the form.')

print(page1)
#print(page2)
#print(page3)

# save page1 as index.html
#with open('index.html', 'w') as f:
#    f.write(str(page1))
# Save page2 as blogposts.html
#with open('blogposts.html', 'w') as f:
#    f.write(str(page2))
# Save page3 as tags.html
#with open('tags.html', 'w') as f:
#    f.write(str(page3))