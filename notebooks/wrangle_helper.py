def split_row(row, sep):
    """Given a string split by sep and return a tuple."""
    
    x = str(row).split(sep=sep)
#     print(x)
    if len(x) == 1:
        return str(x[0])
    else:
        return str(x[0]), str(x[1])
    
def split_tup(row):
    """Split the tuple to be inserted into 2 Pandas series"""
    
    if len(row) == 1:
        return row[0]
    else:
        return row[0], row[1]   
    
# Because the conditions differ slightly, I wrote 2 separate functions

def swap_job_living(job, area, job_status_correct, living_area_correct):
    """ 
    Check if job_status and living_area have been incorrectly entered. 
    If so swap the values into the other column. 
    """

    # print("job: {}\narea: {}".format(job, area))
    if (job in living_area_correct) & (area in job_status_correct):
        print("swap")
        return area, job
    else:
        print("don't swap")
        return job, area
    
def swap_sex_age(sex, age, sex_correct):
    """ 
    Check if age contains 'm' or 'f' we swap the values in the columns. 
    """
    
    # print("sex: {}\nage: {}".format(sex, age))
    if (age in sex_correct):
        print("swap")
        return age, sex
    else:
        print("don't swap")
        return sex, age