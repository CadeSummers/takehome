import pandas as pd
import seaborn as sns
import numpy as np
from time import time
from matplotlib import pyplot as plt

#creating instances of all pages as tables in pandas fron excel

def a_admission_types():

    start = time()

    data = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx", sheet_name = "Data")

    avail_24hr_df = data.filter(regex = r"(AVAIL24HRS|_adm|year)")
    avail_24hr_df.dropna(how='all', axis=1, inplace=True)
    avail_24hr_df.dropna(how='all', axis=0, inplace=True)
    avail_on_call_df = data.filter(regex = r"(AVAIL_ON_CALL|_adm|year)")
    avail_on_call_df.dropna(how='all', axis=1, inplace=True)
    avail_on_call_df.dropna(how='all', axis=0, inplace=True)

    list24hrs = ['ED_ANESTH_AVAIL24HRS', 'ED_LAB_SVCS_AVAIL24HRS', 'ED_OP_RM_AVAIL24HRS', 'ED_PHARM_AVAIL24HRS', 'ED_PHYSN_AVAIL24HRS',
    'ED_PSYCH_ER_AVAIL24HRS', 'ED_RADIOL_SVCS_AVAIL24HRS']

    list_24hr_dfs = []

    for column in list24hrs:

        list_24hr_dfs.append(avail_24hr_df[avail_24hr_df[column] == "YES"])
    
    list_oncall_dfs = []

    listoncall = ['ED_ANESTH_AVAIL_ON_CALL', 'ED_LAB_SVCS_AVAIL_ON_CALL', 'ED_OP_RM_AVAIL_ON_CALL', 'ED_PHARM_AVAIL_ON_CALL', 'ED_PHYSN_AVAIL_ON_CALL', 'ED_PSYCH_ER_AVAIL_ON_CALL', 'ED_RADIOL_SVCS_AVAIL_ON_CALL']

    for column in listoncall:

        list_oncall_dfs.append(avail_on_call_df[avail_on_call_df[column] == "YES"])


    end = time() - start
    print("this program took this amount of time in seconds:")
    print(end)

    return (list_24hr_dfs, list_oncall_dfs)


def a_ambulance_diversion_hours():

    start = time()

    data = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx", sheet_name = "Data")

    avail_24hr_df = data.filter(regex = r"(AVAIL24HRS|_AMB_DIVERS_TOTL_HOURS|year)")
    avail_24hr_df.dropna(how='all', axis=1, inplace=True)
    avail_24hr_df.dropna(how='all', axis=0, inplace=True)
    avail_on_call_df = data.filter(regex = r"(AVAIL_ON_CALL|_AMB_DIVERS_TOTL_HOURS|year)")
    avail_on_call_df.dropna(how='all', axis=1, inplace=True)
    avail_on_call_df.dropna(how='all', axis=0, inplace=True)

    list24hrs = ['ED_ANESTH_AVAIL24HRS', 'ED_LAB_SVCS_AVAIL24HRS', 'ED_OP_RM_AVAIL24HRS', 'ED_PHARM_AVAIL24HRS', 'ED_PHYSN_AVAIL24HRS',
    'ED_PSYCH_ER_AVAIL24HRS', 'ED_RADIOL_SVCS_AVAIL24HRS']

    list_24hr_dfs = []

    for column in list24hrs:

        list_24hr_dfs.append(avail_24hr_df[avail_24hr_df[column] == "YES"])
    
    
    list_oncall_dfs = []

    listoncall = ['ED_ANESTH_AVAIL_ON_CALL', 'ED_LAB_SVCS_AVAIL_ON_CALL', 'ED_OP_RM_AVAIL_ON_CALL', 'ED_PHARM_AVAIL_ON_CALL', 'ED_PHYSN_AVAIL_ON_CALL', 'ED_PSYCH_ER_AVAIL_ON_CALL', 'ED_RADIOL_SVCS_AVAIL_ON_CALL']

    for column in listoncall:

        list_oncall_dfs.append(avail_on_call_df[avail_on_call_df[column] == "YES"])

    print(list_oncall_dfs[0]['year'])

    print(avail_24hr_df['EMS_AMB_DIVERS_TOTL_HOURS'])

    end = time() - start
    print("this program took this amount of time in seconds:")
    print(end)

    return (list_24hr_dfs, list_oncall_dfs)

def b_admission_types():

    start = time()

    data = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx", sheet_name = "Data")

    avail_24hr_df = data.filter(regex = r"(TRAUMA_CTR|_adm|year)")
    avail_24hr_df.dropna(how='all', axis=1, inplace=True)
    avail_24hr_df.dropna(how='all', axis=0, inplace=True)
    avail_on_call_df = data.filter(regex = r"(TRAUMA_CTR|_adm|year)")
    avail_on_call_df.dropna(how='all', axis=1, inplace=True)
    avail_on_call_df.dropna(how='all', axis=0, inplace=True)

    ped_trauma_list = ['Level I - Pediatric', 'Level I & Level I - Ped', 'Level I & Level II - Ped', 'Level II & Level II - Ped']
    non_ped_trauma_list = ['Level I', 'Level I & Level I - Ped', 'Level I & Level II - Ped', 'Level II', 'Level II & Level II - Ped', 'Level III', 'Level IV']

    pediatric_trauma_df = avail_24hr_df[avail_24hr_df["TRAUMA_CTR"].isin(ped_trauma_list)]
    non_pediatric_trauma_df = avail_24hr_df[avail_24hr_df["TRAUMA_CTR"].isin(non_ped_trauma_list)]

    end = time() - start
    print("this program took this amount of time in seconds:")
    print(end)

    return (pediatric_trauma_df, non_pediatric_trauma_df)

def b_ambulance_diversion_hours():

    start = time()

    data = pd.read_excel(r"C:\Users\cadet\Desktop\MedStar TakeHome\chhs-31ea2cfd-bc1c-4bde-9626-f41b97cc1b93\emergency-department-services-trends-2013-2017.xlsx", sheet_name = "Data")

    avail_24hr_df = data.filter(regex = r"(TRAUMA_CTR|_AMB_DIVERS_TOTL_HOURS|year)")
    avail_24hr_df.dropna(how='all', axis=1, inplace=True)
    avail_24hr_df.dropna(how='all', axis=0, inplace=True)
    avail_on_call_df = data.filter(regex = r"(TRAUMA_CTR|_AMB_DIVERS_TOTL_HOURS|year)")
    avail_on_call_df.dropna(how='all', axis=1, inplace=True)
    avail_on_call_df.dropna(how='all', axis=0, inplace=True)

    ped_trauma_list = ['Level I - Pediatric', 'Level I & Level I - Ped', 'Level I & Level II - Ped', 'Level II & Level II - Ped']
    non_ped_trauma_list = ['Level I', 'Level I & Level I - Ped', 'Level I & Level II - Ped', 'Level II', 'Level II & Level II - Ped', 'Level III', 'Level IV']

    pediatric_trauma_df = avail_24hr_df[avail_24hr_df["TRAUMA_CTR"].isin(ped_trauma_list)]
    non_pediatric_trauma_df = avail_24hr_df[avail_24hr_df["TRAUMA_CTR"].isin(non_ped_trauma_list)]

    print(avail_24hr_df['EMS_AMB_DIVERS_TOTL_HOURS'])

    end = time() - start
    print("this program took this amount of time in seconds:")
    print(end)

    return (pediatric_trauma_df, non_pediatric_trauma_df)
