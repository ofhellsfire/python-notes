def tag(name, **attributes):
    tag_open = '<{} '.format(name)
    attrs = ' '.join(['{}="{}"'.format(attr, value) for attr, value in attributes.items()])
    tag_close = '>'
    return ''.join([tag_open, attrs, tag_close])

print(tag('div', id='12345', style='padding: 10px'))
print(tag('img', src='path/to/image', width='100px', height='100px', alt='nice picture'))
