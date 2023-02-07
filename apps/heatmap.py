import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Isı Haritası")

    filepath = "https://raw.githubusercontent.com/kemlvm/TURKEY_GEOJSON/main/tr_cities.csv?token=GHSAT0AAAAAAB6O4V5OJME64RVZNSWTUIHOY7CT4MQ"
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="lat",
        longitude="lng",
        value="population",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(height=700)
