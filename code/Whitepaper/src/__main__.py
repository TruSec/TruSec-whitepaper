# This is the main code of this project nr, and it manages running the code and
# outputting the results to latex.
from .Main import Main
from .latex_export_code import export_code_to_latex
from .latex_compile import compile_latex
from .plantuml_generate import generate_all_dynamic_diagrams
from .plantuml_compile import compile_diagrams_in_dir_relative_to_root
from .plantuml_to_tex import export_diagrams_to_latex


print(f"Hi, I'll be running the main code, and I'll let you know when I'm done.")
project_name = 4
project_name="Whitepaper"

# Specify code configuration details
comile_locally = False
await_compilation = True
verbose = True
gantt_extension = ".uml"
diagram_extension = ".png"

# Specify paths relative to root.
jar_path_relative_from_root = f"code/{project_name}/src/plantuml.jar"
path_to_dynamic_gantts = f"code/{project_name}/src/Diagrams/Dynamic"
path_to_static_gantts = f"code/{project_name}/src/Static_diagrams"
dynamic_diagram_output_dir_relative_to_root = (
    f"latex/{project_name}/Images/Diagrams"
)



main_latex_filename = "report.tex"

## Run main code.
main = Main(project_name)

## PlantUML
# Generate PlantUML diagrams dynamically (using code).
#generate_all_dynamic_diagrams(f"code/{project_name}/src/Diagrams/Dynamic")

# Compile dynamically generated PlantUML diagrams to images.
#compile_diagrams_in_dir_relative_to_root(
#    await_compilation,
#    gantt_extension,
#    jar_path_relative_from_root,
#    path_to_dynamic_gantts,
#    verbose,
#)

# Compile statically generated PlantUML diagrams to images.
compile_diagrams_in_dir_relative_to_root(
    await_compilation,
    gantt_extension,
    jar_path_relative_from_root,
    path_to_static_gantts,
    verbose,
)


# Export PlantUML text files to LaTex.
export_diagrams_to_latex(
    path_to_dynamic_gantts,
    gantt_extension,
    dynamic_diagram_output_dir_relative_to_root,
)

# Export PlantUML diagram images to LaTex.
export_diagrams_to_latex(
    path_to_dynamic_gantts,
    diagram_extension,
    dynamic_diagram_output_dir_relative_to_root,
)


## Plotting
# Generate plots.

# Export plots to LaTex.


## Export code to LaTex.
# TODO: verify whether the latex/{project_name}/Appendices folder exists before exporting.
# TODO: verify whether the latex/{project_name}/Images folder exists before exporting.
export_code_to_latex(main_latex_filename, project_name)


## Compile the accompanying LaTex report.
compile_latex(True, project_name, True)

print(f"\n\nDone.")
