##function para inserir os dados na tabela
def Insert(nome, sobrenome, nascimento, sexo="m", cpf="", rg=""):
    data = "INSERT INTO `clientes` (`id`, `nome`, `sobrenome`, `nascimento`, `sexo`, `cpf`, `rg`) VALUES (NULL, '"+nome+"', '"+sobrenome+"', '"+nascimento+"', '"+sexo+"', '"+cpf+"', '"+rg+"')"
    return data