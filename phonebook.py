def add_contact(contacts_list, contact_name, contact_phone, contact_email):
  contact = {
    'name': contact_name,
    'phone': contact_phone,
    'email': contact_email,
    'contact_favorite': False
  }
  contacts_list.append(contact)
  print(f'Contato: {contact_name}, Telefone: {contact_phone}, Email: {contact_email} adicionados com sucesso!')
  return

def see_contacts(contacts_list):
  print('\nLista de Contatos: ')
  if not contacts_list:
    print('Nenhum contato foi adicionado ainda')
    return

  for indice, contact in enumerate(contacts_list, start=1):
    favorite_status = '✔' if contact['contact_favorite'] else 'Não'
    print(f'{indice}. Nome: {contact["name"]}, Telefone: {contact["phone"]}, Email: {contact["email"]}, Favorito: {favorite_status}')
  return

def update_contact(contacts_list, contact_index, new_name, new_phone, new_email):
  index_contact_adjusted = int(contact_index) - 1 
  if index_contact_adjusted >= 0 or index_contact_adjusted < len(contacts_list):
    contacts_list[index_contact_adjusted] ['name'] = new_name
    contacts_list[index_contact_adjusted] ['phone'] = new_phone
    contacts_list[index_contact_adjusted] ['email'] = new_email
    print(f'Contato atualizado: {new_name}, Telefone: {new_phone}, Email: {new_email}')
  else:
    print('Contato não encontrado. Verique se o contato existe.')
  return

def delete_contact(contacts_list, contact_index):
  index_contact_adjusted = int(contact_index) - 1
  if index_contact_adjusted >= 0 and index_contact_adjusted < len(contacts_list):
    deleted_contact = contacts_list.pop(index_contact_adjusted)
    print(f'Contato {deleted_contact["name"]} apagado com sucesso!')
  return

contacts_list=[]

while True:
  print('\nMenu Agenda de Contatos')
  print('1. Adicionar Contato')
  print('2. Visualizar Lista de Contatos')
  print('3. Atualizar Contato')
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
  
  elif choice == '3':
    contact_index = input('Coloque o número do contato que deseja atualizar: ')
    new_name = input('Digite o novo nome do contato: ')
    new_phone = input('Digite o novo número de telefone: ')
    new_email = input('Digite o novo email do contato: ')
    update_contact(contacts_list, contact_index, new_name, new_phone, new_email)

  elif choice == '6':
    contact_index = input('Coloque o número do contato que deseja apagar:')
    delete_contact(contacts_list, contact_index)
    see_contacts(contacts_list)

  elif choice == '7':
    break

print('Agenda de contatos encerrada.')