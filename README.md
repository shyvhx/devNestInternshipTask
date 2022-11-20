# devNestInternshipTask
Task required to apply for the GO internship
Requirements
Write a service which receives a CSV formatted string input(ex: input_example), and returns a new string(ex: output_example) with the following requirements:



Remove the header
Remove duplicates
Group the data by the first letter of the field "full_name"




input_example:

----------------------------------------------------

full_name, email, location

Anita, anita@email.com, California

Aron, aron.bla@email.com, California

Aron, aron.bla@email.com, California

Cosmin, kox@bla.com, Giurgiu

Crina, ggl@test.com, Letcani

Bogdan, vox@example.com, Resita

----------------------------------------------------



output_example:

----------------------------------------------------

A:

Anita, anita@email.com, California

Aron, aron.bla@email.com, California



C:

Cosmin, kox@bla.com, Giurgiu

Crina, ggl@test.com, Letcani



B:

Bogdan, vox@example.com, Resita

----------------------------------------------------



for both input and output, every row/line ends with a new line character, exactly as it displays in the examples
it's not mandatory to order the data alphabetically
the header from the input "full_name, email, location" is not needed in the output, exactly as it displays in the example



IN ORDER TO RUN THE APP:
1. Add CSV formatted string in the input_example.txt file.
2. Run the main.py file with python
3. Check output in the output.txt file



