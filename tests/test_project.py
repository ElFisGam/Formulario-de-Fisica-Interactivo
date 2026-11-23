from src.project import nuke_accents,check_var_input,format_variables



def test_nuke_accents():
    assert nuke_accents("perro") == "perro"
    assert nuke_accents("árbol") == "arbol"


def test_check_var_input():
    assert check_var_input("aceleracion",{"aceleracion": "a"}) == True
    assert check_var_input("cat",{"aceleracion": "a"}) == False

def test_format_variables():
    assert format_variables(["aceleracion"],{"aceleracion": "a"}) == {"aceleracion": "a"}