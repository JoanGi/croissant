"""migrate_test module."""

import json

from etils import epath

from mlcroissant._src.core.json_ld import compact_jsonld
from mlcroissant._src.core.json_ld import expand_jsonld
from mlcroissant._src.core.rdf import make_context


# If this test fails, you probably manually updated a dataset in datasets/.
# Please, use scripts/migrations/migrate.py to migrate datasets.
def test_expand_and_reduce_json_ld():
    dataset_folder = (
        epath.Path(
            __file__).parent.parent.parent.parent.parent.parent / "datasets"
    )
    json_ld_paths = [path for path in dataset_folder.glob("*/*.json")]
    for path in json_ld_paths:
        with path.open() as f:
            json_ld = json.load(f)
        assert compact_jsonld(expand_jsonld(json_ld)) == json_ld


def test_make_context():
    assert make_context(foo="bar") == {
        "@language": "en",
        "@vocab": "https://schema.org/",
        "column": "cr:column",
        "conformsTo": "dct:conformsTo",
        "cr": "http://mlcommons.org/croissant/",
        "data": {"@id": "cr:data", "@type": "@json"},
        "dataBiases": "cr:dataBiases",
        "dataCollection": "cr:dataCollection",
        "dataType": {"@id": "cr:dataType", "@type": "@vocab"},
        "dct": "http://purl.org/dc/terms/",
        "extract": "cr:extract",
        "field": "cr:field",
        "fileProperty": "cr:fileProperty",
        "fileObject": "cr:fileObject",
        "fileSet": "cr:fileSet",
        "format": "cr:format",
        "includes": "cr:includes",
        "isEnumeration": "cr:isEnumeration",
        "jsonPath": "cr:jsonPath",
        "parentField": "cr:parentField",
        "path": "cr:path",
        "personalSensitiveInformation": "cr:personalSensitiveInformation",
        "recordSet": "cr:recordSet",
        "references": "cr:references",
        "regex": "cr:regex",
        "repeated": "cr:repeated",
        "replace": "cr:replace",
        "sc": "https://schema.org/",
        "separator": "cr:separator",
        "source": "cr:source",
        "subField": "cr:subField",
        "transform": "cr:transform",
        "foo": "bar",
        "dataCollection": "ml.dataCollection",
        "dataCollectionType": "ml.dataCollectionType",
        "dataCollectionTypeOthers": "ml.dataCollectionTypeOthers",
        "dataCollectionMissingData": "ml.dataCollectionMissingData",
        "dataCollectionRawData": "ml.dataCollectionRawData",
        "dataCollectionTimeFrameStart": "ml.dataCollectionTimeFrameStart",
        "dataCollectionTimeFrameEnd": "ml.dataCollectionTimeFrameEnd",
        "dataPreprocessingImputations": "ml.dataPreprocessingImputations",
        "dataPreprocessingProtocol": "ml.dataPreprocessingProtocol",
        "dataPreprocessingManipulation": "ml.dataPreprocessingManipulation",
        "dataAnnotationProtocol": "ml.dataAnnotationProtocol",
        "dataAnnotationPlatform": "ml.dataAnnotationPlatform",
        "dataAnnotationAnalysis": "ml.dataAnnotationAnalysis",
        "dataAnnotationPerItem": "ml.dataAnnotationPerItem",
        "dataAnnotationDemographics": "ml.dataAnnotationDemographics",
        "dataAnnotationTools": "ml.dataAnnotationTools",
        "dataUseCases": "ml.dataUseCases",
        "dataBias": "ml.dataBias",
        "dataLimitations": "ml.dataLimitations",
        "dataSocialImpact": "ml.dataSocialImpact",
        "dataSensitive": "ml.dataSensitive",
        "dataMaintenance": "ml.dataMaintenance",
    }
