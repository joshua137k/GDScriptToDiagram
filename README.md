# GDScriptToDiagram
I created this script to automatically convert our .gd code files into diagrams. To use it, you just need to provide the path to your project in the input prompt. The script will automatically locate all .gd files in your project and search for the chosen parameters, in my case the class_name.

The script then creates a dictionary using the class_name as the key and all functions found in these scripts as the value. Afterwards, it searches the scripts again to check if there is any script that has an extends with a value equal to a key in the dictionary. If it exists, the script adds this script to the value list of the corresponding classname key.

Finally, the script prints the resulting dictionary in JSON format.


To convert the JSON into a diagram, you can use this website:
https://jsoncrack.com/editor
