from bip_eos.compiler.frontend.symbol_table import SymbolTable


def test_symbol_table_define():
    table = SymbolTable()
    table.define("x", 1)
    assert table.resolve("x") == 1
