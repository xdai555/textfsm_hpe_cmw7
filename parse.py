from textfsm import clitable
from pprint import pprint

def parse(cmd):
    cli_table = clitable.CliTable('index','templates')
    attr = {'Command':cmd,'Vendor':'hp_comware'}
    with open('raw_data') as f:
        cli_table.ParseCmd(f.read(),attr)
    print(cli_table)

parse("dis dev man")