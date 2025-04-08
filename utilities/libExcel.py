from xlrd import open_workbook
import pandas as pd

"""def locators(sheetname):
    book = open_workbook(r"pathOfLocatorFile")
    sheet = book.sheet_by_name(sheetname)
    data = {}
    used_rows = sheet.nrows
    for i in range(1, used_rows):
        row = sheet.row_values(i)
        setattr(data, row[0], (row[1], row[2]))
    return data"""

# class decorator where fieldname is attr name and tuple of locatortype and locatorvalue is attr value
# using xlrd
"""def attach_elements(sheetname):
    def _locators(cls):
        book = open_workbook(r"path_of_locators_file")
        sheet = book.sheet_by_name(sheetname)

        used_rows = sheet.nrows
        for i in range(1,used_rows):
            row = sheet.row_values(i)
            setattr(cls,row[0],(row[1],row[2]))
        return cls
    return _locators"""

# using pandas with openpyxl
def read_locator(sheetname):
    def _locators(cls):
        df = pd.read_excel(r"C:\Users\Anita\PycharmProjects\hybridFramework\data\locators.xlsx", sheet_name=sheetname,
                           engine="openpyxl")  # Recommended for `.xlsx` files
        total_rows = df.shape[0]
        for i in range(total_rows):
            row = df.iloc[i].values.tolist()
            setattr(cls,row[0],(row[1],row[2]))
        return cls
    return _locators

def read_headers(sheetname,test_case_name):
    df = pd.read_excel(r"C:\Users\Anita\PycharmProjects\hybridFramework\data\testdata.xlsx", sheet_name=sheetname,
                       engine="openpyxl")
    total_rows = df.shape[0]
    for i in range(1,total_rows):
        if df.iloc[i].values.tolist()[0] == test_case_name:
            return ','.join(df.iloc[i-1].dropna().tolist()[2:])

def read_valid_data(sheetname,test_case_name):
    df = pd.read_excel(r"C:\Users\Anita\PycharmProjects\hybridFramework\data\testdata.xlsx", sheet_name=sheetname,
                       engine="openpyxl")
    total_rows = df.shape[0]
    final_data = []
    for i in range(1,total_rows):
        if df.iloc[i].values.tolist()[0] == test_case_name and df.iloc[i].values.tolist()[1]=='valid':
            final_data.append(tuple(df.iloc[i].dropna().tolist()[2:]))
    return final_data

def read_invalid_data(sheetname,test_case_name):
    df = pd.read_excel(r"C:\Users\Anita\Downloads\testdata.xlsx", sheet_name=sheetname,
                       engine="openpyxl")
    total_rows = df.shape[0]
    final_data = []
    for i in range(1,total_rows):
        if df.iloc[i].values.tolist()[0] == test_case_name and df.iloc[i].values.tolist()[1]=='invalid':
            final_data.append(tuple(df.iloc[i].dropna().tolist()[2:]))
    return final_data

"""def read_headers(sheetname,test_case_name):
    book = open_workbook(r"C:Users\Anita\Downloads\estdata.xlsx")
    sheet = book.sheet_by_name(sheetname)
    used_rows = sheet.nrows
    for i in range(0,used_rows):
        row = sheet.row_values(i)
        # print(row)
        if row[0] == test_case_name:
            headers = sheet.row_values(i-1)
            valid_headers = [header.strip() for header in headers if header.strip()]
            return ','.join(valid_headers[2:])"""
# read_headers('smoke','test_createcampaign')

"""def read_data(sheetname,test_case_name):
    book = open_workbook(r"path_of_test_data_file")
    sheet = book.sheet_by_name(sheetname)
    used_rows = sheet.nrows
    final_data = []
    for i in range(0, used_rows):
        row = sheet.row_values(i)
        if row[0] == test_case_name:
            temp_record = [item.strip() for item in row if item.strip()]
            if temp_record[1].upper() == 'YES':
                final_data.append(tuple(temp_record[2:]))
    return final_data"""