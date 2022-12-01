import jinja2


if __name__ == '__main__':
    env = jinja2.Environment()

    """Load a template: Load a source that contains placeholder variables. 
    By default, they're wrapped in a pair of curly brackets `{{ }}`.
    """
    tmpl = env.from_string("Hey, {{ name }}!")

    """Render the template: Fill the placeholders with content. 
    You can provide a dictionary or keyword arguments as context.
    """
    s = tmpl.render(name="Vladimir")
    print(s)
    s = tmpl.render({"name": "Josef"})
    print(s)
