from django import template

register = template.Library()

# First way to register our own custom filter
# using a decorator
@register.filter(name='cut')
def cut(value, arg):  # Custom template filter
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# Second way to register our own custom filter
# First arg = string you called the function when using the template tag
# Second arg = name of the function itself
#register.filter('cut', cut)
