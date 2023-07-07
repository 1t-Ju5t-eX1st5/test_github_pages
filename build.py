from jinja2 import Environment, PackageLoader, select_autoescape
from jinja2 import exceptions
import os

def build(files: list):
    env = Environment(
        loader=PackageLoader("build"),
        autoescape=select_autoescape()
    )
    err_files = []
    for file in files:
        try:
            template = env.get_template(file)
            with open(file, "w") as f:
                f.write(template.render())
        except exceptions.TemplateNotFound as TemplateNotFound:
            print(f"Error: HTML file \'{file}\' not found. Continuing to render other files...")
            err_files.append(file)
            continue
    if len(err_files) <= 0:
        print("All files rendered successfully!")
    else:
        print(f"The following files were not found/were not able to be rendered: {err_files}")


if __name__ == "__main__":
<<<<<<< Updated upstream
    files = ['about.html', 'index.html', 'portfolio_website.html', 'portfolio.html']
=======
    files = ['about.html', 'index.html', 'python-website.html', 'projects.html', 'events.html', 'discord-bot.html']
>>>>>>> Stashed changes
    build(files)