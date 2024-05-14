
import datetime
#  Gerar uma lista de anos  dinamica
# Obter o ano atual
ano_atual = datetime.datetime.now().year
# Número de anos para incluir após o ano atual
ultimos_anos = 49

# Criar a lista dos últimos 50 anos
anos_dinamico = [str(ano) for ano in range(ano_atual, ano_atual - ultimos_anos, -1)]
anos_p = ['Todos'] + anos_dinamico

print(anos_p)