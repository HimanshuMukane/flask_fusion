from jinja2 import FileSystemLoader

template_dirs = ['templates', 'flask_fusion/templates']
loader = FileSystemLoader(template_dirs)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS