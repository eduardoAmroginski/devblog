from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    # Pega todos os parâmetros atuais da URL (ex: ?categoria=Python)
    query = context['request'].GET.copy()
    
    # Atualiza ou adiciona o novo parâmetro (ex: page=2)
    for kwarg, value in kwargs.items():
        query[kwarg] = value
        
    # Retorna no formato pronto para o link (ex: categoria=Python&page=2)
    return query.urlencode()