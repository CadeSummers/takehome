import pandas as pd
import seaborn as sns
import numpy as np
from time import time

#creating instances of all pages as tables in pandas fron excel

start = time()

profile_summary_page = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx",index_col=0, header=0, sheet_name = "Profile Summary Page")
pivot_selection = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx", sheet_name = "Pivot Selection")
data = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx", sheet_name = "Data")
#notes = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx", sheet_name = "Notes")
#glossary = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx", sheet_name = "Glossary")

#manual declaration of strings denoting subtables, and the row indeces at which they occur in sheets.
#For this report, these values are hardcoded, expect future processes to be dynamically coded 
subtables = {

"PIVOT SELECTIONS" : (0, 13),
"Emergency Departments" : (14,21),
"Designated Trauma Centers" : (22,31),
"ED Services Available" : (32,40),
"ED Patient Treatment Stations": (41,45),
"EMS Visit by Type" : (46,56),
"EMS Admissions" : (57,66),
"Other ED Visits" : (67,77),
"ED - Ambulance Diversion" : (78,83),
"Ambulance Diversion Hours" : (84, 99)

}

#iloc format: first argument denotes row ( :13 grabs up to some row 13), second argument denotes columns (0: grabs all columns from first onwards )
#eg: df_1 = profile_summary_page.iloc[:13, 0:]

#naming convention, psp_name = subtables['name'] will create a table from the profile summary page, based on the dict defining the subtables
#declarations of all subtables in the profile summary page
psp_pivot_selections = profile_summary_page.iloc[subtables["PIVOT SELECTIONS"][0]:subtables["PIVOT SELECTIONS"][1]]
psp_emergeny_departments = profile_summary_page.iloc[subtables["Emergency Departments"][0]:subtables["Emergency Departments"][1]]
psp_designated_trauma_centers = profile_summary_page.iloc[subtables["Designated Trauma Centers"][0]:subtables["Designated Trauma Centers"][1]]
psp_ed_services_available = profile_summary_page.iloc[subtables["ED Services Available"][0]:subtables["ED Services Available"][1]]
psp_patient_treatment_stations = profile_summary_page.iloc[subtables["ED Patient Treatment Stations"][0]:subtables["ED Patient Treatment Stations"][1]]
psp_ems_visit_by_type = profile_summary_page.iloc[subtables["EMS Visit by Type"][0]:subtables["EMS Visit by Type"][1]]
psp_ems_admissions = profile_summary_page.iloc[subtables["EMS Admissions"][0]:subtables["EMS Admissions"][1]]
psp_other_ed_visits = profile_summary_page.iloc[subtables["Other ED Visits"][0]:subtables["Other ED Visits"][1]]
psp_ed_ambulance_diversion = profile_summary_page.iloc[subtables["ED - Ambulance Diversion"][0]:subtables["ED - Ambulance Diversion"][1]]
psp_ambulance_diversion_hours = profile_summary_page.iloc[subtables["Ambulance Diversion Hours"][0]:subtables["Ambulance Diversion Hours"][1]]

psp_subtables = [psp_pivot_selections, psp_emergeny_departments, psp_designated_trauma_centers, psp_ed_services_available, psp_patient_treatment_stations, psp_ems_visit_by_type, psp_ems_admissions, psp_other_ed_visits, psp_ed_ambulance_diversion, psp_ambulance_diversion_hours]

#remove void values

#remove all void values and give all columns year name after the first subtable
for subtable in psp_subtables[1:]:

    #drop all void columns, first by column then by row
    subtable.dropna(how='all', axis=1, inplace=True)
    subtable.dropna(how='all', axis=0, inplace=True)

    #and rename columns
    if subtable.shape[1] == 5:
        subtable.columns = ['2013', '2014', '2015', '2016', '2017']
    #otherwise create a 2013a and 2013b column
    else:
        subtable.columns = ['2013a', '2013b', '2014a', '2014b', '2015a',' 2015b', '2016a', '2016b', '2017a', '2017b']




'''
#print information
for subtable in psp_subtables:
    print("---------------------------------------------------------------------------")
    print(subtable)
    print("---------------------------------------------------------------------------")
print(data)
'''
'''
avail_24hrs = "AVAIL24HRS"
avail_on_call = "AVAIL_ON_CALL"

#for every column_name
for column_name in data.iloc[:0]:
    #if suffix is AVAIL24HRS
    if column_name[-1*len(avail_24hrs):]:
        #TODO commit to 24hr dataframe
        pass
    #if suffix is AVAIL_ON_CALL
    elif column_name[-1*len(avail_24hrs):]:
        #TODO commit to avail_on_call dataframe
        pass
    else:
'''


#print(psp_ambulance_diversion_hours)
end = time() - start
print("this program took this amount of time in seconds:")
print(end)



#GENERAL OUTLINE:
#1. Isolate all tables (done)
#1.1. Isolate all tables from other sheets of data as well (done)
#2. Split tables containing subtables into distinct tables as well. (done)
#2.1 The key comparison we are making is between facilities who have 24hr operations and on-call operations. These are denoted by the suffixes 'AVAIL24HRS' and 'AVAIL_ON_CALL'
#2.1.1 We want to split the data table 'data' into tables based on the above, where we can compares AVAIL24HRS, AVAIL_ON_CALL, and likely a 'BOTH' and a 'NEITHER' table.
#2.2 Organize data from data table to be viewed with admissions (columns whose name ends with '_adm') as the primary focus key
#2.3 Organize data from data table to be viewed with admmissions (columns whose name contains 'AMB_DIVERS') as the primary focus key
#2.4 Compare between facilites who have 24hr operations vs on-call operations
#3. Perform comparison analysis based on isolated subtables
#4. Use seaborn to generate graphs
#5. Create reports using graph information