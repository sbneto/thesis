import os

os.chdir("./")
files_in_folder = os.listdir(".")
for figure_name in files_in_folder:
	if figure_name.endswith(".tex"):
		with open(figure_name, "r") as figure:
			content = figure.read()
			replacedContent = content.replace("\\{", "{").replace("\\}", "}").replace("\\_", "_").replace("\\^{}", "^").replace("\\$", "$").replace("\\ensuremath{\\backslash}","\\")
			if replacedContent!=content:
				with open(figure_name, "w") as write_figure:
					write_figure.write(replacedContent)
					print "Alteracao de tokens feita em " + figure_name
		
		if figure_name.startswith("[scale="):
			scale_str = "\\begin{tikzpicture}" + figure_name.partition("]")[0] + "]"
			with open(figure_name, "r") as figure:
				content = figure.read()
				if "\\begin{tikzpicture}[scale=" not in content:
					replacedContent = content.replace("\\begin{tikzpicture}", scale_str)
					if replacedContent!=content:
						with open(figure_name, "w") as write_figure:
							write_figure.write(replacedContent)
							print "Alteracao de escala feita em " + figure_name.partition("]")[2]
						figure.close()
						try:
							os.remove(figure_name.partition("]")[2])
						except OSError:
							pass
						os.rename(figure_name,figure_name.partition("]")[2])

#raw_input()
