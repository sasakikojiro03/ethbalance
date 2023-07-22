#check EVM balance
from web3 import Web3

#RPC
sepolia_url ='https://rpc.sepolia.org'
goerli_url = 'https://goerli.blockpi.network/v1/rpc/public'
eth_url = 'https://1rpc.io/eth'
base_url = 'https://goerli.base.org'
scroll_url = 'https://alpha-rpc.scroll.io/l2'
taiko_url = 'https://rpc.a2.taiko.xyz/'
bsc_url = 'https://bsc-dataseed1.binance.org/'
polygon_url = 'https://polygon-rpc.com'
linea_rpc = 'https://rpc.goerli.linea.build'
avax_testnet = 'https://rpc.ankr.com/avalanche_fuji'
op = 'https://opt-mainnet.g.alchemy.com/v2/demo'
zksync = ''

#Smart contract
token_address = '0x60e6895184448f3e8ef509d083e3cc3ac31f82fd'
address = '0xC62DC5C6f306E67BF1e9D0346b579000Bc88b6c4'

#Connection
web3 = Web3(Web3.HTTPProvider(eth_url))
print('connection', web3.is_connected())

#check balance
file = open('wallet.txt')
total = 0
stt = 0
for line in file:
    balance = web3.eth.get_balance(line.strip())
    eth = web3.from_wei(balance,'ether')
    tx_count = web3.eth.get_transaction_count(line.strip())

    print(f'Wallet {stt}:', round(eth, 4),'ETH ----', tx_count, "transactions")
    total += eth
    stt += 1

#print total balance
print('total =', round(total, 4), "ETH")
