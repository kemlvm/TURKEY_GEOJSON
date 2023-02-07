from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import math
from Data.List import lists, countries
from getRequest import *
import requests
import json
import csv
import streamlit as st


def app():
    st.sidebar.title("Veri Akış Çapraz Platformu")

    st.markdown("# Tam Zamanlı Veri Akışı!")

    if st.button('AFAD Ve Kandilli Rasathanesinden Alınan Verileri Güncellemek İçin Butona Basmanız Yeterli'):
        st.write('Veriler Başarılı Bir Şekilde Güncellendi!')

        def GetParamsData_ForAdana(req):
            api = req
            response = requests.get(api)

            # response.content()  # Return the raw bytes of the data payload
            # response.text()  # Return a string representation of the data payload
            # response.json()  # This method is convenient when the API returns JSON

            # with open('earthquaqe_2023.csv', 'w', encoding='UTF8') as f:
            #    writer = csv.writer(f)

            #    writer.writerow(response.text())

            getJsonData = response.json()
            # print(getJsonData.keys())
            # print(getJsonData['earthquakes'])

            class fruits(dict):
                def __str__(self):
                    return json.dumps(self)

            collect = getJsonData
            result = fruits(collect)

            df = pd.DataFrame(result['earthquakes'])

            data_file = open('afad_dataFile.csv', 'w',
                             newline='', encoding="utf-8")
            csv_writer = csv.writer(data_file)

            count = 0
            for data in result['earthquakes']:
                if count == 0:
                    header = data.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(data.values())

            data_file.close()

        def GetParamsData_ForKahramanMaras(req):
            api = req
            response = requests.get(api)

            # response.content()  # Return the raw bytes of the data payload
            # response.text()  # Return a string representation of the data payload
            # response.json()  # This method is convenient when the API returns JSON

            # with open('earthquaqe_2023.csv', 'w', encoding='UTF8') as f:
            #    writer = csv.writer(f)

            #    writer.writerow(response.text())

            getJsonData = response.json()
            # print(getJsonData.keys())
            # print(getJsonData['earthquakes'])

            class fruits(dict):
                def __str__(self):
                    return json.dumps(self)

            collect = getJsonData
            result = fruits(collect)

            df = pd.DataFrame(result['earthquakes'])

            data_file = open('afad_dataFile.csv', 'w',
                             newline='', encoding="utf-8")
            csv_writer = csv.writer(data_file)

            count = 0
            for data in result['earthquakes']:
                if count == 0:
                    header = data.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(data.values())

            data_file.close()

        def GetParamsData_ForHatay(req):
            api = req
            response = requests.get(api)

            # response.content()  # Return the raw bytes of the data payload
            # response.text()  # Return a string representation of the data payload
            # response.json()  # This method is convenient when the API returns JSON

            # with open('earthquaqe_2023.csv', 'w', encoding='UTF8') as f:
            #    writer = csv.writer(f)

            #    writer.writerow(response.text())

            getJsonData = response.json()
            # print(getJsonData.keys())
            # print(getJsonData['earthquakes'])

            class fruits(dict):
                def __str__(self):
                    return json.dumps(self)

            collect = getJsonData
            result = fruits(collect)

            df = pd.DataFrame(result['earthquakes'])

            data_file = open('afad_dataFile.csv', 'w',
                             newline='', encoding="utf-8")
            csv_writer = csv.writer(data_file)

            count = 0
            for data in result['earthquakes']:
                if count == 0:
                    header = data.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(data.values())

            data_file.close()

        GetParamsData_ForKahramanMaras(
            "https://deprem-api.vercel.app/?location=kahramanmaras")
        GetParamsData_ForHatay("https://deprem-api.vercel.app/?location=hatay")
        GetParamsData_ForAdana("https://deprem-api.vercel.app/?location=adana")

    ticker = st.sidebar.selectbox(
        'API Parametresi Seçiniz!', sorted(countries.param), index=0)

    if (ticker == "adana"):
        if ticker == "adana":
            new_ticker = "Adana İlimize Ait"
            st.header(f"{new_ticker} Ulaştığımız Son Veriler")

        st.write(adana_pd_param)

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
            data=adana_pd_param, name="cities"
        )  # Alternative: KeplerGl(height=400, data={"name": df})

        keplergl_static(map_1, center_map=True)
    if (ticker == "hatay"):
        if ticker == "hatay":
            new_ticker = "Hatay İlimize Ait"
            st.header(f"{new_ticker} Ulaştığımız Son Veriler")

        st.write(hatay_pd_param)

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
            data=hatay_pd_param, name="cities"
        )  # Alternative: KeplerGl(height=400, data={"name": df})

        keplergl_static(map_1, center_map=True)
    if (ticker == "kahramanmaras"):
        if ticker == "kahramanmaras":
            new_ticker = "Kahramanmaraş İlimize Ait"
            st.header(f"{new_ticker} Ulaştığımız Son Veriler")

        st.write(kahramanM_pd_param)

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
            data=kahramanM_pd_param, name="cities"
        )  # Alternative: KeplerGl(height=400, data={"name": df})

        keplergl_static(map_1, center_map=True)
