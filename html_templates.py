from flask import render_template
def generate_carousel(template_data):
    template_list = {'basic_slide_carousel': 'basic_slide_carousel.html', '3dwheelcarousel': '3dwheelcarousel.html' }
    items = template_data['items']
    template_name = template_data.get('template_type')
    if template_name:
        html = render_template(template_list[template_name], items=items)
        return html
    else:
        return "Template not found"    

def generate_modal(template_data):
    template_list = {'basic_modal': 'basic_modal.html', 'small_modal': 'small_modal.html','large_modal' : 'large_modal.html' }
    template_name = template_data.get('template_type')
    if template_name:
        html = render_template(template_list[template_name], template_data=template_data)
        return html
    else:
        return "Template not found"
    
