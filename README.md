# Agenda Telefônica

Este é um projeto feito ao final da cadeira de Algoritmos e Programação, onde foi usado o conhecimento em Python adquirido ao longo do semestre!

---

## Projeto

O código da agenda está no arquivo **main.py**.

## Requisitos solicitados

Estes foram os requisitos fornecidos para a criação da agenda:

 **Desenvolvimento de uma Agenda Telefônica “Pythônica”**
 
 Objetivo: Desenvolver uma agenda telefônica em Python que permita ao usuário cadastrar,
 visualizar e gerenciar contatos com armazenamento permanente em um arquivo de texto
 (TXT) ou CSV. O sistema deve utilizar funções, listas e dicionários para estruturar o código
 e os dados de forma eficiente. Ao final, o programa deve ser capaz de salvar os contatos
 em um arquivo e carregar os dados sempre que reiniciado.
 
 Requisitos:
 
 1. Estrutura de Dados e Armazenamento:
    - Cada contato deve ser armazenado como um dicionário com as seguintes
 chaves: nome, telefone e email.
    - O programa deve utilizar uma lista para armazenar múltiplos contatos.
    - Os dados devem ser salvos em um arquivo no formato TXT ou CSV,
 permitindo que sejam carregados automaticamente ao iniciar o programa.

 2. Cadastro e Validação de Contatos:
    - O sistema deve permitir que o usuário cadastre novos contatos.
    - Cada contato deve conter:
      * Nome completo (obrigatório, com pelo menos 3 caracteres).
      * Número de telefone (obrigatório, deve conter apenas números e ter entre 8 e 15 dígitos).
      * Email (obrigatório, deve conter o caractere "@" e um domínio válido, como ".com").
    - Validar os dados de entrada:
      * Caso o nome, número ou email não atendam aos critérios, solicitar que o usuário insira novamente.

 3. Funcionalidades do Programa:
    - Implementar as seguintes funções:
      * cadastrar_contato(): para solicitar e validar os dados do contato, adicionando-o à lista de contatos.
      * exibir_contatos(): para exibir todos os contatos cadastrados, mostrando o nome, telefone e email de cada um.
      * buscar_contato(nome): para buscar um contato salvo, pelo nome no arquivo, mostrando o nome, telefone e email.
      * salvar_contatos(): para salvar a lista de contatos no arquivo escolhido (TXT ou CSV), garantindo que os dados sejam persistentes.
      * carregar_contatos(): para carregar os contatos previamente salvos no arquivo ao iniciar o programa.
      * menu_principal(): para exibir as opções do programa e gerenciar a navegação.
  
 4. Estrutura do Programa e Loop Principal:
    - O programa deve rodar em loop contínuo até que o usuário opte por sair.
    - Utilizar um loop while no menu_principal() para oferecer opções como "Cadastrar novo contato", "Visualizar todos os contatos", "Salvar contatos" e "Sair".
    - O loop só deve ser encerrado quando o usuário escolher a opção "Sair".
  
 5. Armazenamento e Recuperação de Dados:
    - Ao iniciar, o programa deve carregar automaticamente os contatos do arquivo (se existir).
    - Sempre que um contato novo é adicionado, o usuário deve ter a opção de salvar as alterações no arquivo.
    - Quando o programa for encerrado, deve garantir que todos os contatos salvos na lista sejam gravados no arquivo, para que estejam disponíveis na próxima execução.
  
 6. Exibição dos Contatos:
    - Ao escolher a opção de visualizar contatos, o programa deve listar todos os contatos cadastrados, exibindo nome, número de telefone e email de cada um.
