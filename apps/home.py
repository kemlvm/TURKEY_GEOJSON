import streamlit as st
import leafmap.foliumap as leafmap
import hydralit_components as hc
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import math
from Data.List import lists
import requests
import json
import csv
import pandas as pd

def app():
    import pymongo
    from urllib.parse import quote_plus
    menu_data = [
        {'icon': "🌏", 'label': "Tam Zamanlı Veri Akışı"},
        {'icon': "⛈️", 'label': "Tüm Depremlerin Harita Gösterimi"},
        {'icon': "🗺️", 'label': "Road Map"},
        {'icon': "➕", 'label': "Poisson Dağılımı ve Deprem Olasılığı"},

    ]

    over_theme = {'txc_inactive': '#FFFFFF',
                  'menu_background': '#55496b', 'txc_active': '#0f0f0f', 'option_active': '#b4d1d0', 'font-weight': 'bold'}

    menu_id = hc.nav_bar(
        menu_definition=menu_data, home_name='Ana Sayfa | Bilgilendirme | Kullanım', override_theme=over_theme)

    st.info("AFAD Ve Kandilli Rasathanesinden Alınan Verileri Derleyip Harmanlayıp Tek Bir Yerde Bakmanız İçin Kodlanmış Bir Uygulamadır!")

    with st.container():
        st.write("Nasıl Kullanılır? Neler Yapılır?")

        st.write(
            "Analizleriniz Sonucu Bilgilenmenizi İsterim En Faydalı Kullanmanız Dileğiyle...")

    if(menu_id == "Tam Zamanlı Veri Akışı"):
        st.sidebar.title("Canlı Veri Akışı Sunucusu")
        st.markdown("# Tam Zamanlı Veri Akışı!")

        if st.button('AFAD Ve Kandilli Rasathanesinden Alınan Verileri Güncellemek İçin Butona Basmanız Yeterli'):
            st.write('Veriler Başarılı Bir Şekilde Güncellendi!')

            def GetParamsData_ForKandilli(req):
                api = req
                response = requests.get(api)

                getJsonData = response.json()

                class fruits(dict):
                    def __str__(self):
                        return json.dumps(self)

                collect = getJsonData
                result = fruits(collect)

                username = quote_plus('eukqla')
                password = quote_plus('mQCtaLqW@yNY!8?-/prot?=ocO*l')
                uri = 'mongodb+srv://' + username + ':' + password + '@cluster0.brz7ehs.mongodb.net/?retryWrites=true&w=majority'
                client = pymongo.MongoClient(uri)

                mydb = client["TURKEYGEOJSON"]
                mycol = mydb["kandilli"]

                routerDataForInsert = mycol.insert_one(result)

                if(routerDataForInsert):
                    st.write("Kayıt yeniledi for kandilli")

            def GetParamsData_ForAfad(req):
                api = req
                response = requests.get(api)

                getJsonData = response.json()

                class fruits(dict):
                    def __str__(self):
                        return json.dumps(self)

                collect = getJsonData
                result = fruits(collect)

                username = quote_plus('eukqla')
                password = quote_plus('mQCtaLqW@yNY!8?-/prot?=ocO*l')
                uri = 'mongodb+srv://' + username + ':' + password + '@cluster0.brz7ehs.mongodb.net/?retryWrites=true&w=majority'
                client = pymongo.MongoClient(uri)

                mydb = client["TURKEYGEOJSON"]
                mycol = mydb["afad"]

                routerDataForInsert = mycol.insert_one(result)

                if(routerDataForInsert):
                    st.write("Kayıt yeniledi for afad")
                

            GetParamsData_ForAfad("https://deprem-api.vercel.app/?type=afad")
            GetParamsData_ForKandilli("https://deprem-api.vercel.app/")

        ticker = st.sidebar.selectbox(
            'API Parametresi Seçiniz!', sorted(lists.param), index=0)

        if (ticker == "kandilli"):
            if ticker == "kandilli":
                new_ticker = "Kandilli Rasathanesinden"
                st.header(
                    f"{new_ticker} Ulaştığımız Son 500 Depreme Ait Veriler")

            username = quote_plus('eukqla')
            password = quote_plus('mQCtaLqW@yNY!8?-/prot?=ocO*l')
            uri = 'mongodb+srv://' + username + ':' + password + '@cluster0.brz7ehs.mongodb.net/?retryWrites=true&w=majority'
            client = pymongo.MongoClient(uri)

            mydb = client["TURKEYGEOJSON"]
            mycol = mydb["kandilli"]

            routerDataForFindAndUseKandilli = mycol.find_one()

            df_forKandilli = pd.DataFrame(routerDataForFindAndUseKandilli['earthquakes'])

            st.dataframe(df_forKandilli, use_container_width=1000)

            st.subheader(
                f"{new_ticker} Tarafından Ulaştığımız Son 100 Depreme Ait Veriler Şu Anda Tam Zamanlı Olarak Veri Görselleştirilmesi Yapılıyor!")

            config = {
                "version": "v1",
                "config": {
                    "mapState": {
                        "bearing": 0,
                        "latitude": 52.52,
                        "longitude": 13.4,
                        "pitch": 0,
                        "zoom": 11,
                    }
                },
            }

            map_1 = KeplerGl(height=900)
            map_1.config = config
            map_1.add_data(
                data=df_forKandilli, name="cities"
            )  # Alternative: KeplerGl(height=400, data={"name": df})

            keplergl_static(map_1, center_map=True)

        if (ticker == "afad"):
            if ticker == "afad":
                new_ticker = "AFAD"
                st.header(
                    f"{new_ticker} Tarafından Ulaştığımız Son 100 Depreme Ait Veriler")

            username = quote_plus('eukqla')
            password = quote_plus('mQCtaLqW@yNY!8?-/prot?=ocO*l')
            uri = 'mongodb+srv://' + username + ':' + password + '@cluster0.brz7ehs.mongodb.net/?retryWrites=true&w=majority'
            client = pymongo.MongoClient(uri)

            mydb = client["TURKEYGEOJSON"]
            mycol = mydb["afad"]

            routerDataForFindAndUse = mycol.find_one()

            df_forAFAD = pd.DataFrame(routerDataForFindAndUse['earthquakes'])

            st.dataframe(df_forAFAD, use_container_width=1000)

            st.subheader(
                f"{new_ticker} Tarafından Ulaştığımız Son 100 Depreme Ait Veriler Şu Anda Tam Zamanlı Olarak Veri Görselleştirilmesi Yapılıyor!")

            config = {
                "version": "v1",
                "config": {
                    "mapState": {
                        "bearing": 0,
                        "latitude": 52.52,
                        "longitude": 13.4,
                        "pitch": 0,
                        "zoom": 11,
                    }
                },
            }

            map_1 = KeplerGl(height=900)
            map_1.config = config
            map_1.add_data(
                data=df_forAFAD, name="cities"
            )  # Alternative: KeplerGl(height=400, data={"name": df})

            keplergl_static(map_1, center_map=True)

    if(menu_id == "Poisson Dağılımı ve Deprem Olasılığı"):
        st.subheader(
            "Python ve Poisson Dağılımı ile Deprem Olasılığı Hesaplaması")
        st.text("Söz konusu tahmin matematiksel bir formülü kullanarak hesaplanmıştır. Hesaplanmasında kullanılan veri modeli => https://www.kaggle.com/datasets/caganseval/earthquake Kaynağından Alınmıştır!")

        df = pd.read_csv('earthquake_final.csv')

        turkey = df[df["country"] == "turkey"]

        len(turkey[turkey["richter"] >= 5.0])

        def poisson(lambd, x):
            return (math.exp(-lambd) * (lambd ** x)) / math.factorial(x)

        st.write(poisson(0.13, 3))

    if(menu_id == "Road Map"):
        st.markdown(
            """
        A [streamlit](https://streamlit.io) app template for geospatial applications based on [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu).
        To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
        https://share.streamlit.io/giswqs/streamlit-template?page=upload

        """
        )

        m = leafmap.Map(locate_control=True)
        m.add_basemap("ROADMAP")
        m.to_streamlit(height=700)

    if(menu_id == "Tüm Depremlerin Harita Gösterimi"):
        st.sidebar.title("Canlı Veri Akışı Sunucusu")

        st.markdown("# Tam Zamanlı Veri Akışı!")

        df = pd.read_csv('earthquake_final.csv')

        st.sidebar.title(
            "Earthquakes in 1910-2017, Turkey ")

        st.subheader(
            "1910 Yılından 2017 Yılına Kadar Tüm Deprem Verilerini Görselleştirebilirsiniz!")

        st.write(
            "Bu, streamlit teknolojisi ile veri girişi olan bir kepler.gl haritasıdır.")
        st.write("Bu Harita Üzerinde Tam Zamanlı Olmasada Geçmişe Dönük Bir Çok Verinin Görselleştirilmesine Göz Atabilirsiniz!")
        st.write(
            "Bu Harita Üzerinde Sadece 1910 Yılından 2017'ye Kadar Olmuş TÜRKİYE Depremlerini Görebilirsiniz!")
        st.write("Veri Modeli Kaggle'dan Alınmıştır.")
        st.write("Aşağıda ki Tabloyu Dilediğiniz Gibi Kullanabilirsiniz!")

        st.write("Haritanın Sol Üstünde Bulunan Ok İşaretine Basarak Yandan Açmış Olduğunuz Sidebar içerisinde Layerslar bulunmakta!")
        st.write(
            "Add Layer diyerek veri kümesini işleyebilir görselleştirebilirsiniz ya da en basit olarak basic kısmına gelip Select A Type Kısmından [Point]' işlemesini seçebilirsiniz")
        st.write("Lat* ve Lon* adında 2 parametre göreceksiniz yanlarında ki kısma tıklayıp açılan panelde lot için lot'u, lon için ise Long'u seçmeniz gerekmektedir!")

        st.write("Diğer ölçeklendirmeleri kullanmak isterseniz")
        st.write(
            "datetime,lat,long,country,city,area,direction,dist,depth,xm,md,richter,mw,ms,mb")

        if(st.checkbox):
            st.write(df)

        config = {
            "version": "v1",
            "config": {
                "mapState": {
                    "bearing": 0,
                    "latitude": 52.52,
                    "longitude": 13.4,
                    "pitch": 0,
                    "zoom": 11,
                }
            },
        }
        map_1 = KeplerGl(height=900)

        map_1.config = config
        map_1.add_data(
            data=df, name="cities"
        )  # Alternative: KeplerGl(height=400, data={"name": df})

        keplergl_static(map_1, center_map=True)
