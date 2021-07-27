import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6ab4979537a699a99b569671baf52f46"
# Your Auth Token from twilio.com/console
auth_token  = "9a1b1b963b0739090bc1b625c0d0c900"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5519987800015",
            from_="+13217104681",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
