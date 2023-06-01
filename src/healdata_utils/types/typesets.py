import visions as v
import pandas.api.types as pdt
from functools import partial
# for declarative API example used as reference see:
# https://github.com/dylan-profiler/visions/blob/develop/examples/declarative_typeset.py

# for Categorical vision type reference, see ydata-profiling:
# https://github.com/ydataai/ydata-profiling/blob/develop/src/ydata_profiling/model/typeset.py
# state param needed for visions graph traversal
class contains:
    def is_category(series,state):
        return pdt.is_categorical_dtype(series)
    def is_boolean(series,state):
        return pdt.is_bool_dtype(series)

class _transformers:
    def to_category(series,state):
        return pd.Categorical(series)

class _relationships:
    def type_is_category(series,k,threshold):
        nunique = series.nunique()
        few_enough_cats = nunique<=k
        low_enough_thresh = (nunique/series.size)<threshold
        is_not_boolean = not is_boolean(series)
        return few_enough_cats and low_enough_thresh and is_not_boolean

class inference_relations:

    def type_to_category(
        related_types=[v.Integer,v.Float,v.String],
        k=5,threshold=.2):

        relationships = []
        for vision_type in related_types:
            relation = dict(
                related_type=vision_type,
                relationship=lambda series,state: partial(_relationships.type_is_category,k=k,threshold=threshold)(series),
                transformer=_transformers.to_category)
            relationships.append(relation)
        return relationships    
# types in the CompleteSet but not in StandardSet
## just manually add additions so additional dependencies
## for unused types not necessary

# {Count,
#  Date,
#  EmailAddress,
#  File,
#  Geometry,
#  IPAddress,
#  Image,
#  Ordinal,
#  Path,
#  Time,
#  URL,
#  UUID}

#TODO: make function to allow specification of params (eg k and threshold). Currently using sensiable default (see typesets_relations.py)
Categorical= v.create_type(
    "Categorical",
    identity=[v.Generic],
    contains=contains.is_category,
    inference=inference_relations.type_to_category()
)

typeset_original = (
    v.StandardSet()
    - v.Categorical
    + v.Date 
    + v.Time
)
typeset_with_categorical = (
    typeset_original
     + Categorical
 )

typeset_mapping = {
    "Integer":"integer",
    "Float":"number",
    "String":"string",
    "Time":"time",
    "TimeDelta":"duration",
    "DateTime":"datetime",
    "Boolean":"boolean"
}


def infer_frictionless_fields(
    df,
    typeset=typeset_with_categorical,
    typset_mapping=typset_mapping):
    # TODO: infer formats with extended dtypes (eg url, email etc)
    df,typepaths,_ = typeset.infer(df) # typepaths is list of the visions graph traversal - last item is casted type
    fields = []

    for col,typepath in typepaths.items():
        field = {"name":col}

        if typepath[-1]=="Categorical":
            typename = typeset_mapping.get(typepath[-2],"any")
        else:
            typename = typeset_mapping.get(typepath[-1],"any")

        field["type"] = typename

        # enums for inferred categoricals
        if typepath[-1]=="Categorical":
            field["constraints"] = {"enum":list(df[col].categories)}
        
        fields.append(field)

        
    
    return fields