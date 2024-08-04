def menu_principal():
    return f"""{38*"="}
1 - Criar Animais\n2 - Ver Animais\n3 - Atualizar Informações dos Animais
4 - Deletar Animais\n5 - Ações dos Animais\n6 - Sair
{38*"="}"""

def sub_menu_create():
    return f"""{38*"="}
1 - Criar Humano\n2 - Criar Cachorro
{38*"="}"""

def sub_menu_read():
    return f"""{38*"="}
1 - Ver Humanos\n2 - Ver Cachorros
{38*"="}"""

def sub_menu_upload():
    return f"""{38*"="}
1 - Atualizar Informações do Humano
2 - Atualizar Informações do Cachorro
{38*"="}"""

def sub_menu_delete():
    return f"""{38*"="}
1 - Deletar Humano\n2 - Deletar Cachorro
{38*"="}"""

def sub_menu_acoes():
    return f"""{38*"="}
1 - Ações do Humano\n2 - Ações do Cachorro
{38*"="}"""

def sub_menu_acoes_cachorro():
    return f"""{38*"="}
1 - Latir\n2 - Andar\n3 - Dormir\n4 - Comer
{38*"="}"""

def sub_menu_acoes_humano():
    return f"""{38*"="}
1 - Cumprimentar\n2 - Andar\n3 - Dormir\n4 - Comer
{38*"="}"""