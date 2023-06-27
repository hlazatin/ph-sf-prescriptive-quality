import numpy as np

def check_passing_wo(df, process):
    "Get work orders that passed"
    df = df.replace('',np.nan)
    df['Lower Specification Limit'] = df['Lower Specification Limit'].astype(float).fillna(-999_999)
    df['Upper Specification Limit'] = df['Upper Specification Limit'].astype(float).fillna(999_999)
    df['Measured Value'] = df['Measured Value'].astype(float)
    
    if process=="HNULL":
        df = df[df['Characteristic Description'].isin(['Null Pressure', 'Pressure Gain'])]
        
    df['Pass'] = df['Measured Value'].between(df['Lower Specification Limit'], df['Upper Specification Limit'])
    
    return df.groupby(['Order','Batch Number', 'Time'])["Pass"].all()

def get_failing_test(df):
    "Get tests that failed in a work order"
    df = df.replace('',np.nan)
    df['Lower Specification Limit'] = df['Lower Specification Limit'].astype(float).fillna(-999_999)
    df['Upper Specification Limit'] = df['Upper Specification Limit'].astype(float).fillna(999_999)
    df['Measured Value'] = df['Measured Value'].astype(float)
        
    df['Pass'] = df['Measured Value'].between(df['Lower Specification Limit'], df['Upper Specification Limit'])
    df.loc[df['Pass']==False, 'Test'] = df['Characteristic Description']

    test_df = df[df['Pass']==False]
    tests = test_df.groupby(['Order','Batch Number', 'Time'])["Test"].unique()
    
    return  tests