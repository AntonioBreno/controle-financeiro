from django import template

register = template.Library()

@register.filter
def moeda(valor):
    if valor is None:
        return "R$ 0,00"
    
    valor_formatado = f"{valor:,.2f}"
    
    # troca padrão americano para brasileiro
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    
    return f"R$ {valor_formatado}"