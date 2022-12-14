## About The Cost-Benefit Analysis Tool

- The Cost-Benefit Analysis Tool is a Python based GUI utility for scanning system vulnerabilities and providing results to assist in cost and benefit analysis for vulnerability resolution.

- This tool was desgined to work in tandem with the Nessus Essentials vulnerability scanner, as it parses .nessus export files.  

## Dependencies

- The Cost-Benefit Analysis Tool requires multiple dependencies:
- 1) PyQt5
- 2) PyQt5-Designer
- 3) SQLite3
- 4) PyInstaller
- 5) PyUic5
- 6) Xlsxwriter
- 7) Xml.etree.ElementTree
- 8) pip3

## Getting Started
- Make sure you have all of the Python dependencies installed.
```
pip install <above_dependency>
```
- Obtain a Nessus vulnerability export scan file ( *.nessus )
- Download the release .zip file for your operating system.
- Unzip the program where desireable.

## Running the Program
- Run the executable, either by clicking on the file, or from the terminal/command prompt.
- For Windows Command Prompt:
```
cd <path_to_executeable>
start CostBenefitAnalysisTool-Windows.exe
```
- For macOS terminal:
```
cd <path_to_executeable>
./CostBenefitAnalysisTool-MacSilicon
```
- For Linux terminal:
```
cd <path_to_executeable>
./CostBenefitAnalysisTool-Linux
```
