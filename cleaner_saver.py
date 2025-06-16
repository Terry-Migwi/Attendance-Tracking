import os
import pandas as pd
import pprint
import re

def clean_name(name):
    # clean the name by removing unwanted parts and formatting it properly.
    name = re.sub(r'\s*\(.*?\)', '', name).strip()
    if ',' in name:
        parts = name.split(',')
        name = ' '.join(part.strip() for part in reversed(parts))
    return name

def reverse_name(name):
    #  reverse the order of names
    parts = name.split()
    if len(parts) > 1:
        name = ' '.join(reversed(parts))
    return name

def save_results(df_members, df_attendance, output_dir):
    # save the results to new Excel files.
    absent_students = df_members[df_members['Status'] == 'Absent'].apply(lambda x: x.astype(str).str.title())
    present_students = df_members[df_members['Status'] == 'Present'].apply(lambda x: x.astype(str).str.title())
    unresolved_students = df_attendance[pd.isna(df_attendance['Email']) & 
                                        (df_attendance['Name'].str.split().str.len() == 1) & 
                                        (~df_attendance['Name'].isin(df_members['Name']))].apply(lambda x: x.astype(str).str.title())

    os.makedirs(output_dir, exist_ok=True)
    absent_students.to_excel(os.path.join(output_dir, 'absent_students.xlsx'), index=False)
    present_students.to_excel(os.path.join(output_dir, 'present_students.xlsx'), index=False)
    df_attendance.apply(lambda x: x.astype(str).str.title()).to_excel(os.path.join(output_dir, 'updated_attendance.xlsx'), index=False)
    unresolved_students.to_excel(os.path.join(output_dir, 'unresolved_students.xlsx'), index=False)

    pprint.pp(f"There are { absent_students.shape[0]}  absent students.")
   #  pprint.pp(absent_students)