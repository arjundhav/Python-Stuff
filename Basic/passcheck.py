user=input('Whats ur User Id: ')
password=input('Enter ur Password: ')

password_length=len(password)
hidden_pass='*' * password_length

print(f'{user},your password {hidden_pass},is {password_length} letters long')

