import datetime

from jinja2 import Environment, FileSystemLoader


if __name__ == '__main__':
    """When you create a Jinja environment with `FileSystemLoader`, you can pass 
    the path that points to the folder of your templates. Once your template is 
    loaded, you can use it over and over again to fill it with content.
    """
    env = Environment(loader=FileSystemLoader("templates/"))
    tmpl = env.get_template("text_example.tmpl")

    dt = datetime.datetime.now()

    for name in ("Vladimir", "Maria", "Josef", "Nikolay"):
        """If you don't provide context for the variables in a template, 
        they don't throw an error. But they render an empty string, 
        which is usually not desired.
        """
        content = tmpl.render(
            name=name,
            time=dt.strftime("%A %d %B %Y %H:%M")
        )
        print(content)
