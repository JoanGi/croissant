import datetime
import enum

import streamlit as st

from core.names import find_unique_name
from core.state import Metadata
import mlcroissant as mlc


class RaiEvent(enum.Enum):
    """Event that triggers a Rai change."""

    RAI_DATA_COLLECTION = "RAI_DATA_COLLECTION"
    RAI_DATA_COLLECTION_TYPE = "RAI_DATA_COLLECTION_TYPE"
    RAI_DATA_COLLECTION_TYPE_OTHERS = "RAI_DATA_COLLECTION_TYPE_OTHERS"
    RAI_DATA_COLLECTION_MISSING_DATA = "RAI_DATA_COLLECTION_MISSING_DATA"
    RAI_DATA_COLLECTION_RAW = "RAI_DATA_COLLECTION_RAW"
    RAI_DATA_COLLECTION_TIMEFRAME_START = "RAI_DATA_COLLECTION_TIMEFRAME_START"
    RAI_DATA_COLLECTION_TIMEFRAME_END = "RAI_DATA_COLLECTION_TIMEFRAME_END"
    RAI_DATA_PREPROCESSING_IMPUTATION = "RAI_DATA_PREPROCESSING_IMPUTATION"
    RAI_DATA_PREPROCESSING_PROTOCOL = " RAI_DATA_PREPROCESSING_PROTOCOL"
    RAI_DATA_PREPROCESSING_MANIPULATION = "RAI_DATA_PREPROCESSING_MANIPULATIO"
    RAI_DATA_ANNOTATION_PROTOCOL = "RAI_DATA_ANNOTATION_PROTOCOL"
    RAI_DATA_ANNOTATION_PLATFORM = "RAI_DATA_ANNOTATION_PLATFORM"
    RAI_DATA_ANNOTATION_ANALYSIS = "RAI_DATA_ANNOTATION_ANALYSIS"
    RAI_DATA_ANNOTATION_PER_ITEM = "RAI_DATA_ANNOTATION_PERI_TEM"
    RAI_DATA_ANNOTATION_DEMOGRAPHICS = "RAI_DATA_ANNOTATION_DEMOGRAPHICS"
    RAI_DATA_ANNOTATION_TOOLS = "RAI_DATA_ANNOTATION_TOOLS"
    RAI_DATA_USE_CASES = "RAI_DATA_USECASES"
    RAI_DATA_BIAS = "RAI_DATA_BIAS"
    RAI_DATA_LIMITATION = "RAI_DATA_LIMITATION"
    RAI_DATA_SOCIAL_IMPACT = "RAI_DATA_SOCIAL_IMPACT"
    RAI_SENSITIVE = "RAI_SENSITIVE"
    RAI_MAINTENANCE = "RAI_MAINTENANCE"


def handle_rai_change(event: RaiEvent, Metadata: Metadata, key: str):
    if event == RaiEvent.RAI_DATA_COLLECTION:
        Metadata.data_collection = st.session_state[key]
    if event == RaiEvent.RAI_DATA_COLLECTION_TYPE:
        Metadata.data_collection_type = st.session_state[key]
    if event == RaiEvent.RAI_DATA_COLLECTION_TYPE_OTHERS:
        Metadata.data_collection_type_others = st.session_state[key]
    if event == RaiEvent.RAI_DATA_COLLECTION_MISSING_DATA:
        Metadata.data_collection_missing = st.session_state[key]
    if event == RaiEvent.RAI_DATA_COLLECTION_RAW:
        Metadata.data_collection_raw = st.session_state[key]
    if event == RaiEvent.RAI_DATA_COLLECTION_TIMEFRAME_START:
        date = st.session_state[key]
        Metadata.data_collection_timeframe_start = datetime.datetime(
            date.year, date.month, date.day
        )
    if event == RaiEvent.RAI_DATA_COLLECTION_TIMEFRAME_END:
        date = st.session_state[key]
        Metadata.data_collection_timeframe_end = datetime.datetime(
            date.year, date.month, date.day
        )
    if event == RaiEvent.RAI_DATA_PREPROCESSING_IMPUTATION:
        Metadata.data_preprocessing_imputation = st.session_state[key]
    if event == RaiEvent.RAI_DATA_PREPROCESSING_PROTOCOL:
        if Metadata.data_preprocessing_protocol:
            index = key.split("_")[-1]
            Metadata.data_preprocessing_protocol[int(index)] = st.session_state[key]
        else:
            Metadata.data_preprocessing_protocol = []
            Metadata.data_preprocessing_protocol.append(st.session_state[key])
    if event == RaiEvent.RAI_DATA_PREPROCESSING_MANIPULATION:
        Metadata.data_preprocessing_manipulation = st.session_state[key]
    if event == RaiEvent.RAI_DATA_ANNOTATION_PROTOCOL:

        Metadata.data_annotation_protocol = st.session_state[key]
    if event == RaiEvent.RAI_DATA_ANNOTATION_PLATFORM:
        Metadata.data_annotation_platform = st.session_state[key]
    if event == RaiEvent.RAI_DATA_ANNOTATION_ANALYSIS:
        Metadata.data_annotation_analysis = st.session_state[key]
    if event == RaiEvent.RAI_DATA_ANNOTATION_PER_ITEM:
        Metadata.data_annotation_per_item = st.session_state[key]
    if event == RaiEvent.RAI_DATA_ANNOTATION_DEMOGRAPHICS:
        Metadata.data_annotation_demographics = st.session_state[key]
    if event == RaiEvent.RAI_DATA_ANNOTATION_TOOLS:
        Metadata.data_annotation_tools = st.session_state[key]
    if event == RaiEvent.RAI_DATA_USE_CASES:

        if Metadata.data_use_cases:
            index = key.split("_")[-1]
            Metadata.data_use_cases[int(index)] = st.session_state[key]
        else:
            Metadata.data_use_cases = []
            Metadata.data_use_cases.append(st.session_state[key])

    if event == RaiEvent.RAI_DATA_BIAS:

        if Metadata.data_biases:
            index = key.split("_")[-1]
            Metadata.data_biases[int(index)] = st.session_state[key]
        else:
            Metadata.data_biases = []
            Metadata.data_biases.append(st.session_state[key])

    if event == RaiEvent.RAI_DATA_LIMITATION:
        if Metadata.data_limitation:
            index = key.split("_")[-1]
            Metadata.data_limitation[int(index)] = st.session_state[key]
        else:
            Metadata.data_limitation = []
            Metadata.data_limitation.append(st.session_state[key])
    if event == RaiEvent.RAI_DATA_SOCIAL_IMPACT:
        Metadata.data_social_impact = st.session_state[key]
    if event == RaiEvent.RAI_SENSITIVE:

        if Metadata.data_sensitive:
            index = key.split("_")[-1]
            Metadata.data_sensitive[int(index)] = st.session_state[key]
        else:
            Metadata.data_sensitive = []
            Metadata.data_sensitive.append(st.session_state[key])
    if event == RaiEvent.RAI_MAINTENANCE:
        Metadata.data_maintenance = st.session_state[key]
