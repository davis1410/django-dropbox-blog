from django import template
import markdown2
 
register = template.Library()
 
@register.filter
def markdown_convert(text):
    html = markdown2.markdown(text, "html5") 
    return html