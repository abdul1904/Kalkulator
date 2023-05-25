import streamlit as st
from streamlit_option_menu import option_menu
import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

page_bg_img ="""
<style>
[data-testid="stAppViewContainer"]{
background-image : url("https://e0.pxfuel.com/wallpapers/902/723/desktop-wallpaper-a-boy-sexy-anime-boy-wings-birds-art-white-background-band-book-cool-brown-hair-blonde-hair-guy-male.jpg");
background-size : cover;
}

[data-testid="stSidebar"]{
background-image: url("https://wallpaperaccess.com/full/3087165.jpg");
background-size: cover;

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
with st.sidebar :
    selected = option_menu ("Pilih Jenis Rangkaian dengan Konfigurasi Common Emitter",
    ["Home",
    "Rangkaian Fixed Bias",
    "Rangkaian Voltage Divider Bias",
    "Rangkaian Feedback Collector",],
    default_index=0)

if(selected == "Home") :
    st.header(":blue[Kalkulator Perhitungan Rangkaian BJT Analisis DC dan AC model re (Ai, Zi, Av dan Zo)]")
    st.subheader(":blue[By abdul Rahman (11-2021-023)]:orange[dari ITENAS Program Studi Teknik Elektro]")
    st.write(":blue[Program ini dibuat untuk memenuhi Tugas Besar Elektronika Analog\nDosen Pengampu : Ir. Rustamaji M.T]")
    st.image("ITENAS.jpeg", width=500)
   

if(selected == "Rangkaian Fixed Bias") :
    st.title(":green[_Contoh Rangkaian Fixed Bias Konfigurasi Common Emitter_]")
    st.image("Fixed.jpg", width = 500)
    st.title(":green[_Rangkaian Ekivalen model re Fixed Bias Konfigurasi Common Emitter_]")
    st.image("Fixed Ekivalen.jpg", width = 500)
    st.subheader(":green[_Perhitungan Analisis DC dan Perhitungan Ai, Zi, Av dan Zo model re_]")

    a=st.number_input(":green[Masukkan Nilai VCC (Volt)]",0)
    b=st.number_input(":green[Masukkan Nilai β]",0)
    c=st.number_input(":green[Masukkan Nilai RB (Ohm)]",0)
    g=st.number_input(":green[Masukkan nilai RC (Ohm)]",0)
    f=st.number_input(":green[Masukkan Nilai ro(jika ada) (Ohm)]",0)
    h=st.number_input(":green[Masukkan nilai Tegangan Input (Volt)]",0.0000)
    d=st.number_input(":green[Masukkan nilai Kapasitor Coupling1 (MikroFarad)]",0)
    e=st.number_input(":green[Masukkan nilai Kapasitor Coupling2 (MikroFarad)]",0)
    hitung = st.button(":green[Analisis DC dan Ai,Zi,Av dan Zo]")

    if hitung :
        ib=(a-0.7)/c
        ie=(b+1)*ib
        ic=b*ib
        re=0.026/ie
        bre=(b)*re
        Zi=((c*bre)/(c+bre))
        Zo=g
        ai=b
        av=-(g/re)
        #jika ada ro
        Zoro=((f*g)/(f+g))
        av1=-(Zoro/re)
        vo=av*h
        vo1=av1*h
        st.write(":green[HASIL PERHITUNGAN JIKA RO TIDAK DIKETAHUI]")
        st.write(":green[ANALISIS DC]")
        st.success(f":green[Nilai arus IB = {ib} A]")
        st.success(f":green[Nilai arus IC = {ic} A]")
        st.success(f":green[Nilai arus IE = {ie} A]")
        st.write(":green[ANALISIS AC model re]")
        st.success(f":green[Nilai re = {re} Ohm]")
        st.success(f":green[Nilai Penguatan Arus Sebesar = {ai} kali]")
        st.success(f":green[Nilai Impedansi Input Sebesar = {Zi} Ohm]")
        st.success(f":green[Nilai Penguatan Tegangan Sebesar = {av} kali]")
        st.success(f":green[Nilai Impedansi Output Sebesar = {Zo} Ohm]")
        st.success(f":green[Nilai Tegangan Output Sebesar = {vo} Volt]")
        st.write(":green[HASIL PERHITUNGAN JIKA RO DIKETAHUI]")
        st.write(":green[ANALISIS DC]")
        st.success(f":green[Nilai arus IB = {ib} A]")
        st.success(f":green[Nilai arus IC = {ic} A]")
        st.success(f":green[Nilai arus IE = {ie} A]")
        st.write(":green[ANALISIS AC model re]")
        st.success(f":green[Nilai re = {re} Ohm]")
        st.success(f":green[Nilai Penguatan Arus Sebesar = {ai} kali]")
        st.success(f":green[Nilai Impedansi Input Sebesar = {Zi} Ohm]")
        st.success(f":green[Nilai Penguatan Tegangan Sebesar = {av1} kali]")
        st.success(f":green[Nilai Impedansi Output Sebesar = {Zoro} Ohm]")
        st.success(f":green[Nilai Tegangan Output Sebesar = {vo1} Volt]")
        t1 =np.arange(0.0, 5.0, 0.1)
        t2 =np.arange(0.0, 5.0, 0.02)

        two_subplot_fig = plt.figure(figsize=(6,6))
        plt.subplot(211)
        plt.title("Tegangan Output jika RO Tidak Diketahui diketahui")
        plt.ylabel('Amplitude (V)')
        plt.xlabel('Time (s)')
        plt.plot(t1, vo*np.sin(2*np.pi*t1), color='tab:blue', linestyle='--', marker=',')

        plt.subplot(212)
        plt.title("Tegangan Output jika RO diketahui")
        plt.ylabel('Amplitude (V)')
        plt.xlabel('Time (s)')
        plt.plot(t2, vo1*np.sin(2*np.pi*t2), color='tab:orange', linestyle='--', marker='.')

        st.pyplot(two_subplot_fig)

if(selected == "Rangkaian Voltage Divider Bias") :
    st.title(":violet[_Contoh Rangkaian Voltage Divider Bias Konfigurasi Common Emitter_]")
    st.image("Divider.jpg", width = 500)
    st.title(":violet[Rangkaian Ekivalen model re Voltage Divider Bias Konfigurasi Common Emitter_]")
    st.image("Vol Ekivalen.jpg", width = 500)
    st.subheader(":violet[_Perhitungan Analisis DC dan Perhitungan Ai, Zi, Av dan Zo model re_]")

    a=st.number_input(":violet[Masukkan Nilai VCC (Volt)]",0)
    b=st.number_input(":violet[Masukkan Nilai β ]",0)
    c=st.number_input(":violet[Masukkan Nilai R1 (Ohm)]",0)
    d=st.number_input(":violet[Masukkan Nilai R2 (Ohm)]",0)
    e=st.number_input(":violet[Masukkan Nilai RC (Ohm)]",0)
    f=st.number_input(":violet[Masukkan Nilai RE (Ohm)]",0)
    j=st.number_input(":violet[Masukkan Nilai ro(jika ada) (Ohm)]",0)
    z=st.number_input(":violet[Masukkan nilai Tegangan Input (Volt)]",0.0000)
    g=st.number_input(":violet[Masukkan nilai Kapasitor Coupling1 (MikroFarad)]",0)
    h=st.number_input(":violet[Masukkan nilai Kapasitor Coupling2 (MikroFarad)]",0)
    i=st.number_input(":violet[Masukkan nilai Kapasitor Bypass (MikroFarad)]",0)
    hitung = st.button(":violet[Analisis DC dan Ai,Zi,Av dan Zo]")

    if hitung :
        VB=(d/(d+c))*a
        VE=VB-0.7
        rth=((c*d)/(c+d))
        z=rth+(f*(1+b))
        ib1=VE/z
        ie1=VE/f
        ic1=ie1-ib1
        re1=0.026/ie1
        bre=b*re1
        ai1=((b*(rth))/(rth+bre))
        Zi1=((rth*bre)/(rth+bre))
        Zo1=e
        av1=-(e/re1)
        #jika ro diketahui
        zi=Zi1
        zo=((e*j)/(e+j))
        Av=-(zo/re1)
        vo=av1*z
        vo1=Av*z
        st.write(":violet[HASIL PERHITUNGAN JIKA RO TIDAK DIKETAHUI]")
        st.write(":violet[ANALISIS DC]")
        st.success(f":violet[Nilai arus IB = {ib1} A]")
        st.success(f":violet[Nilai arus IC = {ic1} A]")
        st.success(f":violet[Nilai arus IE = {ie1} A]")
        st.write(":violet[ANALISIS AC model re]")
        st.success(f":violet[Nilai re = {re1} Ohm]")
        st.success(f":violet[Nilai Penguatan Arus Sebesar = {ai1} kali]")
        st.success(f":violet[Nilai Impedansi Input Sebesar = {Zi1} Ohm]")
        st.success(f":violet[Nilai Penguatan Tegangan Sebesar = {av1} kali]")
        st.success(f":violet[Nilai Impedansi Output Sebesar = {Zo1} Ohm]")
        st.success(f":violet[Nilai Tegangan Output Sebesar = {vo} Volt]")
        st.write(":violet[HASIL PERHITUNGAN JIKA RO DIKETAHUI]")
        st.write(":violet[ANALISIS DC]")
        st.success(f":violet[Nilai arus IB = {ib1} A]")
        st.success(f":violet[Nilai arus IC = {ic1} A]")
        st.success(f":violet[Nilai arus IE = {ie1} A]")
        st.write(":violet[ANALISIS AC model re]")
        st.success(f":violet[Nilai re = {re1} Ohm]")
        st.success(f":violet[Nilai Penguatan Arus Sebesar = {ai1} kali]")
        st.success(f":violet[Nilai Impedansi Input Sebesar = {zi} Ohm]")
        st.success(f":violet[Nilai Penguatan Tegangan Sebesar = {Av} kali]")
        st.success(f":violet[Nilai Impedansi Output Sebesar = {zo} Ohm]")
        st.success(f":violet[Nilai Tegangan Output Sebesar = {vo1} Volt]")

        t1 =np.arange(0.0, 5.0, 0.1)
        t2 =np.arange(0.0, 5.0, 0.02)
        two_subplot_fig = plt.figure(figsize=(6,6))
        plt.subplot(211)
        plt.title("Tegangan Output jika RO Tidak Diketahui diketahui")
        plt.ylabel('Amplitude (V)')
        plt.xlabel('Time (s)')
        plt.plot(t1, vo*np.sin(2*np.pi*t1), color='tab:blue', linestyle='--', marker=',')

        plt.subplot(212)
        plt.title("Tegangan Output jika RO diketahui")
        plt.ylabel('Amplitude (V)')
        plt.xlabel('Time (s)')
        plt.plot(t2, vo1*np.sin(2*np.pi*t2), color='tab:orange', linestyle='--', marker='.')

        st.pyplot(two_subplot_fig)

if(selected == "Rangkaian Feedback Collector") :
    st.title(":orange[_Contoh Rangkaian Feedback Collector Bias Konfigurasi Common Emitter_]")
    st.image("Feed.jpg", width = 500)
    st.title(":orange[_Rangkaian Ekivalen model re Feedback Collector Bias Konfigurasi Common Emitter_]")
    st.image("Feed Ekivalen.jpg", width = 500)
    st.subheader(":orange[_Perhitungan Analisis DC dan Perhitungan Ai, Zi, Av dan Zo model re_]")
    
    a=st.number_input(":orange[Masukkan Nilai VCC (Volt)]",0)
    b=st.number_input(":orange[Masukkan Nilai β ]",0)
    c=st.number_input(":orange[Masukkan Nilai Rf (Ohm)]",0)
    d=st.number_input(":orange[Masukkan Nilai RC (Ohm)]",0)
    e=st.number_input(":orange[Masukkan Nilai ro(jika ada) (Ohm)]",0)
    z=st.number_input(":orange[Masukkan nilai Tegangan Input (Volt)]",0.0000)
    f=st.number_input(":orange[Masukkan nilai Kapasitor Coupling1 (MikroFarad)]",0)
    g=st.number_input(":orange[Masukkan nilai Kapasitor Coupling2 (MikroFarad)]",0)
    hitung = st.button(":orange[Analisis DC dan Ai,Zi,Av dan Zo]")

    if hitung :
        ib = (a-0.7)/(c+(b*d))
        ie = (b+1)*ib
        ic = ib*b
        re = 0.026/ie
        ai = c/d
        zi = re/((1/b)+(d/(d+c)))
        zo = (c*d)/(c+d)
        av = -(d/re)
        #ro diketahui
        rc=((d*e)/(d+e))
        atas=(1+(rc/c))/((1/b*re)+(1/c)+(rc/b*re*c)+(rc/c*re))
        zi1=atas
        p = ((e*d)/(e+d))
        zo1 = ((p*c)/(p+c))
        o = -(c/(p+c))
        av1 = o*(p/re)
        vo=av*z
        vo1=av1*z
        st.write(":orange[HASIL PERHITUNGAN JIKA RO TIDAK DIKETAHUI]")
        st.write(":orange[ANALISIS DC]")
        st.success(f":orange[Nilai arus IB = {ib} A]")
        st.success(f":orange[Nilai arus IC = {ic} A]")
        st.success(f":orange[Nilai arus IE = {ie} A]")
        st.write(":orange[ANALISIS AC model re]")
        st.success(f":orange[Nilai re = {re} Ohm]")
        st.success(f":orange[Nilai Penguatan Arus Sebesar = {ai} kali]")
        st.success(f":orange[Nilai Impedansi Input Sebesar = {zi} Ohm]")
        st.success(f":orange[Nilai Penguatan Tegangan Sebesar = {av} kali]")
        st.success(f":orange[Nilai Impedansi Output Sebesar = {zo} Ohm]")
        st.success(f":orange[Nilai Tegangan Output Sebesar = {vo} Volt]")
        st.write(":orange[HASIL PERHITUNGAN JIKA RO DIKETAHUI]")
        st.write(":orange[ANALISIS DC]")
        st.success(f":orange[Nilai arus IB = {ib} A]")
        st.success(f":orange[Nilai arus IC = {ic} A]")
        st.success(f":orange[Nilai arus IE = {ie} A]")
        st.write(":orange[ANALISIS AC model re]")
        st.success(f":orange[Nilai re = {re} Ohm]")
        st.success(f":orange[Nilai Penguatan Arus Sebesar = {ai} kali]")
        st.success(f":orange[Nilai Impedansi Input Sebesar = {zi1} Ohm]")
        st.success(f":orange[Nilai Penguatan Tegangan Sebesar = {av1} kali]")
        st.success(f":orange[Nilai Impedansi Output Sebesar = {zo1} Ohm]")
        st.success(f":orange[Nilai Tegangan Output Sebesar = {vo1} Volt]")
        
        t1 =np.arange(0.0, 5.0, 0.1)
        t2 =np.arange(0.0, 5.0, 0.02)
        two_subplot_fig = plt.figure(figsize=(6,6))
        plt.subplot(211)
        plt.title("Tegangan Output jika RO Tidak Diketahui diketahui")
        plt.ylabel('Amplitude (V)')
        plt.xlabel('Time (s)')
        plt.plot(t1, vo*np.sin(2*np.pi*t1), color='tab:blue', linestyle='--', marker=',')

        plt.subplot(212)
        plt.title("Tegangan Output jika RO diketahui")
        plt.ylabel('Amplitude (V)')
        plt.xlabel('Time (s)')
        plt.plot(t2, vo1*np.sin(2*np.pi*t2), color='tab:orange', linestyle='--', marker='.')

        st.pyplot(two_subplot_fig)
