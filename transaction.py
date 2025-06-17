from web3 import Web3

web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
print(f"Подключено: {web3.is_connected()}")
print(f"Номер блока: {web3.eth.block_number}")

account_from = web3.eth.accounts[0]
account_to = web3.eth.accounts[1]
print(f"Баланс ноды {account_from} = {web3.eth.get_balance(account_from)}")
print(f"Баланс ноды {account_to} = {web3.eth.get_balance(account_to)}")

tx = {
    'from': account_from,
    'to': account_to,
    'value': web3.to_wei(0.001, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei(50, 'gwei'),
    'nonce': web3.eth.get_transaction_count(account_from),
}

tx_hash = web3.eth.send_transaction(tx)
print(f"Хеш транзакции: {web3.to_hex(tx_hash)}")
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Транзакция подтверждена в блоке {tx_receipt.blockNumber}")
print(f"Статус: {'Успешно' if tx_receipt.status == 1 else 'Не удалось'}")

print(f"Баланс ноды {account_from} = {web3.eth.get_balance(account_from)}")
print(f"Баланс ноды {account_to} = {web3.eth.get_balance(account_to)}")