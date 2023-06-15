## Variable level metadata (data dictionaries)

[![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/norc-heal/healdata-utils/HEAD?labpath=notebooks%2Fdemos%2Finputs-to-heal-data-dictionary.ipynb) 

The healdata-utils variable level metadata (vlmd) tool inputs a variety of different input file types and exports HEAL-formatted data dictionaries (JSON and CSV formats). Additionally, exported validation (ie "error") reports provide the user information as to a. if the exported data dictionary is valid according to HEAL specifications and information
on how to modify one's data dictionary to conform to make HEAL compliant.

For support formats and more detailed software-specific instructions and recommendations, [see here](docs/supported_input_formats.md)


For more information on variable level metadata properties (fields), see the [`csv` field specification](rendered-schemas/csv-fields.md) and [`json` field specification](rendered-schemas/json-fields.md). 



Typical workflows for creating a HEAL-compliant data dictionary include:

1. **Run the `vlmd` command** (or `convert_to_vlmd` if in python) to generate a HEAL-compliant data dictionary via your desired input format (See the basic usage section on the homepage for general installation and usage information.)
2. **Add/annotate with** additional information in your preferred HEAL data dictionary format (either `json` or `csv`).

To further annotate and use the data dictionary, see the variable level metadata field property information below:

- [`csv` data dictionary](rendered-schemas/csv-fields.md)
- [`json` data dictionary](rendered-schemas/json-fields.md)

3. **Run the `vlmd` command** again with your HEAL data dictioanry as input to validate.
4. Repeat 2 and 3 until you are ready to submit. Remember, currently only `name` and `description` are required.



