# Main code that performs computations for this project.


class Main:
    """ """

    def __init__(self, project_name):
        # Path related variables
        self.project_name = project_name
        self.relative_src_filepath = f"code/{project_name}/src/"

        # PlantUML related variables
        self.plant_uml_java_filename = "plantuml.jar"
        self.relative_plant_uml_java_filepath = (
            f"code/{project_name}/src/{self.plant_uml_java_filename}"
        )
        self.diagram_dir = "Diagrams"
        self.static_diagram_dir = "Static_diagrams"
        self.src_to_diagram_path = f"{self.relative_src_filepath}{self.diagram_dir}/"
        self.gantt_text_extension = ".uml"

        # Run main code.
        print(f"5+2={self.add_two(5)}")

    def add_two(self, x):
        """adds two to the incoming integer and returns the result of the computation.

        :param x: Integer number.

        """
        return x + 2


if __name__ == "__main__":
    # initialize main class
    main = Main()
