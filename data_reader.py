import pandas as pd
import cleaner_saver as cs

def update_status_by_name(df_members, name, status='Present'):
    # update the status of a member by exact or reversed name match.
    exact_match = df_members[df_members['Name'] == name]
    if len(exact_match) == 1:
        df_members.loc[exact_match.index, 'Status'] = status
        return exact_match.index[0]
    reversed_name = cs.reverse_name(name)
    reversed_match = df_members[df_members['Name'] == reversed_name]
    if len(reversed_match) == 1:
        df_members.loc[reversed_match.index, 'Status'] = status
        return reversed_match.index[0]
    return None

def update_status_by_email(df_members, email, status='Present'):
    # update the status of a member by email match.
    email_match = df_members[df_members['Email'] == email]
    if len(email_match) == 1:
        df_members.loc[email_match.index, 'Status'] = status
        return email_match.index[0]
    return None

def update_status_by_partial_name(df_members, name, status='Present'):
    # update the status of a member by partial name match.
    possible_matches = df_members[df_members['Name'].str.contains(name, na=False)]
    if len(possible_matches) == 1:
        df_members.loc[possible_matches.index, 'Status'] = status
        return possible_matches.index[0]
    return None

def process_attendance(df_members, df_attendance):
    # process the attendance and update the status of members
    for index, row in df_attendance.iterrows():
        name = row['Name']
        email = row.get('Email', None)
        
        # try to update status by exact or reversed name
        member_index = update_status_by_name(df_members, name)
        
        if member_index is not None:
            df_attendance.at[index, 'Email'] = df_members.at[member_index, 'Email']
        else:
            # try to update status by email 
            if pd.notna(email):
                member_index = update_status_by_email(df_members, email)
                if member_index is not None:
                    continue
            
            # try to update status by partial name match
            member_index = update_status_by_partial_name(df_members, name)
            if member_index is not None:
                df_attendance.at[index, 'Email'] = df_members.at[member_index, 'Email']
            else:
                df_attendance.at[index, 'Email'] = None

def data_mage(members_file, attendance_file, output_dir):
    try:
        # load the files into DataFrames
        df_members = pd.read_excel(members_file)
        df_attendance = pd.read_excel(attendance_file)

        # convert all text data to lower case for case insensitive comparison
        df_members = df_members.apply(lambda x: x.astype(str).str.lower())
        df_attendance = df_attendance.apply(lambda x: x.astype(str).str.lower())

        # clean the 'Name' column
        df_members['Name'] = df_members['Name'].apply(cs.clean_name)
        df_attendance['Name'] = df_attendance['Name'].apply(cs.clean_name)

        # create 'Status' column and set default value to 'Absent'
        df_members['Status'] = "Absent"

        # process attendance
        process_attendance(df_members, df_attendance)

        # save the results
        cs.save_results(df_members, df_attendance, output_dir)
        
    except PermissionError as e:
        print(f"An error occurred: {e}. Please check if the file is open in another program or if you have the necessary permissions.")

