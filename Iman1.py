import streamlit as st
from streamlit_option_menu import option_menu
import math
from PIL import Image

with st.sidebar :
    selected = option_menu ("Pilih Jenis Rangkaian dengan Konfigurasi Common Emitter",
    ["Home",
    "Rangkaian Fixed Bias",
    "Rangkaian Voltage Divider Bias",
    "Rangkaian Feedback Collector",],
    default_index=0)

if(selected == "Home") :
    st.header(":blue[Kalkulator Perhitungan Rangkaian BJT Analisis DC dan AC model re (Ai, Zi, Av dan Zo)]")
    st.subheader(":blue[By abdul Rahman (11-2021-023)] dari :orange[ITENAS]")
    st.write(":blue[Program ini dibuat untuk memenuhi Tugas Besar Elektronika Analog\nDosen Pengampu : Ir. Rustamaji M.T]")
    st.image("ITENAS.jpeg", width=500)

if(selected == "Rangkaian Fixed Bias") :
    st.title(":green[_Contoh Rangkaian Fixed Bias Konfigurasi Common Emitter_]")
    st.image("Fixed.jpg", width = 500)
    st.subheader(":green[_Perhitungan Analisis DC dan Perhitungan Ai, Zi, Av dan Zo model re_]")

    a=st.number_input("Masukkan Nilai VCC (Volt)",0)
    b=st.number_input("Masukkan Nilai β",0)
    c=st.number_input("Masukkan Nilai RB (Ohm)",0)
    g=st.number_input("Masukkan nilai RC (Ohm)",0)
    f=st.number_input("Masukkan Nilai ro(jika ada) (Ohm)",0)
    d=st.number_input("Masukkan nilai Kapasitor Coupling1 (MikroFarad)",0)
    e=st.number_input("Masukkan nilai Kapasitor Coupling2 (MikroFarad)",0)
    hitung = st.button("Analisis DC dan Ai,Zi,Av dan Zo")

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
        st.write("HASIL PERHITUNGAN JIKA RO DIKETAHUI")
        st.write("ANALISIS DC")
        st.success(f"Nilai arus IB = {ib} A")
        st.success(f"Nilai arus IC = {ic} A")
        st.success(f"Nilai arus IE = {ie} A")
        st.write("ANALISIS AC model re")
        st.success(f"Nilai re = {re} Ohm")
        st.success(f"Nilai Penguatan Arus Sebesar = {ai} kali")
        st.success(f"Nilai Impedansi Input Sebesar = {Zi} Ohm")
        st.success(f"Nilai Penguatan Tegangan Sebesar = {av} kali")
        st.success(f"Nilai Impedansi Output Sebesar = {Zo} Ohm")
        st.write("HASIL PERHITUNGAN JIKA RO DIKETAHUI")
        st.write("ANALISIS DC")
        st.success(f"Nilai arus IB = {ib} A")
        st.success(f"Nilai arus IC = {ic} A")
        st.success(f"Nilai arus IE = {ie} A")
        st.write("ANALISIS AC model re")
        st.success(f"Nilai re = {re} Ohm")
        st.success(f"Nilai Penguatan Arus Sebesar = {ai} kali")
        st.success(f"Nilai Impedansi Input Sebesar = {Zi} Ohm")
        st.success(f"Nilai Penguatan Tegangan Sebesar = {av1} kali")
        st.success(f"Nilai Impedansi Output Sebesar = {Zoro} Ohm")

if(selected == "Rangkaian Voltage Divider Bias") :
    st.title(":violet[_Contoh Rangkaian Voltage Divider Bias Konfigurasi Common Emitter_]")
    st.image("Divider.jpg", width = 500)
    st.subheader(":violet[_Perhitungan Analisis DC dan Perhitungan Ai, Zi, Av dan Zo model re_]")
    a=st.number_input("Masukkan Nilai VCC (Volt)",0)
    b=st.number_input("Masukkan Nilai β ",0)
    c=st.number_input("Masukkan Nilai R1 (Ohm)",0)
    d=st.number_input("Masukkan Nilai R2 (Ohm)",0)
    e=st.number_input("Masukkan Nilai RC (Ohm)",0)
    f=st.number_input("Masukkan Nilai RE (Ohm)",0)
    j=st.number_input("Masukkan Nilai ro(jika ada) (Ohm)",0)
    g=st.number_input("Masukkan nilai Kapasitor Coupling1 (MikroFarad)",0)
    h=st.number_input("Masukkan nilai Kapasitor Coupling2 (MikroFarad)",0)
    i=st.number_input("Masukkan nilai Kapasitor Bypass (MikroFarad)",0)
    hitung = st.button("Analisis DC dan Ai,Zi,Av dan Zo")

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
        st.write("HASIL PERHITUNGAN JIKA RO DIKETAHUI")
        st.write("ANALISIS DC")
        st.success(f"Nilai arus IB = {ib1} A")
        st.success(f"Nilai arus IC = {ic1} A")
        st.success(f"Nilai arus IE = {ie1} A")
        st.write("ANALISIS AC model re")
        st.success(f"Nilai re = {re1} Ohm")
        st.success(f"Nilai Penguatan Arus Sebesar = {ai1} kali")
        st.success(f"Nilai Impedansi Input Sebesar = {Zi1} Ohm")
        st.success(f"Nilai Penguatan Tegangan Sebesar = {av1} kali")
        st.success(f"Nilai Impedansi Output Sebesar = {Zo1} Ohm")
        st.write("HASIL PERHITUNGAN JIKA RO DIKETAHUI")
        st.write("ANALISIS DC")
        st.success(f"Nilai arus IB = {ib1} A")
        st.success(f"Nilai arus IC = {ic1} A")
        st.success(f"Nilai arus IE = {ie1} A")
        st.write("ANALISIS AC model re")
        st.success(f"Nilai re = {re1} Ohm")
        st.success(f"Nilai Penguatan Arus Sebesar = {ai1} kali")
        st.success(f"Nilai Impedansi Input Sebesar = {zi} Ohm")
        st.success(f"Nilai Penguatan Tegangan Sebesar = {Av} kali")
        st.success(f"Nilai Impedansi Output Sebesar = {zo} Ohm")

if(selected == "Rangkaian Feedback Collector") :
    st.title(":orange[_Contoh Rangkaian Feedback Collector Bias Konfigurasi Common Emitter_]")
    st.image("Feed.jpg", width = 500)
    st.subheader(":orange[_Perhitungan Analisis DC dan Perhitungan Ai, Zi, Av dan Zo model re_]")
    a=st.number_input("Masukkan Nilai VCC (Volt)",0)
    b=st.number_input("Masukkan Nilai β ",0)
    c=st.number_input("Masukkan Nilai Rf (Ohm)",0)
    d=st.number_input("Masukkan Nilai RC (Ohm)",0)
    e=st.number_input("Masukkan Nilai ro(jika ada) (Ohm)",0)
    f=st.number_input("Masukkan nilai Kapasitor Coupling1 (MikroFarad)",0)
    g=st.number_input("Masukkan nilai Kapasitor Coupling2 (MikroFarad)",0)
    hitung = st.button("Analisis DC dan Ai,Zi,Av dan Zo")

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
        st.write("HASIL PERHITUNGAN JIKA RO DIKETAHUI")
        st.write("ANALISIS DC")
        st.success(f"Nilai arus IB = {ib} A")
        st.success(f"Nilai arus IC = {ic} A")
        st.success(f"Nilai arus IE = {ie} A")
        st.write("ANALISIS AC model re")
        st.success(f"Nilai re = {re} Ohm")
        st.success(f"Nilai Penguatan Arus Sebesar = {ai} kali")
        st.success(f"Nilai Impedansi Input Sebesar = {zi} Ohm")
        st.success(f"Nilai Penguatan Tegangan Sebesar = {av} kali")
        st.success(f"Nilai Impedansi Output Sebesar = {zo} Ohm")
        st.write("HASIL PERHITUNGAN JIKA RO DIKETAHUI")
        st.write("ANALISIS DC")
        st.success(f"Nilai arus IB = {ib} A")
        st.success(f"Nilai arus IC = {ic} A")
        st.success(f"Nilai arus IE = {ie} A")
        st.write("ANALISIS AC model re")
        st.success(f"Nilai re = {re} Ohm")
        st.success(f"Nilai Penguatan Arus Sebesar = {ai} kali")
        st.success(f"Nilai Impedansi Input Sebesar = {zi1} Ohm")
        st.success(f"Nilai Penguatan Tegangan Sebesar = {av1} kali")
        st.success(f"Nilai Impedansi Output Sebesar = {zo1} Ohm")