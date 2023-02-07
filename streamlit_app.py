import streamlit as st
from streamlit_option_menu import option_menu
from apps import ForCitiesRealTimeData, home, heatmap, upload,readEarthquake

st.set_page_config(page_title="Canlı Veri Akışı", layout="wide")

apps = [
    {"func": home.app, "title": "Ana Sayfa", "icon": "house"},
    {"func": ForCitiesRealTimeData.app,
     "title": "Şehirlere Göre Özel Filtreleme [AFAD] [Kandilli]", "icon": "cloud-upload"},
    {"func": readEarthquake.app,
     "title": "Deprem Planları, Neler Yapılmalı?", "icon": "cloud-upload"},
    {"func": upload.app, "title": "Verikümesi Vektörleri Yükleyin",
     "icon": "cloud-upload"},
    {"func": heatmap.app, "title": "Isı Haritası", "icon": "map"},

]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Ana Menü",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("GEÇMİŞ OLSUN TÜM TÜRKİYE!")
    st.sidebar.info(
        """
        AFAD Ve Kandilli Rasathanesinden Alınan Verileri Derleyip Harmanlayıp Tek Bir Yerde Bakmanız İçin Kodlanmış Bir Uygulamadır! \n
        Tam Zamanlı Veri Akışı Ve Harita Üzerinde Veri Analizi Servisleri Sağlanmaktadır. \n 
        Poisson Dağılımı ve Deprem Olasılığı Üzerine Matematiksel Sonuçlarda Bulunmamıza Yarayan Algoritmalar Yazılmıştır!
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
