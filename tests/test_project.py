from src.project import nuke_accents



def test_nuke_accents():
    assert nuke_accents("perro") == "perro"
    assert nuke_accents("árbol") == "arbol"