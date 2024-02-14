from django import template

register = template.Library()

def condition(numbers, condition_func):
    return [x for x in numbers if condition_func(x)]

@register.filter
def less_than(numbers):
    return condition(numbers, lambda x: x < 10)

@register.filter
def only_even(numbers):
    return condition(numbers, lambda x: x % 2 == 0)
