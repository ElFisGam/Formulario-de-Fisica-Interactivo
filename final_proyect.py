import csv
import pyfiglet
from tabulate import tabulate
from difflib import get_close_matches


def main():

    # ----------------------INIT------------------

    print_welcome()

    # Read physics equations from the file
    valid_formulas = read_formulas()
    available_words, format_dict = read_formatting()

    # Variable that will read the data from the user
    vars = []

    # --------------------------------------------

    # ---------------------INPUT------------------

    # Read the number of variables that the user will input
    num_var = get_num_var()

    # Read the variables and checks if the name is valid. If not, it gives a suggestion
    for i in range(num_var):
        while True:
            var_input = input(f"Escribe la variable número {i+1}: ").lower().strip()
            var_input = nuke_accents(var_input)
            if check_var_input(var_input, format_dict):
                vars.append(var_input)
                break
            else:
                print("El nombre de la variable no es válida, tal vez quisiste decir:")
                for word in get_close_matches(var_input, available_words):
                    print(word)

    # ----------------------------------------------

    # -----------------FORMATTING----------------------

    # Format the variables to be compared with the equations as a dictionary
    vars_format = format_variables(vars, format_dict)

    # --------------------------------------------------

    # ------------------COMPARISSION---------------------

    # Checks if each variable is in any equations, if so, it updates the valid_formulas list to only keep the ones with a match
    for var in vars_format.keys():
        valid_formulas = get_formula_list(vars_format[var], valid_formulas)

    # GETS A DICTIONARY OF ALL THE VARIABLES USED IN THE VALID FORMULAS
    vars_in_valid_formulas = {}
    for formula in valid_formulas:
        for var in formula["vars"]:
            for k, v in format_dict.items():
                if var == v and k not in vars_in_valid_formulas.keys():
                    vars_in_valid_formulas[k.capitalize()] = v

    # ---------------------------------------------------

    # ---------------------OUTPUT--------------------------

    # Writes the output to the user
    write_answer(valid_formulas, vars_in_valid_formulas.items())

    # -------------------------------------------------


def print_welcome():

    text = "Formulario Interactivo"

    print(pyfiglet.figlet_format(text, font="santa_clara"))

    print(
        "Te doy la bienvenida al formulario interactivo.\n\nPara encontrar la fórmula que necesitas, tendrás que indicar las variables que se utilizan en el problema. Considera tanto las variables"
        " que te dan como las variables que te piden encontrar. También, en algunos casos una misma variable aparece en 2 puntos diferentes o en un momento inicial y final, para ellas querrás "
        "indicar algo como 'velocidad inicial/velocidad final' o 'presión 1/presión 2.\n\nComienza indicando cuántas variables conoces. Recueda incluir la que te piden encontrar.\n"
    )


def read_formulas() -> list:
    """Loads the equations as a list of dictionaries"""
    formulas = []
    with open("data.csv", "r", encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["vars"] = row["vars"].split("-")
            formulas.append(row)
    return formulas


def read_formatting() -> list:
    """Loads only the words from the format file as a list"""
    words = []
    format = {}
    with open("format.csv", "r", encoding="utf-8",newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            words.append(row[0])
            format[row[0]] = row[1]
    return words, format


def get_num_var() -> int:
    """Reads the number of variables to be recieved by the user"""
    while True:
        try:
            num_var = int(
                input("¿Cuántas variables conoces del problema? (valor entre 1 y 8) ")
            )
            if not (0 < num_var < 9):
                print("Número inválido, por favor escribe un valor entre 1 y 8")
                continue
            return num_var
        except (TypeError, ValueError):
            print("Solo se admiten números enteros")
            continue


def nuke_accents(s) -> str:
    """Gets rid of the accents"""
    accents = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]
    for i, j in accents:
        s = s.replace(i, j)
    return s


def check_var_input(var, format_dict) -> bool:
    """Checks if the variable given by the user is valid"""
    if var in format_dict.keys():
        return True
    return False


def format_variables(variables, format_dict) -> dict:
    """Format the variables input by the user to the form they can be compared with the equations table"""
    new_vars = {}

    for var in variables:
        if var in format_dict.keys():
            new_vars[var] = format_dict[var]

    return new_vars


def get_formula_list(variable, formulas) -> list:
    """Checks in which formulas the given variables is and updates the list"""
    formulas_updated = []
    for formula in formulas:
        if variable in formula["vars"]:
            formulas_updated.append(formula)

    return formulas_updated


def write_answer(formula_list, variables_list):
    """Writes the final output"""
    if not formula_list:
        print(
            f"\n No fue posible encontrar una fórmula adecuada con las variables proporcionadas"
        )
    else:

        print(
            f"\nCon la información proporcionada, todo se redujo a {len(formula_list)} posibles fórmulas para resolver tu problema."
        )
        print(
            "\nLa siguiente tabla te ayudará a entender el significado de cada símbolo:\n"
        )

        print(tabulate(variables_list, tablefmt="grid"))

        print("\n FÓRMULAS:\n")

        final_table = []
        for formula in formula_list:

            final_table.append(
                [formula["subject"].capitalize(), formula["topic"].capitalize(), formula["equation"]]
            )

        print(tabulate(final_table, tablefmt="grid",headers=["Área","Tema","Fórmula"]))


if __name__ == "__main__":
    main()
