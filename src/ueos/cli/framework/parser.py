import argparse

def create_parser():
    p=argparse.ArgumentParser(prog="ueos")
    p.add_argument("system",nargs="?")
    p.add_argument("command",nargs="?")
    p.add_argument("arguments",nargs="*")
    return p
