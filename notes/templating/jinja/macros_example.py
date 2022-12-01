import datetime

from jinja2 import Environment, FileSystemLoader


if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader("templates/"))
    tmpl = env.get_template("macros_usage_example.tmpl")

    dt = datetime.datetime.now()
    name = "Vladimir"

    content = tmpl.render(
        name=name,
        time=dt.strftime("%A %d %B %Y %H:%M"),
        hour=dt.hour,
    )

    print(content)