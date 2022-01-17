# This script converts Wikiversity multiple-choice questions with choice-specific feedback to a standard Respondus format.

# import package
import pandas as pd

# set display options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# create lists to read in lines, questions, choices, and feedback
mylines = []
Question_Wording = []
Title_ID = []
Choice_1 = []
Choice_2 = []
Choice_3 = []
Choice_4 = []
Feedback_1 = []
Feedback_2 = []
Feedback_3 = []
Feedback_4 = []

# create lists of lists and tuples
fieldnames = [Title_ID, Question_Wording, Choice_1, Feedback_1, Choice_2, Feedback_2, Choice_3, Feedback_3, Choice_4, Feedback_4]
tuple_fieldnames = ()

# set increment variables 
question = 0 
count = 1
adjust = 0 # this variable is used to restart the count after each 10-line question

# read in lines based on this approach # Try this approach https://www.computerhope.com/issues/ch001721.htm
with open ('questions.txt', 'rt', encoding="utf8") as myfile: 
    for myline in myfile:
        myline = myline.strip("+-|\n") # remove extra characters
        mylines.append(myline)        
# if the first character of the line is { add the line to the Question_Wording and Title_ID lists and increment question number
        if myline[0] == "{":   
            myline_clean = myline.replace("{","")
            Question_Wording.append(myline_clean)
            Title_ID.append(myline_clean)
            question += 1
# increment adjustment when starting a new question
        adjust = 10 + count - (question * 10)
# add choice and feedback to their corresponding lists based on their position in the question file
        for linenum in range (3, 11):
            if linenum in {count, adjust}:
                fieldnames[linenum-1].append(myline)  
        count += 1

# Create tuples from lists
tuples = [tuple(fieldname) for fieldname in fieldnames]
print(tuples)

# create data frame with questions as columns and elements as rows
data = tuples 
df=pd.DataFrame.from_records(data)

# transpose data frame so each question is a row with 10 columns
df_transposed = df.T

# add column names
df_transposed.columns =['Title_ID', 'Question_Wording', 'Choice_1', 'Feedback_1', 'Choice_2', 'Feedback_2', 'Choice_3', 'Feedback_3', 'Choice_4', 'Feedback_4']

# Create list with MC for Multiple Choice as Type for each question
Type = ['MC'] * question

# Create list with 1 for Points for each question
Points = [1] * question

# Create list with 4 for Correct Answer for each question
Correct_Answer = [4] * question

# Using DataFrame.insert() to add a columns Type, Points, and Correct answer with their respective default values
# These columns are inserted to match the Respondus template order
df_transposed.insert(0, "Type", Type, True)
df_transposed.insert(2, "Points", Points, True)
df_transposed.insert(3, "Correct_Answer", Correct_Answer, True)

# Print dataframe to check output
print(df)

# export to .csv in Respondus template format
df_transposed.to_csv("questions.csv", encoding='utf-8', index=False)



