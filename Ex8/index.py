# Dicionário para organizar as cores do terminal
cores_terminal = {
    "limpa": "\033[0m",
    "texto_amarelo_fundo_azul": "\033[33;44m",
    "sucesso": "\033[1;32m",  # Verde negrito
    "alerta": "\033[1;31m"    # Vermelho negrito
}

# Aplicando as cores no print
print(f"{cores_terminal['texto_amarelo_fundo_azul']}Texto customizado aqui!{cores_terminal['limpa']}")
print(f"{cores_terminal['sucesso']}Operação realizada com sucesso!{cores_terminal['limpa']}")
print(f"{cores_terminal['alerta']}Erro: Conexão falhou.{cores_terminal['limpa']}")
