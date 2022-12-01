from jinja2 import Environment, FileSystemLoader


if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader("templates/"))
    tmpl = env.get_template("child_uno.tmpl")

    name = "Vladimir"
    title = "Nesting & Including Example"
    items = ["shirt", "comb", "glasses", "shorts", "polo", "socks"]
    menu_list = ["Home", "Products", "Support", "News", "About", "Links"]

    content = tmpl.render(name=name, items=items, title=title, menu_list=menu_list)
    print(content)
