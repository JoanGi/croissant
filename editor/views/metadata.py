import streamlit as st

from core.state import Metadata
from events.metadata import find_license_index
from events.metadata import handle_metadata_change
from events.metadata import LICENSES
from events.metadata import LICENSES_URL
from events.metadata import MetadataEvent


def render_metadata():
    """Renders the `Metadata` view."""
    metadata: Metadata = st.session_state[Metadata]
    col1, col2 = st.columns([1, 1])
    with col1.expander("**Generic metadata**", expanded=True):
        _render_generic_metadata(metadata)
    with col2.expander("**Instructions**", expanded=True):
        st.info("Instructions to fill up the metadata section", icon="💡")


def _render_generic_metadata(metadata: Metadata):
    """Renders all non-RAI generic metadata."""
    index = find_license_index(metadata.license)
    key = "metadata-url"
    st.text_input(
        label="URL",
        key=key,
        value=metadata.url,
        placeholder="URL to the dataset.",
        on_change=handle_metadata_change,
        args=(MetadataEvent.URL, metadata, key),
    )
    key = "metadata-version"
    st.text_input(
        label="Version (`MAJOR.MINOR.PATCH`)",
        key=key,
        help=(
            "Refer to https://semver.org/spec/v2.0.0.html for more information on the"
            " format."
        ),
        value=metadata.version,
        placeholder="1.0.0",
        on_change=handle_metadata_change,
        args=(MetadataEvent.VERSION, metadata, key),
    )
    key = "metadata-license"
    st.selectbox(
        label="License",
        help=(
            "More information on license names and meaning can be found"
            f" [here]({LICENSES_URL})."
        ),
        key=key,
        options=LICENSES.keys(),
        index=index,
        on_change=handle_metadata_change,
        args=(MetadataEvent.LICENSE, metadata, key),
    )
    key = "metadata-citation"
    st.text_area(
        label="Citation",
        key=key,
        value=metadata.citation,
        placeholder="@book{\n  title={Title}\n}",
        on_change=handle_metadata_change,
        args=(MetadataEvent.CITATION, metadata, key),
    )
    key = "metadata-date-published"
    st.date_input(
        label="Date of first broadcast/publication.",
        key=key,
        value=metadata.date_published,
        on_change=handle_metadata_change,
        args=(MetadataEvent.DATE_PUBLISHED, metadata, key),
    )
    if metadata.creators:
        creator = metadata.creators[0]
        col1, col2, col3 = st.columns([1, 1, 1])
        key = "metadata-creator-name"
        col1.text_input(
            label="Creator name",
            key=key,
            value=creator.name,
            on_change=handle_metadata_change,
            placeholder="A person or an organization",
            args=(MetadataEvent.CREATOR_NAME, metadata, key),
        )
        key = "metadata-creator-url"
        col2.text_input(
            label="Creator URL",
            key=key,
            value=creator.url,
            placeholder="https://mlcommons.org",
            on_change=handle_metadata_change,
            args=(MetadataEvent.CREATOR_URL, metadata, key),
        )
        key = "metadata-creator-remove"
        col3.button(
            "✖️",
            key=key,
            help="Remove the creator",
            on_click=handle_metadata_change,
            args=(MetadataEvent.CREATOR_REMOVE, metadata, key),
        )
    else:
        key = "metadata-add-creator"
        st.button(
            label="✚ Add a creator",
            key=key,
            on_click=handle_metadata_change,
            args=(MetadataEvent.CREATOR_ADD, metadata, key),
        )
