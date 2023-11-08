from flask import Blueprint, render_template, request
from flask_fusion.html_templates import generate_carousel,generate_modal
import os
from flask_fusion.config import ALLOWED_EXTENSIONS  
import uuid

carousel_blueprint = Blueprint('carousel', __name__)

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']

@carousel_blueprint.route('/createCarousel', methods=['POST'])
def createCarousel():
    if request.method == 'POST':
        template_type = request.form.get('template_type')
        template_imgs = request.files.getlist('template_img')
        template_img_titles = request.form.getlist('template_img_title')
        items = []
        for i in range(len(template_imgs)):
            if template_imgs[i].filename != '' and template_imgs[i].filename.split('.')[-1] in ALLOWED_EXTENSIONS:
                template_imgs[i].filename = str(uuid.uuid4()) + '.' + template_imgs[i].filename.split('.')[-1]
                template_imgs[i].save(os.path.join('static/user_uploaded/',template_imgs[i].filename))
                items.append({'image':template_imgs[i].filename,'text_content':template_img_titles[i]})
        template_data = {'template_type':template_type,'items':items}
        html = generate_carousel(template_data=template_data)
        with open(f"./templates/{template_type}_output.html",'w') as f:
            f.write(html)
        return render_template(f"{template_type}_output.html")
    
def carousel_routes(app):
    app.register_blueprint(carousel_blueprint, url_prefix='/')