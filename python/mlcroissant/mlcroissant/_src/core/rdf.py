"""RDF module to represent all things related to the Resource Description Framework."""

from __future__ import annotations

import dataclasses
import functools

from mlcroissant._src.core.types import Json

BASE_CONTEXT = {
    "@language": "en",
    "@vocab": "https://schema.org/",
    "column": "cr:column",
    "conformsTo": "dct:conformsTo",
    "cr": "http://mlcommons.org/croissant/",
    "data": {"@id": "cr:data", "@type": "@json"},
    "dataBiases": "cr:dataBiases",
    "dataCollection": "cr:dataCollection",
    "dataCollectionMissing": "cr:dataCollectionMissing",
    "dataCollectionType": "cr:dataCollectionType",
    "dataCollectionTypeOthers": "cr:dataCollectionTypeOthers",
    "dataCollectionRaw": "cr:dataCollectionRaw",
    "dataCollectionTimeFrameStart": "cr:dataCollectionTimeframeStart",
    "dataCollectionTimeFrameEnd": "cr:dataCollectionTimeframeEnd", 
    "dataPreprocessingImputation": "cr:dataPreprocessingImputation",
    "dataPreprocessingProtocol": "cr:dataPeprocessingProtocol",
    "dataPreprocessingManipulation": "cr:dataPreprocessingManipulation",
    "dataAnnotationProtocol": "cr:dataAnnotationProtocol",
    "dataAnnotationPlatform": "cr:dataAnnotationPlatform",
    "dataAnnotationAnalysis": "cr:dataAnnotationAnalysis",
    "dataAnnotationPerItem": "cr:dataAnnotationPeritem",
    "dataAnnotationDemographics": "cr:dataAnnotationDemographics",
    "dataBiases": "cr:dataBiases",
    "dataUseCases": "cr:dataUsecases",
    "dataLimitations": "cr:dataLimitation",
    "dataSocialImpact": "cr:dataSocialImpact",
    "dataSensitive": "cr:dataSensitive",
    "dataMaitenance": "cr:dataMaintenance",
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
}


def get_context(json_: Json) -> Json:
    """Returns the context and raises an error if it is not a dictionary as expected."""
    context = json_.get("@context", {})
    if not isinstance(context, dict):
        raise ValueError("@context should be a dictionary. Got: {existing_context}")
    return context


def make_context(**kwargs):
    """Returns the JSON-LD @context with additional keys."""
    return {**BASE_CONTEXT, **kwargs}


@dataclasses.dataclass(eq=False, repr=False)
class Rdf:
    """RDF-specific vocabulary on the metadata."""

    context: Json = dataclasses.field(default_factory=make_context)

    @classmethod
    def from_json(cls, json: Json) -> Rdf:
        """Creates a `Rdf` from JSON."""
        context = get_context(json)
        return cls(context=make_context(**context))

    @functools.cache
    def reverse_context(self) -> Json:
        """Reverses the context dictionary.

        - context = "ml"->"http://mlcommons.org/schema"
        - inverse_context = "http://mlcommons.org/schema"->"ml"
        """
        return {v: k for k, v in self.context.items() if isinstance(v, str)}

    @functools.cache
    def shorten_value(self, value: str) -> str:
        """Shortens a value according to the context if possible."""
        for url, abbreviation in self.reverse_context().items():
            is_url = value.startswith("http://") or value.startswith("https://")
            if is_url and value.startswith(url):
                return value.replace(url, f"{abbreviation}:")
        return value
