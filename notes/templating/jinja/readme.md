# Jinja2

Jinja is a fast, expressive, extensible templating engine.

The core component of Jinja is the `Environment()` class.

## Templates Nesting

When you use Jinja's template inheritance, you can move the common structure of 
your document to a parent base template and let child templates inherit that code.

To make your base template extendable, add some `{% block <blockname> %}` to the structure.

You use the `{% block %}` to define which parts of your base template may be 
overridden by child templates.

> The names of your content blocks must be unique inside each template. 
> Otherwise, Jinja will get confused about which block to choose for replacements.

To connect the child template with its parent template, you must add an 
`{% extends <docname> %}` at the top of the file.

## Include Documents

We can add documents directly to another document by leveraging the `{% include %}` tag. 
By referencing another template with `{% include %}`, you're loading the whole template into that position.

## Filters

Jinja provides a bunch of built-in filters. They look similar to Python's 
built-in functions and string methods.

In your template you specify the variable and then a pipe symbol `|`, 
followed by the filter. In some cases, you can specify arguments in parentheses.

> In contrast to using Booleans in Python, you should write Booleans in Jinja in lowercase.

## Macros

Jinja's macros can help you create template partials that accept arguments. 
Like when defining your own functions in Python, you can define macros and 
import them into your templates.

You define a macro with a `{% macro <macro name> %}` block that resembles a 
function definition in Python. Your macro must have a name, and it can accept arguments.

To use your macros, you must import them to your base template. 
Just like with Python's import statements, it's recommended to put the 
`{% import %}` block at the top of your template.
