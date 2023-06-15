# Supported Input Formats

In this section, supported formats for generating heal-compliant data dictionaries are listed. We also provide additional instructions on how to get the necessary input files format/software.

!!! note
    To further annotate your outputted data dictionaries, see the variable level metadata field properties (with examples) for either the __`csv data dictionary`__ [click here](rendered-schemas/csv-fields.md) and for the __`json data dictionary`__ [click here](rendered-schemas/json-fields.md)


### `csv` Datasets

CSV (comma-separated values) is the main open tabular data format for storage and exchange. It is easy to
create and understand using basic text editors in addition to popular spreadsheet software like Google Sheets
and Excel. Importantly, it is simple and can be easily integrated into web applications and just about any software.

Currently, the HEAL data utilities `vlmd` function can infer a minimal-HEAL compliant dataset by inferring `name`,`type`,and `enum` (i.e., possible values). After this minimal data dictionary is generated, the researcher can further annotate
it with fields' `description` and other optional properties in either the HEAL-compliant csv or json data dictionary (see the HEAL data dictionary template sections below for more information)

### `csv` HEAL data dictionary (e.g., from template)

HEAL data utilities can also input a `csv` HEAL data dictionary either from a manually filled out template or 
as an additional step after additional annotation (e.g., from the HEAL csv data dictionary output of the above file formats).

#### Creating a `csv` HEAL data dictionary

1. Use the template and start from scratch

    [Click here to download a blank __csv__ HEAL data dictionary template here](https://github.com/norc-heal/heal-metadata-schemas/blob/mbkranz/variable-lvl-dev/variable-level-metadata-schema/templates/template_submission.csv){:download .md-button .md-button--primary }

    [Click here to download an example of filled out __csv__ HEAL data dictionary template here](https://github.com/norc-heal/healdata-utils/blob/main/tests/data/heal_dd_from_redcap_dd_export.csv){:download .md-button .md-button--primary }

2. Output from one of the below software-specific formats and then further annotate.

!!! note
    To further annotate your outputted data dictionaries, see the variable level metadata field properties (with examples) for either the __`csv data dictionary`__ [click here](rendered-schemas/csv-fields.md)


#### Validate with the `vlmd` command

After finishing your work on the csv HEAL data dictionary, run the `vlmd` command to ensure it is HEAL-compliant with:

```bash
vlmd --filepath data/heal-dd-output.csv --inputtype csvtemplate
```

### `json` HEAL data dictionary (e.g., from template)

While the `csv` HEAL data dictionary provides a tabular format for HEAL-compliant data dictionaries, ultimately, 
these csv data dictionary files are converted to a json file (the most common format to store and exchange data within web applications such as the HEAL data platform). 

The HEAL data utilities `vlmd` tool can also input this `json` HEAL data dictionary either from a manually filled out template or as an additional step after additional annotation. Another advantage of `json` HEAL data dictionaries is that one can specify metadata describing the data dictionary as a whole (e.g., the `description` and `title`). 

#### Creating a `json` HEAL data dictionary
1. Use the template and start from scratch (click on the template below to expand)

    [Click here to download a blank __json__ HEAL data dictionary template here](https://github.com/norc-heal/heal-metadata-schemas/blob/mbkranz/variable-lvl-dev/variable-level-metadata-schema/templates/template_submission.json){:download .md-button .md-button--primary }

    [Click here to download an example of filled out __json__ HEAL data dictionary template here](https://github.com/norc-heal/healdata-utils/blob/main/tests/data/heal_dd_from_redcap_dd_export.json){:download .md-button .md-button--primary }

2. Output from one of the below software-specific formats and then further annotate.

!!! note
    To further annotate your outputted data dictionaries, see the variable level metadata field properties (with examples) for the __`json data dictionary`__ [click here](rendered-schemas/json-fields.md)


#### Validate with the `vlmd` command

After finishing your work on the csv HEAL data dictionary, run the `vlmd` command to ensure it is HEAL-compliant with:

```bash
vlmd --filepath data/heal-dd-output.json --inputtype jsontemplate
```

### Redcap: Data Dictionary CSV Export

For users collecting data in a [Redcap](https://www.project-redcap.org) data management system, HEAL-compliant data dictionaries can be generated directly from Redcap exports. 

The redcap data dictionary export serves the purpose of providing variable level metadata in a standardized, tabular format and is generally easy to export. The HEAL data utilities leverages this user experience and standardized format to enable HEAL researchers to generate a Heal-compliant data dictionary. 

#### Export your Redcap data dictionary 

To download a Redcap CSV export do the following*: 

1. After logging in to your Redcap project page, locate the `Data dictionary` page. A link to this page may be available on the project side bar (see image below) or in the `Project Setup tab` at the top of your page.

![redcap_dd_link](../assets/redcap_data_dictionary_page.png "Redcap DD Export button")

2. After arriving at the `Data dictionary` page, click on `Download the current data dictionary` to export the dictionary (see below).

![redcap_export_link](../assets/redcap_csv_dd_export_link.png "Redcap DD Export button")

*there may be slight differences depending on your specific Redcap instance and version

#### Run the `vlmd` command

```bash
vlmd --filepath input/example_redcap_demo.redcap.csv --inputtype redcap.csv --outputdir output/heal-vlmd-from-redcap.csv
```

### SAS `sas7bdat` (and `sas7bcat`) files

To accommodate SAS users, HEAL data utilities supports the binary `sas7bdat` file format, which contains the actual data values (observations/records). This file also includes variable metadata (variable `names` and variable labels/ `descriptions`).

HEAL data utilities also provides the option to include a catalog file – `sas7bcat` format - with the `sas7bdat`.  A `sas7bcat` file contains variable value labels, or `encodings` that can be mapped onto the corresponding data from a sas7bdat file.

#### Creating a `sas7bdat` and a `sas7bcat` file

Many SAS users build formats and labels into their data processing and analysis scripts. In this section, we provide syntax that can be easily copy-pasted into these existing workflows to create `sas7bdat` and `sas7bcat` files to input into the `vlmd` tool. 

This script template can be run separately or inserted directly at the end of a SAS user's workflow 

!!! note
If inserted directly, remember to delete the lines with `%INCLUDE`)

???+ Template
    ```sas title="template.sas"
    /*1. Read in data file without value labels and run full code. 
            Note: The most important pieces to run here are the PROC FORMAT statement(s) and any data steps 
            that assign formats and variable labels which are needed for the data dictionary. You may have defined variable labels and values in separate scripts for different analyses. In order to capture all your defined variable labels and values across scripts, you will need an %INCLUDE statement for each SAS script that defines unique variable labels or value labels.*/

    %INCLUDE "<INSERT SAS SCRIPT HERE FILE PATH HERE>"; /* THIS WILL RUN A SEPARATE SAS SCRIPT*/
    %INCLUDE "<INSERT SAS SCRIPT HERE FILE PATH HERE>"; /* THIS WILL RUN A SECOND SEPARATE SAS SCRIPT*/ 

    /*2. Output the format catalog (sas7bcat) */
    /*2a. If you do not have an out directory, assign one to output the SAS catalog and data file. If you already have an out directory assigned, skip this step and replace “out” with your out directory libname in the flow*/

    libname out "<INSERT THE DESIRED LOCATION (FILE PATH) TO YOUR SAS7BCAT AND SAS7BDAT FILES HERE>";

    /*2b. Output the format catalog.
            Note: The format catalog is automatically stored in work.formats. This step copies the format file to the 
            out directory as a sas7bcat file.*/
    proc catalog cat=work.FORMATS;
        copy out=out.FORMATS;
        run;
        
    /*3. Output the data file (sas7bdat) */
    data out.yourdata;
        set <INSERT THE NAME OF YOUR FINAL SAS DATASET HERE>;
        run;

    ```

The below SAS syntax is an example of how to use the template within your SAS workflow.

The below sample script creates all of our variable and value labels. Your workflow may include multiple SAS scripts with multiple format statements and may include analyses and other PROC calls for data exploration, 
but for demonstration purposes, this example only uses one script and focuses on defining the variable and value labels.

???+ Example Template Usage

    ```sas title="my_existing_sas_workflow.sas"
    /*1. Read in input data */
    proc import datafile="myprojectfolder/input/mydata.csv"
        out=raw
        dbms=csv replace;
        getnames=yes;
    run;

    /*2. Set up proc format and apply formats and variable labels in data step */
    /*Create encodings (value labels)*/
    proc format;
        VALUE YESNO
        0       ="No"
        1       ="Yes"
        
        VALUE PUBLIC
        1='State mental health authority (SMHA)'
        2='Other state government agency or department'
        3='Regional/district authority or county, local, or municipal government'
        4='Tribal government'
        5='Indian Health Service'
        6='Department of Veterans Affairs'
        7='Other'
        
        VALUE FOCUS
        1='Mental health treatment'
        2='Substance abuse treatment'
        3='Mix of mental health and substance abuse treatment (neither is primary)'
        4='General health care'
        5='Other service focus';

    **Apply formats to dataset;
    data processed;
        set raw;
        
    	/*Assign formats*/
        format YOUNGADULTS TREATPSYCHOTHRPY TREATTRAUMATHRPY YESNO. FOCUS FOCUS. PUBLIC PUBLIC.;
    	/*Add variable labels*/
        label YOUNGADULTS="Accepts young adults (aged 18-25 years old) for Tx"
                TREATPSYCHOTHRPY="Facility offers individual psychotherapy"
                TREATTRAUMATHRPY="Facility offers trauma therapy"
                FOCUS="Primary treatment focus of facility"
                PUBLIC="Public agency or department that operates facility";
    run;
    ```

    This second script called `my_output.sas` is the filled out template ([see here](template.md)). Note the `%INCLUDE` function that calls `my_existing_sas_workflow.sas`

    ```sas title="my_output.sas"
    /*1. Read in data file without value labels and run full code. 
            Note: The most important pieces to run here are the PROC FORMAT statement(s) and any data steps 
            that assign formats and variable labels which are needed for the data dictionary. You may have defined variable labels and values in separate scripts for different analyses. In order to capture all your defined variable labels and values across scripts, you will need an %INCLUDE statement for each SAS script that defines unique variable labels or value labels.*/*/

    %INCLUDE "myprojectfolder/my_existing_workflow.sas"; /* THIS WILL RUN A SEPARATE SAS SCRIPT*/

    /*2. Output the format catalog (sas7bcat) */
    /*2a. If you do not have an out directory, assign one to output the SAS catalog and data file.*/
    libname out "myprojectfolder/output";

    /*2b. Output the format catalog.
            Note: The format catalog is automatically stored in work.formats. This step copies the format file to the 
            out directory as a sas7bcat file.*/
    proc catalog cat=work.FORMATS;
        copy out=out.FORMATS;
        run;
        
    /*3. Output the data file (sas7bdat) to your output folder*/
    data out.yourdata;
        set processed;
        run;

    ```

#### Run the `vlmd` command

After creating the necessary `sas7bdat` and `sas7bcat` files, you can then run the `vlmd` command. Note, the `sas7bcat` files are optional. However, if you don't include a `sas7bcat` file, the `encodings` (i.e., value labels) will not be added.

With the sas7bcat file:

```bash
vlmd --filepath input/data.sas7bdat --sas7bcat-filepath input/formats.sas7bcat --inputtype sas7bdat
```

Without the sas7bdat file:


```bash
vlmd --filepath input/data.sas7bdat --inputtype sas7bdat
```



### SPSS `.sav` files

For SPSS users, HEAL data utilities generates heal-compliant data dictionaries from SPSS's default file format for storing datasets: A `SAV` file. It not only stores the data itself but also stores metadata such as variable names, variable labels, types, and value labels. The HEAL data utilities extracts the data and metadata to create heal-compliant data dictionaries.

<!-- ### Creating a well-annotated `sav` file

TO ADD -->

#### Run the `vlmd` command
```bash
vlmd --filepath data/example_pyreadstat_output.sav --inputtype sav
```
### Stata `.dta` files

For Stata users, HEAL data utilities generates heal-compliant data dictionaries through Stata's default file format: the `DTA` files. `DTA` files not only store the data itself but also stores metadata such as variable names, variable labels, types, and value labels.

<!-- ### Creating a well-annotated `dta` file

TO ADD -->
