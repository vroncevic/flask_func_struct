# -*- coding: utf-8 -*-

project = u'flask_func_struct'
copyright = u'2017, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.4.0'
release = u'https://github.com/vroncevic/flask_func_struct/releases'
extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'classic'
html_static_path = ['_static']
htmlhelp_basename = 'flask_func_structdoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'flask_func_struct.tex',
    u'flask\\_func\\_struct Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'flask_func_struct', u'flask_func_struct Documentation',
    [author], 1
)]
texinfo_documents = [(
    master_doc, 'flask_func_struct', u'flask_func_struct Documentation',
    author, 'flask_func_struct', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
