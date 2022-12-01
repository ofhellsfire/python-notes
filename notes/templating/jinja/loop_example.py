from jinja2 import Environment, FileSystemLoader


if __name__ == '__main__':
    """When you create a Jinja environment with `FileSystemLoader`, you can pass 
    the path that points to the folder of your templates. Once your template is 
    loaded, you can use it over and over again to fill it with content.
    """
    env = Environment(loader=FileSystemLoader("templates/"))
    tmpl = env.get_template("loop_example.tmpl")

    name = "Vladimir"
    items = ["shirt", "comb", "glasses", "shorts", "polo", "socks"]

    content = tmpl.render(name=name, items=items)
    print(content)
