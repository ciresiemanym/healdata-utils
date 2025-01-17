import pytest 
from pathlib import Path
from healdata_utils.conversion import choice_fxn
import json

@pytest.fixture(scope="module")
def fields_propname():
    return "data_dictionary"

@pytest.fixture(scope="module")
def valid_input_params():
    inputdir = Path("data/valid/input")
    outputdir = Path("tmp")
    data_dictionary_props = {
        "description": (
            "This is a proof of concept to demonstrate"
            " the healdata-utils functionality"
        ),
        "title": "Healdata-utils Demonstration Data Dictionary",
    }
    get_input_params = lambda input_filepath: {
        "input_filepath":inputdir.joinpath(input_filepath),
        "output_filepath":outputdir.joinpath("heal-dd.json"),
        "data_dictionary_props":data_dictionary_props}
        
    input_params = {
        "excel-data":{
            **get_input_params("excel-multitab-dataset1.xlsx"),
            "inputtype":"excel-data"
        },
        "csv-data":{
            **get_input_params("data_csv_dataset1.data.csv"),
            "inputtype":"csv-data"
        },
        "sas":{
            **get_input_params("sas-nmhss-2019/data.sas7bdat"),
            #NOTE: now auto detecting sas formats file
            # "sas_catalog_filepath":inputdir.joinpath("sas-nmhss-2019/formats.sas7bcat"),
            "inputtype":"sas"
        }, #TODO: reduce data so easier to manage and test
        "stata":{**get_input_params("stata_dta_dataset1.dta"),"inputtype":"stata"},
        # "sav":get_input_params("../../JCOIN_NORC_Omnibus_SURVEY3_June2020.sav"),
        "spss":{**get_input_params("spss_sav_dataset1.sav"),"inputtype":"spss"},
        "redcap":{**get_input_params("redcap_dd_export.redcap.csv"),"inputtype":"redcap-csv"},
        "frictionless":{**get_input_params("frictionless_dataset1.frictionless.schema.json"),
            "inputtype":"frictionless-tbl-schema"}
    }
    return input_params

@pytest.fixture(scope="module")
def valid_output_json(valid_input_params):
    path = Path("data/valid/output")
    filenames = {
        "excel-data":{
            "experiment1":path/"excel-dataset1/multiple-dd/heal-dd-experiment1.json",
            "experiment2":path/"excel-dataset1/multiple-dd/heal-dd-experiment2.json"
        },
        "csv-data":path/"heal_dd_from_csv_data_dataset1.json",
        "sas":path/"heal_dd_from_sas7bdat_with_sas7bcat.json", #TODO: reduce data so easier to manage and test
        "stata":path/"heal_dd_from_stata_dta_dataset1.json",
        "spss":path/"heal_dd_from_spss_sav_dataset1.json",
        "redcap":path/"heal_dd_from_redcap_dd_export.json",
        "frictionless":path/"heal_dd_from_frictionless_schema.json"
    }
    assert set(filenames) == set(valid_input_params)
            
    return filenames

@pytest.fixture(scope="module")
def valid_output_csv(valid_input_params):
    path = Path("data/valid/output")
    filenames = {
        "excel-data":{
            "experiment1":path/"excel-dataset1/multiple-dd/heal-dd-experiment1.csv",
            "experiment2":path/"excel-dataset1/multiple-dd/heal-dd-experiment2.csv"
        },
        "csv-data":path/"heal_dd_from_csv_data_dataset1.csv",
        "sas":path/"heal_dd_from_sas7bdat_with_sas7bcat.csv",#TODO: reduce data so easier to manage and test
        "stata":path/"heal_dd_from_stata_dta_dataset1.csv",
        "spss":path/"heal_dd_from_spss_sav_dataset1.csv",
        "redcap":path/"heal_dd_from_redcap_dd_export.csv",
        "frictionless":path/"heal_dd_from_frictionless_schema.csv"
    }

    assert set(filenames) == set(valid_input_params)

    return filenames


def compare_vlmd_tmp_to_output(tmpdir,csvoutput,jsonoutput,fields_propname,stemsuffix=""):
    """ compares a given csv and json output to a tmp directory
    for both csv and json (vlmd - variable level metadata)
    """
    
    ddjson = json.loads(list(tmpdir.glob(f"*{stemsuffix}.json"))[0].read_text())
    #NOTE: csv are just fields so no ddcsv

    # check for incorrect fields       
    csv_fields = list(tmpdir.glob(f"*{stemsuffix}.csv"))[0].read_text().split("\n")
    json_fields = ddjson.pop(fields_propname) #NOTE: testing individual fields

    valid_output_json_fields = jsonoutput.pop(fields_propname)
    valid_output_csv_fields = csvoutput

    invalid_json_fields = []
    invalid_csv_fields = []
    indices = range(len(json_fields))
    for i in indices:
        if json_fields[i]!=valid_output_json_fields[i]:
            invalid_json_fields.append(i)
        if csv_fields[i]!=valid_output_csv_fields[i]:
            invalid_csv_fields.append(i)
    
    json_field_names = [f["name"] for f in json_fields]
    csv_field_names = [f["name"] for f in json_fields]
    try:
        assert sorted(json_field_names)==sorted(csv_field_names),f"json fields must have the same field names as csv fields"
    except:
        assert json_field_names == csv_field_names, "json field names must be same as csv field names"
    
    assert len(invalid_json_fields)==0,f"The following **json** dd fields are not valid: {str(invalid_json_fields)}"
    assert len(invalid_csv_fields)==0,f"The following **csv** dd fields are not valid: {str(invalid_csv_fields)}"
    
    
    # check if root level properties other than the fields are valid
    for propname in ddjson:
        assert ddjson[propname] == jsonoutput[propname],f"json dd property '{propname}' assertion failed"
