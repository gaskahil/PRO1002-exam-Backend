from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

from blogposts import post1, post2, post3, post4, post5, post6, post7, post8, post9, post10

posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]

posts_sorted = sorted(posts, key=lambda p: datetime.strptime(p['date'], "%Y-%m-%d"), reverse=True)

post_template = env.get_template('single_post_page.html')  # Create this template

for idx, post in enumerate(posts_sorted, start=1):
    with open(f'post{idx}.html', 'w') as f:
        f.write(post_template.render(post=post, year=2025, title=post['title']))

tmpl = env.get_template('simple-variables.html')
print(tmpl.render(title='Home Page', who='everyone', year=2025, posts=posts_sorted))
