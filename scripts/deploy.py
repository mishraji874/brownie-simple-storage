from brownie import accounts, config, SimpleStorage, network
from dotenv import load_dotenv
import os

load_dotenv()

def deploy_simple_storage():
    # # 1st way: getting the accounts from the local ganache server
    # account = accounts[0]
    # print(account)
    
    # #2nd way by creating a new account using ```brownie accounts new <account-name>``` and then add the private key and password to secure it
    # # for deleting the account use ```brownie accounts delete <account-name>``` amd to show the account list use ```brownie accounts list```
    # account = accounts.load("freecodecamp-account")
    # print(account)
    
    # #3rd way is to use environment variables and brownie config
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)
    
    # #another way using config file
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    #Transaction
    #Call
    print(simple_storage)
    
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()