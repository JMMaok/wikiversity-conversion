# wikiversity-conversion
Script to convert Wikiversity multiple choice quiz question format to Respondus template compatible with many learning management systems.
This script converts Wikiversity single-response multiple-choice questions with choice-specific feedback to a standard format.
This standard format can be used or adapted to import questions into many learning management systems.

**Instructions**
Create a file <questions.txt> containing single-response multiple choice questions in Wikiversity format. The easiest way to do this is to copy the source from Wikiversity.
The Wikiversity question format is found here: https://en.wikiversity.org/wiki/Help:Quiz
The script is designed for questions with 4 choices with the correct choice in position 4.
Prepare your <questions.txt> file by deleting any extra blank lines and any spaces before the first word of questions, choices, and feedback.
A sample <questions.txt. file is provided.

**What if the correct choice is not in postion 4?**
If the correct choice is not in position 4, use cut and paste to move the correct choice **and** its corresponding feedback to position 4.
Many learning management systems have settings that will allow you to randomize the order of the choices after you import them.
Alternative approach: Leave the correct choice in its position and manually change the Correct_Answer field in the <questions.csv> file after running the script.

**Output**
This script creates a file <questions.csv> in the Respondus template format. For best results, import the output from this script into your spreadsheet as UTF-8.
You can just open the .csv file in the spreadsheet, but you will probably have some special characters convert incorrectly.
More information about the Respondus template format can be found here: Formatting Guidelines for  Respondus  4.0  Exam  Converter: http://www.uwyo.edu/lms/wyocourses/improved/respondustabsfolder/exam_formatting.pdf
