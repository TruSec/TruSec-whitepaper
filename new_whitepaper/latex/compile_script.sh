#!/bin/bash
# compiles the latex report in project 7. Run from /latex/project7/ directory.

## Specify global variables that are used in this script.
PROJECT_ID=8
PROJECT_FOLDERNAME="project"
REPORT_FILENAME="report"
PATH_TO_REPORT_TEX="latex/$PROJECT_FOLDERNAME$PROJECT_ID"
PATH_TO_REPORT_TEX_FILE="$PATH_TO_REPORT_TEX/$REPORT_FILENAME.tex"
OUTPUT_DIR="output"
OUTPUT_PATH="$PATH_TO_REPORT_TEX/$OUTPUT_DIR"


## Specify the functions that are used in this script.
#######################################
# Checks if directory/path exists, throws error if it does not exist.
# Local variables:
# dir
# Globals:
#  None.
# Arguments:
#  dir - The path to the directory that is being checked for existance.
# Returns:
#  0 if the directory exists.
#  4 if the directory does not exist
# Outputs:
#  FOUND if the directory exists.
#######################################
assert_dir_exists() {
	local dir=$1 
	if [ -d "$dir" ]; then
		echo "FOUND" 
	else
		echo "The directory:$dir does not exist."
		exit 4
	fi
}


#######################################
# Checks if file/filepath exists, and returns FOUND/NOTFOUND accordingly.
# Local variables:
# filepath
# Globals:
#  None.
# Arguments:
#  filepath - The path to the file that is being checked for existance.
# Returns:
#  0 if the function is executed succesfully.
# Outputs:
#  FOUND if the file exists.
#  NOTFOUND if the file does not exist.
#######################################
assert_file_exists() {
	local filepath=$1 
	if [ -f "$filepath" ]; then
		echo "FOUND" 
	else
		echo "The file:$filepath does not exist."
		exit 4
	fi
}


#######################################
# Checks if the current path is the root directory of this project, throws
# error if it does not exist.
# Local variables:
# output_path
# output_path_length
# current_path
# last_characters_of_current_path
# Globals:
#  None.
# Arguments:
#  output_path - The path of the latex compilation output directory.
# Returns:
#  0 if the directory exists.
#  5 if the directory does not exist
# Outputs:
#  FOUND if the directory exists.
#######################################
assert_current_directory_is_output_dir() {
	local output_path="$1"
	local output_path_length=${#output_path}

	local current_path=$PWD
	local last_characters_of_current_path=${current_path:(-$output_path_length)}
	if [[ $last_characters_of_current_path == $output_path ]]; then
		echo "FOUND"
	else
		echo "ERROR, the last characters of current path:$last_characters_of_current_path is not equal to the output path:$output_path"
		exit 5
	fi
}


#######################################
# Checks if the current path is the root directory of this project, returns
# FOUND/NOTFOUND accordingly. This check is performed by checking if the 
# report.tex file is found at the relative position it would be in, as seen 
# from the root directory.
# Local variables:
# path_to_report_tex_file
# Globals:
#  None.
# Arguments:
#  path_to_report_tex_file - The path to the report.tex as seen from root dir.
# Returns:
#  0 if the function is evaluated successfully.
# Outputs:
#  FOUND if the report.tex exists at the expected relative position.
#  NOTFOUND if the report.tex exists at the expected relative position.
#######################################
is_root_dir() {
	local path_to_report_tex_file="$1"
	if [ -f "$path_to_report_tex_file" ] ; then
		echo "FOUND"
	else
		echo "NOTFOUND"
	fi
}


#######################################
# Checks if the current path is the root directory of this project. This check
# is performed by checking if the report.tex file is found at the relative 
# position it would be in, as seen from the root directory. Throws error if the
# file is not found at the expected relative position.
# Local variables:
# path_to_report_tex_file
# Globals:
#  None.
# Arguments:
#  path_to_report_tex_file - The path to the report.tex as seen from root dir.
# Returns:
#  0 if the report.tex exists at the expected relative position.
#  6 if the report.tex exists at the expected relative position.
# Outputs:
#  FOUND if the report.tex exists at the expected relative position.
#######################################
assert_is_root_dir() {
	local path_to_report_tex_file="$1"
	if [ -f "$path_to_report_tex_file" ] ; then
		echo "FOUND"
	else
		echo "ERROR, the current path:$PWD is not the root directory."
		exit 6
	fi
}


## Ensure the script is executed from the root directory.
if [ "$(is_root_dir $PATH_TO_REPORT_TEX_FILE)" == "FOUND" ] ; then
	echo "FOUND"
else
	# Get lenght of expected subdir
	expected_path_length=${#PATH_TO_REPORT_TEX}
	if [[ "${PWD: -$expected_path_length}" == "$PATH_TO_REPORT_TEX" ]]; then
		cd ../..
		if [ "$(is_root_dir $PATH_TO_REPORT_TEX_FILE)" == "FOUND" ] ; then
			echo "FOUND"
		else
			exit "The script should be able to go up into the root directory with two parents, but it did not."
			exit 20
		fi
	else
		exit "You are calling this script from the wrong directory. PWD=$PWD"
		exit 21
	fi
fi


## Create clean output directories
# Clean up build artifacts prior to compilation.
rm -r $PATH_TO_REPORT_TEX/$OUTPUT_DIR/*
rmdir $PATH_TO_REPORT_TEX/$OUTPUT_DIR

# Create output directory
mkdir $OUTPUT_PATH
assert_dir_exists $OUTPUT_PATH

# Create relative dir from root to report.tex inside output dir 
# (for stylefile (for bibliograpy)).
mkdir -p $OUTPUT_PATH/$PATH_TO_REPORT_TEX
assert_dir_exists $OUTPUT_PATH/$PATH_TO_REPORT_TEX

# Copy zotero.bib file into output directory
cp zotero.bib $OUTPUT_PATH/zotero.bib
assert_file_exists "$OUTPUT_PATH/zotero.bib"

# Copy tudelft-report.bst file into relative directory from root to report.tex
# file, inside output directory:
cp "$PATH_TO_REPORT_TEX/tudelft-report.bst" "$OUTPUT_PATH/$PATH_TO_REPORT_TEX/tudelft-report.bst"
assert_file_exists "$OUTPUT_PATH/$PATH_TO_REPORT_TEX/tudelft-report.bst"


## Perform installation of required packages
# Verify the Dutch language package used by the TU Delft style files is installed.
yes | sudo apt install texlive-lang-european

# Install the roboto font used by the TU Delft style files.
yes | sudo apt install fonts-roboto
yes | sudo apt-get install texlive-fonts-extra

# Unused package.
#yes | sudo apt-get install texlive-science


## Compiling latex project.
echo "COMPILING"

# Compile cover
#xelatex cover.tex
#xelatex -output-directory=$OUTPUT_PATH $PATH_TO_REPORT_TEX/cover.tex

# Create some files needed for makeindex
pdflatex -output-directory=$OUTPUT_PATH $PATH_TO_REPORT_TEX/report

# Go into output directory to compile the glossaries
cd $OUTPUT_PATH
assert_current_directory_is_output_dir "$OUTPUT_PATH"

# Compiling from root directory files
makeindex report.nlo -s nomencl.ist -o report.nls

# Glossary
makeindex -s report.ist -t report.glg -o report.gls report.glo
 
# List of acronyms
makeindex -s report.ist -t report.alg -o report.acr report.acn

# Include glossary into report.
makeglossaries report

# Compile bibliography.
bibtex report

# Go back up into root directory
cd ../../..
assert_is_root_dir "$PATH_TO_REPORT_TEX_FILE"

# Recompile report to include the bibliography.
pdflatex -output-directory=$OUTPUT_PATH latex/project$PROJECT_ID/report
# Recompile report to include acronyms, glossary and nomenclature (in TOC).
pdflatex -output-directory=$OUTPUT_PATH latex/project$PROJECT_ID/report

## Post processing/clean-up.
# Move pdf back into "$PATH_TO_REPORT_TEX.
mv $OUTPUT_PATH/report.pdf "$PATH_TO_REPORT_TEX/report.pdf"

# Clean up build artifacts.
rm $OUTPUT_PATH/report.*