
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

# Sayfa ayarları
st.set_page_config(page_title=" İzmir'de Ev Fiyat Tahmini", page_icon="🏠", layout="centered")
st.markdown("<h1 style='text-align: center; color:rgb(246, 250, 253);'>🏠 İzmir'de Ev Fiyat Tahmini Aracı</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp {
        background: 
            linear-gradient(rgba(132, 133, 130, 0.6), rgba(132, 133, 130, 0.6)), 
            url("https://blog.corendonairlines.com/wp-content/uploads/2024/04/izmir01.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;

        padding: 2rem;
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Model pipeline'ını yüklüyoruz
model = pickle.load(open("model_pipeline.pkl", "rb"))  

@st.cache_data
def get_izmir_districts():
    response = requests.get("https://turkiyeapi.dev/api/v1/provinces")
    provinces = response.json()["data"]
    izmir = next((province for province in provinces if province["name"] == "İzmir"), None)
    if izmir:
        province_id = izmir["id"]
        detail = requests.get(f"https://turkiyeapi.dev/api/v1/provinces/{province_id}").json()
        return {district["name"]: district["id"] for district in detail["data"]["districts"]}
    else:
        return {}

@st.cache_data
def get_mahalleler(ilce_id):
    url = f"https://turkiyeapi.dev/api/v1/neighborhoods?districtId={ilce_id}"
    response = requests.get(url)
    data = response.json()
    if "data" in data:
        return [neighborhood["name"] for neighborhood in data["data"]]
    else:
        return []

# İlçe ve mahalle seçim
ilceler = get_izmir_districts()
ilce = st.selectbox("İlçe Seçiniz", sorted(ilceler.keys()), key="ilce_selectbox")
mahalleler = get_mahalleler(ilceler[ilce])
mahalle = st.selectbox("Mahalle Seçiniz", sorted(mahalleler) if mahalleler else ["Veri Yok"], key="mahalle_selectbox")

# Kullanıcı girişi
col1, col2 = st.columns(2)

with col1:
    alan = st.number_input("Alan (m²)", min_value=20, max_value=1000, step=1)
    bina_yasi = st.number_input("Bina Yaşı", min_value=0, max_value=100, step=1)
    konum = st.selectbox("Konum Merkezi mi?", ["Evet", "Hayır"])
    deniz = st.selectbox("Deniz Manzarası Var mı?", ["Var", "Yok"])
    site = st.selectbox("Site İçinde mi?", ["Evet", "Hayır"])

with col2:
    havuz = st.selectbox("Havuz Var mı?", ["Var", "Yok"])
    villa = st.selectbox("Villa mı?", ["Evet", "Hayır"])
    kat = st.selectbox("Kat Seçiniz", ['Ara Kat', 'Villa Katı', 'Zemin Kat', 'Çatı Katı', 'Yüksek Kat', 'Kot'])

# Sayısal dönüşüm
binary_map = {"Evet": 1, "Hayır": 0, "Var": 1, "Yok": 0}
konum = binary_map[konum]
deniz = binary_map[deniz]
site = binary_map[site]
havuz = binary_map[havuz]
villa = binary_map[villa]

# Tahmin için DataFrame oluştur (pipeline buna göre hazır)
input_df = pd.DataFrame({
    'Alan': [alan],
    'Bina Yaşı': [bina_yasi],
    'Konum': [konum],
    'Deniz': [deniz],
    'Site': [site],
    'Havuz': [havuz],
    'Villa': [villa],
    'İlçe': [ilce],
    'Mahalle': [mahalle],
    'Kat': [kat]
})

# Tahmin butonu
if st.button("Tahmini Göster"):
    prediction_log = model.predict(input_df)  # pipeline sayesinde tüm ön işlemeler otomatik
    prediction = np.expm1(prediction_log)     # log dönüşüm tersine çevriliyor
    st.success(f"Tahmini Ev Fiyatı: {int(prediction[0]):,} TL")

