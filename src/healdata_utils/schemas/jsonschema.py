healjsonschema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "vlmd",
    "title": "Variable Level Metadata (Data Dictionaries)",
    "description": "This schema defines the variable level metadata for one data "
    "dictionary for a given study.Note a given study can have "
    "multiple data dictionaries",
    "type": "object",
    "required": ["title", "data_dictionary"],
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "data_dictionary": {
            "type": "array",
            "items": {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "$id": "vlmd-fields",
                "title": "HEAL Variable " "Level Metadata " "Fields",
                "description": "Variable "
                "level "
                "metadata "
                "individual "
                "fields "
                "integrated "
                "into the "
                "variable "
                "level\n"
                "metadata "
                "object "
                "within the "
                "HEAL "
                "platform "
                "metadata "
                "service.\n"
                "\n"
                "> Note, only "
                "`name` and "
                "`description` "
                "are "
                "required.\n"
                ">  Listed at "
                "the end of "
                "the "
                "description "
                "are "
                "suggested "
                '"priority" '
                "levels in "
                "brackets "
                "(e.g., "
                "[<priority>]):\n"
                "  1. "
                "[Required]: "
                "Needs to be "
                "filled out "
                "to be "
                "valid.\n"
                "  2. [Highly "
                "recommended]: "
                "Greatly help "
                "using the "
                "data "
                "dictionary "
                "but not "
                "required. \n"
                "  3. "
                "[Optional, "
                "if "
                "applicable]: "
                "May only be "
                "applicable "
                "to certain "
                "fields.\n"
                "  4. "
                "[Autopopulated, "
                "if not "
                "filled]: "
                "These fields "
                "are intended "
                "to be "
                "autopopulated "
                "from other "
                "fields but "
                "can be "
                "filled out "
                "if desired.\n"
                "  5. "
                "[Experimental]: "
                "These fields "
                "are not "
                "currently "
                "used but are "
                "in "
                "development.\n",
                "type": "object",
                "additionalProperties": True,
                "required": ["name", "description"],
                "properties": {
                    "module": {
                        "type": "string",
                        "title": "Module",
                        "description": "The "
                        "section, "
                        "form, "
                        "survey "
                        "instrument, "
                        "set "
                        "of "
                        "measures  "
                        "or "
                        "other "
                        "broad "
                        "category "
                        "used \n"
                        "to "
                        "group "
                        "variables.\n",
                        "examples": [
                            "Demographics",
                            "PROMIS",
                            "Substance " "use",
                            "Medical " "History",
                            "Sleep " "questions",
                            "Physical " "activity",
                        ],
                    },
                    "name": {
                        "type": "string",
                        "title": "Variable " "Name",
                        "description": "The "
                        "name "
                        "of "
                        "a "
                        "variable "
                        "(i.e., "
                        "field) "
                        "as "
                        "it "
                        "appears "
                        "in "
                        "the "
                        "data. \n"
                        "\n"
                        "[Required]\n",
                    },
                    "title": {
                        "type": "string",
                        "title": "Variable " "Label " "(ie " "Title)",
                        "description": "The "
                        "human-readable "
                        "title "
                        "or "
                        "label "
                        "of "
                        "the "
                        "variable. \n"
                        "\n"
                        "[Highly "
                        "recommended]\n",
                        "examples": [
                            "My " "Variable " "(for " "name " "of " "my_variable)"
                        ],
                    },
                    "description": {
                        "type": "string",
                        "title": "Variable " "Description",
                        "description": "An "
                        "extended "
                        "description "
                        "of "
                        "the "
                        "variable. "
                        "This "
                        "could "
                        "be "
                        "the "
                        "definition "
                        "of "
                        "a "
                        "variable "
                        "or "
                        "the \n"
                        "question "
                        "text "
                        "(e.g., "
                        "if "
                        "a "
                        "survey). \n"
                        "\n"
                        "[Required]\n",
                        "examples": [
                            "Definition",
                            "Question " "text " "(if " "a " "survey)",
                        ],
                    },
                    "type": {
                        "title": "Variable " "Type",
                        "description": "A "
                        "classification "
                        "or "
                        "category "
                        "of "
                        "a "
                        "particular "
                        "data "
                        "element "
                        "or "
                        "property "
                        "expected "
                        "or "
                        "allowed "
                        "in "
                        "the "
                        "dataset.\n"
                        "\n"
                        "-  "
                        "`number` "
                        "(A "
                        "numeric "
                        "value "
                        "with "
                        "optional "
                        "decimal "
                        "places. "
                        "(e.g., "
                        "3.14))\n"
                        "-  "
                        "`integer` "
                        "(A "
                        "whole "
                        "number "
                        "without "
                        "decimal "
                        "places. "
                        "(e.g., "
                        "42))\n"
                        "-  "
                        "`string` "
                        "(A "
                        "sequence "
                        "of "
                        "characters. "
                        "(e.g., "
                        '\\"test\\"))\n'
                        "-  "
                        "`any` "
                        "(Any "
                        "type "
                        "of "
                        "data "
                        "is "
                        "allowed. "
                        "(e.g., "
                        "true))\n"
                        "-  "
                        "`boolean` "
                        "(A "
                        "binary "
                        "value "
                        "representing "
                        "true "
                        "or "
                        "false. "
                        "(e.g., "
                        "true))\n"
                        "-  "
                        "`date` "
                        "(A "
                        "specific "
                        "calendar "
                        "date. "
                        "(e.g., "
                        '\\"2023-05-25\\"))\n'
                        "-  "
                        "`datetime` "
                        "(A "
                        "specific "
                        "date "
                        "and "
                        "time, "
                        "including "
                        "timezone "
                        "information. "
                        "(e.g., "
                        '\\"2023-05-25T10:30:00Z\\"))\n'
                        "-  "
                        "`time` "
                        "(A "
                        "specific "
                        "time "
                        "of "
                        "day. "
                        "(e.g., "
                        '\\"10:30:00\\"))\n'
                        "-  "
                        "`year` "
                        "(A "
                        "specific "
                        "year. "
                        "(e.g., "
                        "2023)\n"
                        "-  "
                        "`yearmonth` "
                        "(A "
                        "specific "
                        "year "
                        "and "
                        "month. "
                        "(e.g., "
                        '\\"2023-05\\"))\n'
                        "-  "
                        "`duration` "
                        "(A "
                        "length "
                        "of "
                        "time. "
                        "(e.g., "
                        '\\"PT1H\\")\n'
                        "-  "
                        "`geopoint` "
                        "(A "
                        "pair "
                        "of "
                        "latitude "
                        "and "
                        "longitude "
                        "coordinates. "
                        "(e.g., "
                        "[51.5074, "
                        "-0.1278]))\n",
                        "type": "string",
                        "enum": [
                            "number",
                            "integer",
                            "string",
                            "any",
                            "boolean",
                            "date",
                            "datetime",
                            "time",
                            "year",
                            "yearmonth",
                            "duration",
                            "geopoint",
                        ],
                    },
                    "format": {
                        "title": "Frictionless " "Formats",
                        "description": "A "
                        "format "
                        "taken "
                        "from "
                        "one "
                        "of "
                        "the "
                        "[frictionless "
                        "specification](https://specs.frictionlessdata.io/) "
                        "schemas.\n"
                        "For "
                        "example, "
                        "for "
                        "tabular "
                        "data, "
                        "there "
                        "is "
                        "the "
                        "[Table "
                        "Schema "
                        "specification](https://specs.frictionlessdata.io/table-schema)\n"
                        "\n"
                        "Each "
                        "format "
                        "is "
                        "dependent "
                        "on "
                        "the "
                        "`type` "
                        "specified. "
                        "For "
                        "example:\n"
                        "If "
                        "`type` "
                        "is "
                        '"string", '
                        "then "
                        "see "
                        "the "
                        "String "
                        "formats. \n"
                        "If "
                        "`type` "
                        "is "
                        "one "
                        "of "
                        "the "
                        "date-like "
                        "formats, "
                        "then "
                        "see "
                        "Date "
                        "formats.\n",
                        "name": "frictionless_formats",
                        "anyOf": [
                            {
                                "title": "String " "Format",
                                "enum": ["uri", "email", "binary", "uuid"],
                            },
                            {
                                "title": "Date " "Format",
                                "description": "A "
                                "format "
                                "for "
                                "a "
                                "date "
                                "variable "
                                "(`date`,`time`,`datetime`).  \n"
                                "    "
                                "\\n\\t* "
                                "**default**: "
                                "An "
                                "ISO8601 "
                                "format "
                                "string.\n"
                                "    "
                                "\\n\\t* "
                                "**any**: "
                                "Any "
                                "parsable "
                                "representation "
                                "of "
                                "a "
                                "date/time/datetime. "
                                "The "
                                "implementing "
                                "library "
                                "can "
                                "attempt "
                                "to "
                                "parse "
                                "the "
                                "datetime "
                                "via "
                                "a "
                                "range "
                                "of "
                                "strategies.\n"
                                "    "
                                "\\n\\t* "
                                "**{PATTERN}**: "
                                "The "
                                "value "
                                "can "
                                "be "
                                "parsed "
                                "according "
                                "to "
                                "`{PATTERN}`, "
                                "which "
                                "`MUST` "
                                "follow "
                                "the "
                                "date "
                                "formatting "
                                "syntax "
                                "of "
                                "C "
                                "/ "
                                "Python "
                                "[strftime](http://strftime.org/).\n"
                                "\n"
                                "\\nExamples:\n"
                                "\n"
                                "  "
                                "`%Y-%m-%d` "
                                "(for "
                                "date, "
                                "e.g., "
                                "2023-05-25)\n"
                                "  "
                                "`%Y%-%d` "
                                "(for "
                                "date, "
                                "e.g., "
                                "20230525) "
                                "for "
                                "date "
                                "without "
                                'dashes"\n'
                                "  "
                                "`%Y-%m-%dT%H:%M:%S` "
                                "(for "
                                "datetime, "
                                "e.g., "
                                "2023-05-25T10:30:45)\n"
                                "  "
                                "`%Y-%m-%dT%H:%M:%SZ` "
                                "(for "
                                "datetime "
                                "with "
                                "UTC "
                                "timezone, "
                                "e.g., "
                                "2023-05-25T10:30:45Z)\n"
                                "  "
                                "`%Y-%m-%dT%H:%M:%S%z` "
                                "(for "
                                "datetime "
                                "with "
                                "timezone "
                                "offset, "
                                "e.g., "
                                "2023-05-25T10:30:45+0300)\n"
                                "  "
                                "`%Y-%m-%dT%H:%M` "
                                "(for "
                                "datetime "
                                "without "
                                "seconds, "
                                "e.g., "
                                "2023-05-25T10:30)\n"
                                "  "
                                "`%Y-%m-%dT%H` "
                                "(for "
                                "datetime "
                                "without "
                                "minutes "
                                "and "
                                "seconds, "
                                "e.g., "
                                "2023-05-25T10)\n"
                                "  "
                                "`%H:%M:%S` "
                                "(for "
                                "time, "
                                "e.g., "
                                "10:30:45)\n"
                                "  "
                                "`%H:%M:%SZ` "
                                "(for "
                                "time "
                                "with "
                                "UTC "
                                "timezone, "
                                "e.g., "
                                "10:30:45Z)\n"
                                "  "
                                "`%H:%M:%S%z` "
                                "(for "
                                "time "
                                "with "
                                "timezone "
                                "offset, "
                                "e.g., "
                                "10:30:45+0300)\n",
                            },
                            {
                                "title": "Geopoint " "Format",
                                "description": "The "
                                "two "
                                "types "
                                "of "
                                "formats "
                                "for "
                                "`geopoint` "
                                "(describing "
                                "a "
                                "geographic "
                                "point).",
                                "oneOf": [
                                    {
                                        "type": "array",
                                        "description": "A "
                                        "JSON "
                                        "array "
                                        "or "
                                        "a "
                                        "string "
                                        "parsable "
                                        "as "
                                        "a "
                                        "JSON "
                                        "array "
                                        "where "
                                        "each "
                                        "item "
                                        "is "
                                        "a "
                                        "number "
                                        "with "
                                        "the "
                                        "first \n"
                                        "as "
                                        "the "
                                        "latitude "
                                        "and "
                                        "the "
                                        "second "
                                        "as "
                                        "longitude. \n",
                                    },
                                    {
                                        "type": "object",
                                        "description": "Contains "
                                        "latitude "
                                        "and "
                                        "longitude "
                                        "with "
                                        "two "
                                        "keys "
                                        '("lat" '
                                        "and "
                                        '"long") '
                                        "with "
                                        "number "
                                        "items "
                                        "mapped "
                                        "to "
                                        "each "
                                        "key.\n",
                                    },
                                ],
                            },
                            {
                                "title": "geojson",
                                "description": "The "
                                "JSON "
                                "object "
                                "according "
                                "to "
                                "the "
                                "geojson "
                                "spec.",
                                "enum": ["topojson", "default"],
                            },
                        ],
                    },
                    "constraints": {
                        "type": "object",
                        "properties": {
                            "maxLength": {
                                "type": "integer",
                                "title": "Maximum " "Length",
                                "description": "Indicates "
                                "the "
                                "maximum "
                                "length "
                                "of "
                                "an "
                                "iterable "
                                "(e.g., "
                                "array, "
                                "string, "
                                "or\n"
                                "object). "
                                "For "
                                "example, "
                                "if "
                                "'Hello "
                                "World' "
                                "is "
                                "the "
                                "longest "
                                "value "
                                "of "
                                "a\n"
                                "categorical "
                                "variable, "
                                "this "
                                "would "
                                "be "
                                "a "
                                "maxLength "
                                "of "
                                "11.\n"
                                "\n"
                                "[Optional,if "
                                "applicable]\n",
                            },
                            "enum": {
                                "title": "Variable " "Possible " "Values",
                                "description": "Constrains "
                                "possible "
                                "values "
                                "to "
                                "a "
                                "set "
                                "of "
                                "values.\n"
                                "\n"
                                "[Optional,if "
                                "applicable]\n",
                                "type": "array",
                            },
                            "pattern": {
                                "type": "string",
                                "title": "Regular " "Expression " "Pattern",
                                "description": "A "
                                "regular "
                                "expression "
                                "pattern "
                                "the "
                                "data "
                                "MUST "
                                "conform "
                                "to.\n"
                                "\n"
                                "[Optional,if "
                                "applicable]\n",
                            },
                            "maximum": {
                                "type": "integer",
                                "title": "Maximum " "Value",
                                "description": "Specifies "
                                "the "
                                "maximum "
                                "value "
                                "of "
                                "a "
                                "field "
                                "(e.g., "
                                "maximum "
                                "-- "
                                "or "
                                "most\n"
                                "recent "
                                "-- "
                                "date, "
                                "maximum "
                                "integer "
                                "etc). "
                                "Note, "
                                "this "
                                "is "
                                "different "
                                "then\n"
                                "maxLength "
                                "property.\n"
                                "\n"
                                "[Optional,if "
                                "applicable]\n",
                            },
                            "minimum": {
                                "type": "integer",
                                "title": "Minimum " "Value",
                                "description": "Specifies "
                                "the "
                                "minimum "
                                "value "
                                "of "
                                "a "
                                "field.\n"
                                "\n"
                                "[Optional,if "
                                "applicable]\n",
                            },
                        },
                    },
                    "encodings": {
                        "title": "Variable "
                        "Value "
                        "Encodings "
                        "(i.e., "
                        "mappings; "
                        "value "
                        "labels)",
                        "description": "Variable "
                        "value "
                        "encodings "
                        "provide "
                        "a "
                        "way "
                        "to "
                        "further "
                        "annotate "
                        "any "
                        "value "
                        "within "
                        "a "
                        "any "
                        "variable "
                        "type,\n"
                        "making "
                        "values "
                        "easier "
                        "to "
                        "understand. \n"
                        "\n"
                        "\n"
                        "Many "
                        "analytic "
                        "software "
                        "programs "
                        "(e.g., "
                        "SPSS,Stata, "
                        "and "
                        "SAS) "
                        "use "
                        "numerical "
                        "encodings "
                        "and "
                        "some "
                        "algorithms\n"
                        "only "
                        "support "
                        "numerical "
                        "values. "
                        "Encodings "
                        "(and "
                        "mappings) "
                        "allow "
                        "categorical "
                        "values "
                        "to "
                        "be "
                        "stored "
                        "as\n"
                        "numerical "
                        "values.\n"
                        "\n"
                        "Additionally, "
                        "as "
                        "another "
                        "use "
                        "case, "
                        "this "
                        "field "
                        "provides "
                        "a "
                        "way "
                        "to\n"
                        "store "
                        "categoricals "
                        "that "
                        "are "
                        "stored "
                        "as  "
                        '"short" '
                        "labels "
                        "(such "
                        "as\n"
                        "abbreviations).\n"
                        "\n"
                        "[Optional,if "
                        "applicable]\n",
                        "type": "object",
                        "examples": [
                            {"0": "No", "1": "Yes"},
                            {
                                "HW": "Hello " "world",
                                "GBW": "Good " "bye " "world",
                                "HM": "Hi, " "Mike",
                            },
                        ],
                    },
                    "ordered": {
                        "title": "An " "ordered " "variable",
                        "description": "Indicates "
                        "whether "
                        "a "
                        "categorical "
                        "variable "
                        "is "
                        "ordered. "
                        "This "
                        "variable  "
                        "is\n"
                        "relevant "
                        "for "
                        "variables "
                        "that "
                        "have "
                        "an "
                        "ordered "
                        "relationship "
                        "but "
                        "not\n"
                        "necessarily  "
                        "a "
                        "numerical "
                        "relationship "
                        "(e.g., "
                        "Strongly "
                        "disagree "
                        "< "
                        "Disagree\n"
                        "< "
                        "Neutral "
                        "< "
                        "Agree).\n"
                        "\n"
                        "[Optional,if "
                        "applicable]\n",
                        "type": "boolean",
                    },
                    "missingValues": {
                        "title": "Missing " "Values",
                        "description": "A "
                        "list "
                        "of "
                        "missing "
                        "values "
                        "specific "
                        "to "
                        "a "
                        "variable.\n"
                        "\n"
                        "[Highly "
                        "recommended]\n",
                        "type": "array",
                    },
                    "trueValues": {
                        "title": "Boolean " "True " "Value " "Labels",
                        "description": "For "
                        "boolean "
                        "(true) "
                        "variable "
                        "(as "
                        "defined "
                        "in "
                        "type "
                        "field), "
                        "this "
                        "field "
                        "allows\n"
                        "a "
                        "physical "
                        "string "
                        "representation "
                        "to "
                        "be "
                        "cast "
                        "as "
                        "true "
                        "(increasing\n"
                        "readability "
                        "of "
                        "the "
                        "field). "
                        "It "
                        "can "
                        "include "
                        "one "
                        "or "
                        "more "
                        "values.\n"
                        "\n"
                        "[Optional, "
                        "if "
                        "applicable]\n",
                        "type": "array",
                        "items": {"type": "string"},
                        "examples": [
                            "Required",
                            "REQUIRED",
                            "required",
                            "Yes",
                            'Checked"',
                        ],
                    },
                    "falseValues": {
                        "title": "Boolean " "False " "Value " "Labels",
                        "description": "For "
                        "boolean "
                        "(false) "
                        "variable "
                        "(as "
                        "defined "
                        "in "
                        "type "
                        "field), "
                        "this "
                        "field "
                        "allows\n"
                        "a "
                        "physical "
                        "string "
                        "representation "
                        "to "
                        "be "
                        "cast "
                        "as "
                        "false "
                        "(increasing\n"
                        "readability "
                        "of "
                        "the "
                        "field) "
                        "that "
                        "is "
                        "not "
                        "a "
                        "standard "
                        "false "
                        "value. "
                        "It "
                        "can "
                        "include "
                        "one "
                        "or "
                        "more "
                        "values.\n",
                        "type": "array",
                    },
                    "repo_link": {
                        "type": "string",
                        "title": "Variable " "Repository " "Link",
                        "description": "A "
                        "link "
                        "to "
                        "the "
                        "variable "
                        "as "
                        "it "
                        "exists "
                        "on "
                        "the "
                        "home "
                        "repository, "
                        "if "
                        "applicable\n",
                    },
                    "standardsMappings": {
                        "title": "Standards " "Mappings",
                        "description": "A "
                        "published "
                        "set "
                        "of "
                        "standard "
                        "variables "
                        "such "
                        "as "
                        "the "
                        "NIH "
                        "Common "
                        "Data "
                        "Elements "
                        "program.\n"
                        "[Autopopulated, "
                        "if "
                        "not "
                        "filled]",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "title": "Standards " "Mapping " "- " "Title",
                                    "description": "The "
                                    "**type** "
                                    "of "
                                    "mapping "
                                    "linked "
                                    "to "
                                    "a "
                                    "published "
                                    "set "
                                    "of "
                                    "standard "
                                    "variables "
                                    "such "
                                    "as "
                                    "the "
                                    "NIH "
                                    "Common "
                                    "Data "
                                    "Elements "
                                    "program.\n"
                                    "[Autopopulated, "
                                    "if "
                                    "not "
                                    "filled]\n",
                                    "examples": ["cde", "ontology", "reference_list"],
                                    "type": "string",
                                },
                                "label": {
                                    "title": "Standards " "Mapping " "- " "Label",
                                    "description": "A "
                                    "free "
                                    "text "
                                    "**label** "
                                    "of "
                                    "a "
                                    "mapping "
                                    "indicating "
                                    "a "
                                    "mapping(s) "
                                    "to "
                                    "a "
                                    "published "
                                    "set "
                                    "of "
                                    "standard "
                                    "variables "
                                    "such "
                                    "as "
                                    "the "
                                    "NIH "
                                    "Common "
                                    "Data "
                                    "Elements "
                                    "program.\n"
                                    "\n"
                                    "[Autopopulated, "
                                    "if "
                                    "not "
                                    "filled]\n",
                                    "type": "string",
                                    "examples": [
                                        "substance " "use",
                                        "chemical " "compound",
                                        "promis",
                                    ],
                                },
                                "url": {
                                    "title": "Standards " "Mapping " "- " "Url",
                                    "description": "The "
                                    "url "
                                    "that "
                                    "links "
                                    "out "
                                    "to "
                                    "the "
                                    "published, "
                                    "standardized "
                                    "mapping.\n"
                                    "\n"
                                    "[Autopopulated, "
                                    "if "
                                    "not "
                                    "filled]\n",
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                        "https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"
                                    ],
                                },
                                "source": {
                                    "title": "Standard " "Mapping " "- " "Source",
                                    "description": "The "
                                    "source "
                                    "of "
                                    "the "
                                    "standardized "
                                    "variable.\n",
                                    "type": "string",
                                    "examples": [
                                        "TBD "
                                        "(will "
                                        "have "
                                        "controlled "
                                        "vocabulary)"
                                    ],
                                },
                                "id": {
                                    "title": "Standard " "Mapping " "- " "Id",
                                    "type": "string",
                                    "description": "The "
                                    "id "
                                    "locating "
                                    "the "
                                    "individual "
                                    "mapping "
                                    "within "
                                    "the "
                                    "given "
                                    "source.\n",
                                },
                            },
                        },
                    },
                    "relatedConcepts": {
                        "title": "Related " "Concepts",
                        "description": "Mappings "
                        "to "
                        "a "
                        "published "
                        "set "
                        "of "
                        "concepts "
                        "related "
                        "to "
                        "the "
                        "given "
                        "field "
                        "such "
                        "as "
                        "ontological "
                        "information "
                        "(eg., "
                        "NCI "
                        "thesaurus, "
                        "bioportal "
                        "etc)\n"
                        "[Autopopulated, "
                        "if "
                        "not "
                        "filled]",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "title": "Related " "concepts " "- " "Type",
                                    "description": "The "
                                    "**type** "
                                    "of "
                                    "mapping "
                                    "to "
                                    "a "
                                    "published "
                                    "set "
                                    "of "
                                    "concepts "
                                    "related "
                                    "to "
                                    "the "
                                    "given "
                                    "field "
                                    "such "
                                    "as \n"
                                    "ontological "
                                    "information "
                                    "(eg., "
                                    "NCI "
                                    "thesaurus, "
                                    "bioportal "
                                    "etc)\n"
                                    "\n"
                                    "[Autopopulated, "
                                    "if "
                                    "not "
                                    "filled]\n",
                                    "type": "string",
                                },
                                "label": {
                                    "type": "string",
                                    "title": "Related " "Concepts " "- " "Label",
                                    "description": "A "
                                    "free "
                                    "text "
                                    "**label** "
                                    "of "
                                    "mapping "
                                    "to "
                                    "a "
                                    "published "
                                    "set "
                                    "of "
                                    "concepts "
                                    "related "
                                    "to "
                                    "the "
                                    "given "
                                    "field "
                                    "such "
                                    "as \n"
                                    "ontological "
                                    "information "
                                    "(eg., "
                                    "NCI "
                                    "thesaurus, "
                                    "bioportal "
                                    "etc)\n"
                                    "\n"
                                    "[Autopopulated, "
                                    "if "
                                    "not "
                                    "filled]\n",
                                },
                                "url": {
                                    "title": "Related " "Concepts " "- " "Url",
                                    "description": "The "
                                    "url "
                                    "that "
                                    "links "
                                    "out "
                                    "to "
                                    "the "
                                    "published, "
                                    "standardized "
                                    "concept.\n"
                                    "\n"
                                    "[Autopopulated, "
                                    "if "
                                    "not "
                                    "filled]\n",
                                    "type": "string",
                                    "format": "uri",
                                    "examples": [
                                        "https://cde.nlm.nih.gov/deView?tinyId=XyuSGdTTI"
                                    ],
                                },
                                "source": {
                                    "title": "Related " "Concepts " "- " "Source",
                                    "description": "The "
                                    "source "
                                    "of "
                                    "the "
                                    "related "
                                    "concept.\n"
                                    "\n"
                                    "[Autopopulated, "
                                    "if "
                                    "not "
                                    "filled]\n",
                                    "type": "string",
                                    "examples": [
                                        "TBD "
                                        "(will "
                                        "have "
                                        "controlled "
                                        "vocabulary)"
                                    ],
                                },
                                "id": {
                                    "title": "Related " "Concepts " "- " "Id",
                                    "type": "string",
                                    "description": "The "
                                    "id "
                                    "locating "
                                    "the "
                                    "individual "
                                    "mapping "
                                    "within "
                                    "the "
                                    "given "
                                    "source.\n"
                                    "\n"
                                    "[Autopopulated, "
                                    "if "
                                    "not "
                                    "filled]\n",
                                },
                            },
                        },
                    },
                    "univarStats": {
                        "type": "object",
                        "description": "Univariate "
                        "statistics "
                        "inferred "
                        "from "
                        "the "
                        "data "
                        "about "
                        "the "
                        "given "
                        "variable \n"
                        "\n"
                        "[Experimental]\n",
                        "properties": {
                            "median": {"type": "number"},
                            "mean": {"type": "number"},
                            "std": {"type": "number"},
                            "min": {"type": "number"},
                            "max": {"type": "number"},
                            "mode": {"type": "number"},
                            "count": {"type": "integer", "minimum": 0},
                            "twentyFifthPercentile": {"type": "number"},
                            "seventyFifthPercentile": {"type": "number"},
                            "categoricalMarginals": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "count": {"type": "integer"},
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
