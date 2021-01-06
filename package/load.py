import pandas as pd

links = {
    'comp_reserves': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/company_reserves&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'lic_regLicensees': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/licence_petreg_licence_licencee&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'lic_overview': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/licence&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'lic_licensees': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/licence_licensee_hst&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'lic_operators': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/licence_oper_hst&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'lic_workObligs': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/licence_task&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'baa_licensees': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/bsns_arr_area_licensee_hst&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'field_overview': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'field_status': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_activity_status_hst&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'field_operators': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_operator_hst&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'field_owners': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_owner_hst&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'field_licensees': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_licensee_hst&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'field_reserves': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_reserves&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'field_inplaceVol': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_in_place_volumes&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'field_description': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_description&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'strat_wellbores': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/strat_litho_wellbore&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'strat_cores': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/strat_litho_wellbore_core&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'well_explCurrent': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/wellbore_exploration_current_year&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'well_prevYear': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/wellbore_exploration_last_year&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'well_expl10years': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/wellbore_exploration_last_10_years&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'well_allLong': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/wellbore_exploration_all&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'disc_overview': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/discovery&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'disc_resources': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/discovery_reserves&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'investments_yearly_by_field': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_investment_yearly&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en',
    'production_monthly_by_field': 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/TableView/field_production_monthly&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=not_used&CultureCode=en'
}

# load csv file into DataFrame and convert date columns to datetime objects

def load(key):
    """
    Download csv file from npd.no and load to DataFrame.
    Once loaded, reformat columns containing dates to datetime objects

    """

    df = pd.read_csv(links[key])

    for column in df.columns:
        if 'date' in column.lower():
            try:
                df[column] = pd.to_datetime(df[column], format='%d.%m.%Y')
            except ValueError as err:
                print(err)
        elif 'year' in column.lower():
            try:
                df[column] = pd.to_datetime(df[column], format='%Y')
            except ValueError as err:
                print(err)
        elif 'fldoperatorfrom' in column.lower():
            try:
                df[column] = pd.to_datetime(df[column], format='%d.%m.%Y')
            except ValueError as err:
                print(err)
        elif 'fldoperatorto' in column.lower():
            try:
                df[column] = pd.to_datetime(df[column], format='%d.%m.%Y')
            except ValueError as err:
                print(err)
        elif 'fldownerfrom' in column.lower():
            try:
                df[column] = pd.to_datetime(df[column], format='%d.%m.%Y')
            except ValueError as err:
                print(err)
        elif 'fldlicenseefrom' in column.lower():
            try:
                df[column] = pd.to_datetime(df[column], format='%d.%m.%Y')
            except ValueError as err:
                print(err)

    for column in df.columns:
        if 'datesyncnpd' in column.lower():
            df = df.drop(column, axis=1)

    return df


# Function to calculate reserves / volumes
def calculate(fields, df, column='fldName'):
    """
    fields: pd.Series.  Need to convert to list in order to iterate.
    df    : DataFrame from which to calculate either In place volumes or Reserves
    column: Column containing the field names, currently 'fldName' but could change from NPD
    """
    volumes = pd.DataFrame()    
    for field in list(fields):        
        if field in list(df[column]):            
            volumes = volumes.append(df[df[column]==field])
            
    volumes.loc['Total'] = volumes.sum(numeric_only=True, axis=0)
    return volumes
