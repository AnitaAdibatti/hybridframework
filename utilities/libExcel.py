import pandas as pd


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


