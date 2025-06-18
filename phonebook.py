def add_contact(contacts_list, contact_name, contact_phone, contact_email):
  contact = {
    'name': contact_name,
    'phone': contact_phone,
    'email': contact_email,
    'contact_favorite': False
  }
  contacts_list.append(contact)
  print(f'Contato: {contact_name}, Phone: {contact_phone}, Email: {contact_email} adicionados com sucesso!')
  return

def see_contacts(contacts_list):
  print('\nLista de Contatos: ')
  for indice, contact in enumerate(contacts_list, start=1):
    favorite_status = '✔' if contact['contact_favorite'] else 'Não'
    print(f'{indice}. Nome: {contact["name"]}, Telefone: {contact["phone"]}, Email: {contact["email"]}, Favorito: {favorite_status}')
  return

contacts_list=[]

while True:
  print('\nMenu Agenda de Contatos')
  print('1. Adicionar Contato')
  print('2. Visualizar Lista de Contatos')
  print('3. Editar Contato')
  print('4. Marcar/Desmarcar contato como favorito')
  print('5. Ver Lista de Favoritos')
  print('6. Apagar Contato')
  print('7. Sair da Agenda')

  choice = input('\nEscolha uma opção: ')

  if choice == '1':
    contact_name = input('Digite o nome do contato: ')
    contact_phone = input('Digite o número de telefone: ')
    contact_email= input('Digite o email do contato: ')

    add_contact(contacts_list, contact_name, contact_phone, contact_email)

  elif choice == '2':
    see_contacts(contacts_list)

  elif choice == '7':
    break

print('Agenda de contatos encerrada.')