''' 

command line interface for generating HEAL data dictionary/vlmd json files

''' 

import click 


from healdata_utils.validators.validate import validate_vlmd_json,validate_vlmd_csv
import json
from pathlib import Path
import petl as etl
import pandas as pd
import csv
from collections import deque

from healdata_utils.utils import find_docstring_desc
from healdata_utils.conversion import convert_to_vlmd,choice_fxn
from healdata_utils.validators import validate_vlmd_json,validate_vlmd_csv
# TODO: vlmd group that invokes input prompts and directs towards one of the three sub commands
# TODO: validate takes in either a heal specified json or a csv and validates
@click.group()
def vlmd():
    pass 

@vlmd.command()
def quick_start():
    pass 

@vlmd.command()
@click.argument("inputfile")
#TODO: --output-file or --output-filepath?
@click.option('--outfile',default="",help='File path (or file name) where you want to output your HEAL data dictionary')
@click.option('--inputtype',default=None,type=click.Choice(list(choice_fxn.keys())),help='The type of your input file.')
@click.option('--title',default=None,help='The title of your data dictionary. If not specified, then the file name will be used')
@click.option('--description',default=None,help='Description of data dictionary')
def extract(inputfile,outfile,inputtype,title,description):

    data_dictionary_props = {'title':title,'description':description}

    #save dds and error reports to files
    data_dictionaries = convert_to_vlmd(
        input_filepath=inputfile,
        data_dictionary_props=data_dictionary_props,
        output_filepath=outfile,
        inputtype=inputtype
    )

@vlmd.command()
@click.argument("filepath")
def validate():
    pass 
     
if __name__=='__main__':
    main()