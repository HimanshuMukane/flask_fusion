from flask_fusion.html_templates import generate_carousel,generate_modal
from flask import Blueprint, render_template, request

modal_blueprint = Blueprint('modal', __name__)

@modal_blueprint.route('/createModal', methods=['POST'])
def createModal():
    if request.method == 'POST':
        template_type = request.form.get('template_type')
        modal_button = request.form.get('modal_button')
        modal_title = request.form.get('modal_title')
        modal_body = request.form.get('modal_body')
        template_data = {'template_type':template_type,'modal_button':modal_button,'modal_title':modal_title,'modal_body':modal_body}
        html = generate_modal(template_data=template_data)
        with open(f"./templates/{template_type}_output.html",'w') as f:
            f.write(html)
        return render_template(f"{template_type}_output.html")

def modal_routes(app):
    app.register_blueprint(modal_blueprint, url_prefix='/')
