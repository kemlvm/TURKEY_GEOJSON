import json
import os.path
import csv
import os
import pandas as pd
import requests
import pandas as pd
from requests.exceptions import Timeout


def ExecuteForKandilli(url):
    try:
        Get_Data = requests.get(url, params=None, headers=None,
                                cookies=None, auth=None, timeout=None)

        class System(object):
            if (Get_Data.reason):
                str(Get_Data)
                if(Get_Data.reason == "OK"):
                    print(
                        f"\n Veri Akışı Aktif ve STATUS CODE => {Get_Data.status_code}")
                    Info = """
                            =>   Yanıt kodu	Anlamı
                            |       200	    Eğer bir sonuç varsa, sonucun başarılı bir şekilde geri getirildiğini belirtir.
                            |       301	    Sunucu ilgili isteği farklı bir endpoint’e yönlendirmektedir. Alan adı değişikliklerinde görülür.
                            |       400	    Sunucu yanlış bir istek yolladığınızı düşünür.
                            |       401	    API kimlik bilgilerinin girilmediğini veya hatalı girildiğini belirtir.
                            |       403	    Erişilmek istenilen kaynağa erişmenizin yasak olduğunu belirtir.
                            |       404	    Erişmek istediğiniz noktanın sunucuda bulunmadığını belirtir.
                            |       503	    Sunucu isteğe yanıt vermek için hazır değildir.
                        """
                    print(Info)
            else:
                print("API Kapalı! Manuele Geçiş İçin Kodları İnceleyiniz.")

    except Timeout:
        print('Zaman aşımı!')
    else:
        print('Kandilli Veri Akışı İçin Her şey yolunda! \n')


def ExecuteForAfad(url):
    try:
        Get_Data = requests.get(url, params=None, headers=None,
                                cookies=None, auth=None, timeout=None)

        class System(object):
            if (Get_Data.reason):
                str(Get_Data)
                if(Get_Data.reason == "OK"):
                    print(
                        f"\n Veri Akışı Aktif ve STATUS CODE => {Get_Data.status_code}")
                    Info = """
                            =>   Yanıt kodu	Anlamı
                            |       200	    Eğer bir sonuç varsa, sonucun başarılı bir şekilde geri getirildiğini belirtir.
                            |       301	    Sunucu ilgili isteği farklı bir endpoint’e yönlendirmektedir. Alan adı değişikliklerinde görülür.
                            |       400	    Sunucu yanlış bir istek yolladığınızı düşünür.
                            |       401	    API kimlik bilgilerinin girilmediğini veya hatalı girildiğini belirtir.
                            |       403	    Erişilmek istenilen kaynağa erişmenizin yasak olduğunu belirtir.
                            |       404	    Erişmek istediğiniz noktanın sunucuda bulunmadığını belirtir.
                            |       503	    Sunucu isteğe yanıt vermek için hazır değildir.
                        """
                    print(Info)
            else:
                print("API Kapalı! Manuele Geçiş İçin Kodları İnceleyiniz.")

    except Timeout:
        print('Zaman aşımı!')
    else:
        print('AFAD Veri Akışı İçin Her şey yolunda! \n')


os.system("cls")

ExecuteForKandilli("https://deprem-api.vercel.app/")
ExecuteForAfad("https://deprem-api.vercel.app/?type=afad")


choose = input("API Parametresi Seçiniz: ")
print("\n\n")
print("Aktif Parametreler => [kandilli,afad]")


def GetParamsData_ForKandilli(req):
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

    data_file = open('kandilli_dataFile.csv', 'w',
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


def GetParamsData_ForAfad(req):
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

    data_file = open('afad_dataFile.csv', 'w', newline='', encoding="utf-8")
    csv_writer = csv.writer(data_file)

    count = 0
    for data in result['earthquakes']:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())

    data_file.close()


if(choose == "kandilli"):
    GetParamsData_ForKandilli("https://deprem-api.vercel.app/")
    print(
        "Kandilli Rasathanesine Göre Son 500 Deprem [kandilli_dataFile.csv] Dosyasına Kaydedildi!")
    input("Kapatmak İçin Herhangi Bir Tuşa Basın.")

elif(choose == "afad"):
    GetParamsData_ForAfad("https://deprem-api.vercel.app/?type=afad")
    print(
        "AFAD'a Göre Son 100 Deprem [afad_dataFile.csv] Dosyasına Kaydedildi!")
    input("Kapatmak İçin Herhangi Bir Tuşa Basın.")

else:
    print("Geçerli Parametre Seçilmedi!")
    quit()
