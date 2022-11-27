import json
import sys
import subprocess as sp
import re

MIN_STAKE_AMOUNT = 600 * 1000000000000000000


def bech32_convert_file(path: str, from_prefix: str, to_prefix: str = 'juno'):
    cmd = f'sh ./bech32-convert-file {path} {from_prefix} {to_prefix}'
    proc = sp.Popen(cmd.split(), stdout=sp.PIPE)
    return proc.stdout.read().decode()


def main():
    delegations = json.loads(bech32_convert_file('rebus-2330439.txt', 'rebus'))['delegation_responses']
    recipients = {}

    for record in delegations:
        delegation = record['delegation']
        juno_addr = delegation['delegator_address']
        rebus_amount = int(record['balance']['amount'])
        if rebus_amount >= MIN_STAKE_AMOUNT:
            recipients[juno_addr] = 0

    total = 0
    for k in recipients:
        amount = int(1 / len(recipients) * 1e6)
        recipients[k] = str(amount)
        total += amount
   
    print(total)
    with open('early-rebus-stakers-recipients-1.json', 'w') as fout:
        json.dump(recipients, fout)


if __name__ == '__main__':
    main()
