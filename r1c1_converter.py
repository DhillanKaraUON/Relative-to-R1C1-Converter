import re
import pyperclip


def int_to_letter(n):
    name = ''
    while n: n, r = divmod(n - 1, 26); name = chr(r + ord('A')) + name
    return name


def letter_to_int(name):
    return int(sum((ord(c) - ord('A') + 1) * 26 ** i for i, c in enumerate(name[::-1])))


def row(cell):
    return int(re.findall(r"[^\W\d_]+|\d+", cell)[1])
                      
def col(cell):
    return re.findall(r"[^\W\d_]+|\d+", cell)[0]

def relative(origin,target_cell):
    origin_row_int = row(origin)
    origin_col_int = letter_to_int(col(origin))

    target_row_int = row(target_cell)
    target_col_int = letter_to_int(col(target_cell))

    difference_row = f"[{target_row_int - origin_row_int}]" if (target_row_int - origin_row_int) != 0 else ""
    difference_col = f"[{target_col_int - origin_col_int}]" if (target_col_int - origin_col_int) != 0 else ""

    return f"R{difference_row}C{difference_col}"


relative_formula = "=IFERROR(IF(INT(M275)=INT(M275+J275),M275+J275,IF(INT(M275+J275)=M275+J275,WORKDAY(N275,1,HOLIDAY),N275)),Project_Start)"


origin_cell = "N270"

relative_cells_list = list(set(re.findall(r'[A-Z]+\d+', relative_formula))) #unique list of cells referenced
print(relative_cells_list)

r1c1_formula = relative_formula
for relative_cell_ii in relative_cells_list:
    r1c1_cell_ii = relative(relative_cell_ii,origin_cell)
    
    r1c1_formula = r1c1_formula.replace(relative_cell_ii,r1c1_cell_ii)


pyperclip.copy(f"\"{r1c1_formula}\"")
print(f"\n\"{r1c1_formula}\"")


