# Attendance-Tracking
A Python script to automate the attendance tracking process for learners, significantly reducing manual effort and improving efficiency.

<img src = "(https://github.com/Terry-Migwi/Attendance-Tracking/blob/main/assets/images/assets/images/attendance_tracking_ui.png)" width = "600" height = "600"> 

### Project Overview
This project was developed to automate the learner attendance tracking process to reduce manual work and save time. Previously, marking attendance manually for approximately 100 learners took me about 30 minutes per session. With two sessions per week, that added up to 2 hours of repetitive work every week. To streamline this task, I created a Python script that now completes the process in under 5 minutes.

#### How it works:
1. I maintain a spreadsheet with all learners' names and email addresses.
2. After each session, I receive a separate spreadsheet with the emails of attendees.
3. The script compares the two files, identifies absentees, and generates a separate spreadsheet listing them.

This output simplifies the process of updating the attendance system—especially since it defaults to marking everyone as present.

#### Results:
1. Reduced attendance tracking time from 2 hours/week to under 10 minutes/week
2. Eliminated redundant manual tasks
3. Created a reliable and repeatable workflow for future sessions

### Packages Used
Data Preparation and Cleaning - Pandas, Regular Expressions, Cleaners Saver

User Interface - tkinter

### Resources Used
Python 3

### Code Structure
#### cleaner_saver.py
This script handles data pre-processing and cleaning. Key steps include:

1. Stripping unwanted characters (e.g., punctuation) from learner names.
2. Normalizing name order to address inconsistencies between files—for example, converting names listed as "Last Name, First Name" in attendance records to match the "First Name Last Name" format in the main list.
3. This ensures accurate matching of learners across both datasets.

#### data_reader.py
This is the core matching script responsible for updating attendance status. It includes:

1. Three functions to mark students as present by matching their Full name, Email address, and Partial name (for flexibility in cases of name formatting inconsistencies)
2. A combined function that consolidates these three checks to update each learner’s attendance status.
3. A final function that compares the updated main list and identifies absent learners, saving the results in a separate file.

#### get_file.py
This utility script prompts the user to input the file paths for:

1. The main learner list (with names and email addresses)
2. The session attendance file
3. This makes the script adaptable to different file inputs each time it's run.

#### ui_test.py
This is the graphical user interface (GUI) component built using Tkinter. It provides a simple, interactive front end for users to:

1. Select input files
2. Run the attendance script
3. View or access the generated output files

### Data Challenges and Resolutions
1. Missing Email Addresses:
Some learners attended sessions without including their email addresses—the primary identifier used for matching records.
Resolution: These cases were flagged and moved to a separate spreadsheet labelled "Unresolved Learners" for manual follow-up.

2. Inconsistent Name Structure:
Name formats varied between files. In the main file, names appeared as First Name Last Name, while in the attendance file, some were reversed to Last Name First Name.
Resolution: A name-cleaning step was introduced in the script to standardize and normalize name order, improving the accuracy of the matching process.
