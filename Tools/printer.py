import shutil
from Tools.colors import colors as c
def printer(sym):
	conwidth = shutil.get_terminal_size().columns
	print(f"{c.w}"+conwidth * sym)
