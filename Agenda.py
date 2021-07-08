# contatos guardados
agenda = [
    ['Maria', '3245-0098'],
    ['Thiago', '3272-8482'],
    ['Ana', '4002-8922']
]
while True:
    # apresentação do painel
    print(
        '''
        ***************************
        * AGENDA App - versão 0.1 *
        ***************************
         1- Listar Contatos
         2- Adicionar contato
         3- Editar contato
         4- Apagar contato
         5- Pesquisar contato
         0- Sair
        '''
    )
    r = int(input(':> '))
    if r == 1: # 1 \\ apresenta contatos listados
        for posição, contato in enumerate(agenda):
            print(f'{posição} Nome: {contato[0]} - Tel: {contato[1]} ')
            
    if r == 2: #2 \\ adiciona contato
        nome = str(input('Digite o nome: '))
        tel = str(input('Digite o telefone: '))
        agenda.append([nome, tel])
    
    if r == 3: # 3 \\ edita contato
        print('Digite a posição do contato a ser editado.')
        posição = int(input(':> '))
        contato = agenda.pop(posição)
        print(f'Nome: {contato[0]}')
        new_contato = []
        new_name = str(input('Novo nome[enter para manter] :> '))
        if new_name == '':
            new_contato.append(contato[0])
        else:
            new_contato.append(new_name)
        
        print('Editor de telefone.')
        new_tel = str(input('Novo número[enter para manter] :>'))
        if new_tel == '':
            new_contato.append(contato[1])
        else:
            new_contato.append(new_tel)
        agenda.insert(posição, new_contato)       
        
    elif r == 4: # 4 \\ apagar contato
        c = int(input('Digite a posição do contato que você deseja apagar: '))
        contato = agenda.pop(c)
        print(f'{contato} apagado.')
        
    elif r == 5: #5 \\ pesquisar um contato
        print('Pesquise o contato.')
        name = str(input('Nome: '))
        for posição, contato in enumerate(agenda):
            if name in contato[0]:
                print(50*'*')
                print(f'{posição} Nome: {contato[0]} - tel {contato[1]}')
                print(50*'*')
    # saída
    elif r == 0:
        print('Obrigado por usar o App.')
        break
input()
