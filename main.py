import re
import csv
import os
from typing import Dict, List

class AgendaTelefonica:
    def __init__(self, arquivo: str = "contatos.csv"):
        """
        Inicializa a agenda telefônica.
        Args:
            arquivo: Nome do arquivo CSV para armazenar os contatos
        """
        self.arquivo = arquivo
        self.contatos: List[Dict[str, str]] = []
        self.carregar_contatos()

    def validar_nome(self, nome: str) -> bool:
        """Valida se o nome tem pelo menos 3 caracteres."""
        return len(nome.strip()) >= 3

    def validar_telefone(self, telefone: str) -> bool:
        """Valida se o telefone tem entre 8 e 15 digitos numéricos."""
        telefone_limpo = ''.join(filter(str.isdigit, telefone))
        return 8 <= len(telefone_limpo) <= 15

    def validar_email(self, email: str) -> bool:
        """Valida se o email contém @ e um domínio válido."""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao, email))

    def cadastrar_contato(self) -> None:
        """Solicita e valida os dados do novo contato."""
        print("\n=== Cadastro de Novo Contato ===")

        # Validação do nome
        while True:
            nome = input("Nome completo: ").strip()
            if self.validar_nome(nome):
                break
            print("Nome inválido! Digite pelo menos 3 caracteres.")

        # Validação do telefone
        while True:
            telefone = input("Telefone: ").strip()
            if self.validar_telefone(telefone):
                telefone = ''.join(filter(str.isdigit, telefone))
                break
            print("Telefone inválido! Digite entre 8 e 15 dígitos numéricos.")

        # Validação do email
        while True:
            email = input("Email: ").strip()
            if self.validar_email(email):
                break
            print("Email inválido! Digite um email válido (exemplo@dominio.com).")

        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }

        self.contatos.append(contato)
        print("\nContato cadastrado com sucesso!")

        # Pergunta se deseja salvar imediatamente
        if input("\nDeseja salvar as alterações agora? (s/n): ").lower() == 's':
            self.salvar_contatos()

    def exibir_contatos(self) -> None:
        """Exibe todos os contatos cadastrados."""
        if not self.contatos:
            print("\nNenhum contato cadastrado!")
            return

        print("\n=== Lista de Contatos ===")
        for i, contato in enumerate(self.contatos, 1):
            print(f"\nContato {i}:")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print("-" * 30)

    def buscar_contato(self, nome: str) -> None:
        """
        Busca um contato pelo nome.
        Args:
            nome: Nome do contato a ser buscado
        """
        nome = nome.lower()
        encontrados = [
            contato for contato in self.contatos
            if nome in contato['nome'].lower()
        ]

        if not encontrados:
            print("\nNenhum contato encontrado!")
            return

        print("\n=== Contatos Encontrados ===")
        for contato in encontrados:
            print(f"\nNome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print("-" * 30)

    def salvar_contatos(self) -> None:
        """Salva os contatos no arquivo CSV."""
        try:
            with open(self.arquivo, 'w', newline='', encoding='utf-8') as arquivo:
                writer = csv.DictWriter(arquivo, fieldnames=['nome', 'telefone', 'email'])
                writer.writeheader()
                writer.writerows(self.contatos)
            print("\nContatos salvos com sucesso!")
        except Exception as e:
            print(f"\nErro ao salvar contatos: {str(e)}")

    def carregar_contatos(self) -> None:
        """Carrega os contatos do arquivo CSV."""
        if not os.path.exists(self.arquivo):
            return

        try:
            with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
                reader = csv.DictReader(arquivo)
                self.contatos = list(reader)
            print("\nContatos carregados com sucesso!")
        except Exception as e:
            print(f"\nErro ao carregar contatos: {str(e)}")

    def menu_principal(self) -> None:
        """Exibe e gerencia o menu principal do programa."""
        while True:
            print("\n=== AGENDA TELEFÔNICA ===")
            print("1. Cadastrar novo contato")
            print("2. Visualizar todos os contatos")
            print("3. Buscar contato")
            print("4. Salvar contatos")
            print("5. Sair")

            opcao = input("\nEscolha uma opção (1-5): ").strip()

            if opcao == '1':
                self.cadastrar_contato()
            elif opcao == '2':
                self.exibir_contatos()
            elif opcao == '3':
                nome = input("\nDigite o nome para busca: ")
                self.buscar_contato(nome)
            elif opcao == '4':
                self.salvar_contatos()
            elif opcao == '5':
                print("\nSalvando contatos antes de sair...")
                self.salvar_contatos()
                print("\nObrigado por usar a Agenda Telefônica!")
                break
            else:
                print("\nOpção inválida! Por favor, escolha uma opção entre 1 e 5.")

def main():
    agenda = AgendaTelefonica()
    agenda.menu_principal()

if __name__ == "__main__":
    main()
