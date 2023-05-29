# Mini-cpu

Flowchart
![image](https://github.com/3bdallaaa/Mini-cpu/assets/118936824/f4fdccb3-a2c3-4db1-bc0f-c14e90a5f67d)

Output
![image](https://github.com/3bdallaaa/Mini-cpu/assets/118936824/38de940e-06b3-4de1-b437-daf96b388a2f)

A. General Namings:
 Lexial Analyzer (Scanner)
o The lexical analyzer is responsible for taking high-level language statements, scanning, and tokenizing them, generating a table that consists of lexemes and their corresponding tokens.
 Context-Free Grammar (C.F.G)
o To be able to continue the next phases, you have to design an appropriate C.F.G. The C.F.G. has to be as general as possible for the structure of given statement only.
 Syntax Analyzer (Parser)
o The syntax analyzer is responsible for utilizing the available (C.F.G) and processing the input to determine whether it conforms to the intended grammar rules.
 Sematnic Analyzer
o The sematnic analyzer is in charge of type-checking the parser output and ensuring that type conversion occurs in the event of a type mismatch. The output of this phase is a fully annotated syntax tree, which involves displaying the data type of each note as well as type conversions done in between.

B. The Parser
 The parser required for this project is Parse tree.
 This type of parser is a geometrical representation of the derived string.

C. The statement
 The statement to be implemented in this project is the switch…case statement.

c = 'X';
switch (c)
{
case 'N':
y = 30;
break;
case 'X':
y = 60;
break;
default:
y = 0;
break;
}
