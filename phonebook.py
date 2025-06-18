def add_contact(contacts_list, contact_name, contact_phone, contact_email):
  contact = {
    'name': contact_name,
    'phone': contact_phone,
    'email': contact_email,
    'contact_favorite': False
  }
  contacts_list.append(contact)
  print(f'Contato {contact_name} adicionado à agenda com sucesso!')
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

def toogle_favorite(contacts_list, contact_index):
  index_contact_adjusted = int(contact_index) - 1
  if index_contact_adjusted >= 0 and index_contact_adjusted < len(contacts_list):
    if contacts_list[index_contact_adjusted]['contact_favorite'] == False:
      contacts_list[index_contact_adjusted]['contact_favorite'] = True
      print(f'Contato {contacts_list[index_contact_adjusted]["name"]} marcado como favorito!')
    else:
      print(f'Contato {contacts_list[index_contact_adjusted]["name"]} já é favorito.')
  else:
    print('Contato não encontrado. Verifique se o contato existe.')
  return

def toogle_unfavorite(contacts_list, contact_index):
  index_contact_adjusted = int(contact_index) - 1
  if index_contact_adjusted >= 0 and index_contact_adjusted < len(contacts_list):
    if contacts_list[index_contact_adjusted]['contact_favorite'] == True:
      contacts_list[index_contact_adjusted]['contact_favorite'] = False
      print(f'Contato {contacts_list[index_contact_adjusted]["name"]} desmarcado como favorito!')
    else:
      print(f'Contato {contacts_list[index_contact_adjusted]["name"]} já não é favorito.')
      
  else:
    print('Contato não encontrado. Verifique se o contato existe.')
  return

def see_favorites(contacts_list):
  print('\nLista de Contatos Favoritos:')
  favorites = [contact for contact in contacts_list if contact['contact_favorite'] == True]

  if not favorites:
    print('Não existe nenhum contato na lista de favoritos.')
    return
  
  for indice, contact in enumerate(favorites, start=1):
    print(f'{indice}. Name: {contact["name"]}, Telefone: {contact["phone"]}, Email: {contact["email"]}')
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
  print('4. Marcar contato como favorito')
  print('5. Desmarcar contato como favorito')
  print('6. Ver Lista de Favoritos')
  print('7. Apagar Contato')
  print('8. Sair da Agenda')

  choice = input('\nEscolha uma opção: ')
  if choice < '1' or choice > '8':
    print('Opção inválida. Por favor, escolha uma opção válida.')
    continue

  if choice == '1':
    contact_name = input('Digite o nome do contato: ')
    contact_phone = input('Digite o número de telefone: ')
    contact_email= input('Digite o email do contato: ')

    add_contact(contacts_list, contact_name, contact_phone, contact_email)

  elif choice == '2':
    see_contacts(contacts_list)
  
  elif choice == '3':
    see_contacts(contacts_list)
    contact_index = input('Coloque o número do contato que deseja atualizar: ')
    new_name = input('Digite o novo nome do contato: ')
    new_phone = input('Digite o novo número de telefone: ')
    new_email = input('Digite o novo email do contato: ')
    update_contact(contacts_list, contact_index, new_name, new_phone, new_email)

  elif choice == '4':
    see_contacts(contacts_list)
    contact_index = input('Coloque o número do contato que deseja marcar como favorito: ')
    toogle_favorite(contacts_list, contact_index)
    see_contacts(contacts_list)

  elif choice == '5':
    see_contacts(contacts_list)
    contact_index = input('Coloque o número do contato que deseja desmarcar como favorito: ')
    toogle_unfavorite(contacts_list, contact_index)
    see_contacts(contacts_list)

  elif choice == '6':
    see_favorites(contacts_list)  

  elif choice == '7':
    contact_index = input('Coloque o número do contato que deseja apagar:')
    delete_contact(contacts_list, contact_index)
    see_contacts(contacts_list)

  elif choice == '8':
    break

print('Agenda de contatos encerrada.')