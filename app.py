import streamlit as st
import math

def main():
    st.title("🔧 Aplikasi Multi-Fungsi")
    st.sidebar.title("Pilih Fitur")
    
    # Sidebar untuk memilih fitur
    feature = st.sidebar.selectbox(
        "Silakan pilih fitur yang ingin digunakan:",
        ["🧮 Kalkulator Sederhana", "🌡️ Konversi Suhu", "🔢 Deret Fibonacci"]
    )
    
    if feature == "🧮 Kalkulator Sederhana":
        calculator()
    elif feature == "🌡️ Konversi Suhu":
        temperature_converter()
    elif feature == "🔢 Deret Fibonacci":
        fibonacci_sequence()

def calculator():
    st.header("🧮 Kalkulator Sederhana")
    st.write("Masukkan dua angka dan pilih operasi yang diinginkan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        angka1 = st.number_input("Angka 1", value=0, step=1)
    
    with col2:
        angka2 = st.number_input("Angka 2", value=0, step=1)
    
    operator = st.selectbox(
        "Pilih Operator:",
        ["+", "-", "×", "÷", "^", "√"]
    )
    
    if st.button("Hitung", key="calc"):
        try:
            if operator == "+":
                result = angka1 + angka2
                st.success(f"Hasil: {angka1} + {angka2} = **{result}**")
            elif operator == "-":
                result = angka1 - angka2
                st.success(f"Hasil: {angka1} - {angka2} = **{result}**")
            elif operator == "×":
                result = angka1 * angka2
                st.success(f"Hasil: {angka1} × {angka2} = **{result}**")
            elif operator == "÷":
                if angka2 != 0:
                    result = angka1 / angka2
                    st.success(f"Hasil: {angka1} ÷ {angka2} = **{result}**")
                else:
                    st.error("Error: Tidak dapat membagi dengan nol!")
            elif operator == "^":
                result = angka1 ** angka2
                st.success(f"Hasil: {angka1} ^ {angka2} = **{result}**")
            elif operator == "√":
                if angka1 >= 0:
                    result = math.sqrt(angka1)
                    st.success(f"Hasil: √{angka1} = **{result}**")
                    st.info("Catatan: Akar kuadrat menggunakan Angka 1")
                else:
                    st.error("Error: Tidak dapat menghitung akar kuadrat dari bilangan negatif!")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")

def temperature_converter():
    st.header("🌡️ Konversi Suhu")
    st.write("Konversi suhu antar satuan Celsius, Reamur, dan Fahrenheit")
    
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("Dari satuan:", ["Celsius", "Reamur", "Fahrenheit"])
        temperature = st.number_input("Masukkan suhu:", value=0.0, format="%.2f")
    
    with col2:
        to_unit = st.selectbox("Ke satuan:", ["Celsius", "Reamur", "Fahrenheit"])
    
    if st.button("Konversi", key="temp"):
        try:
            # Konversi ke Celsius terlebih dahulu
            if from_unit == "Celsius":
                celsius = temperature
            elif from_unit == "Reamur":
                celsius = temperature * 5/4
            elif from_unit == "Fahrenheit":
                celsius = (temperature - 32) * 5/9
            
            # Konversi dari Celsius ke satuan tujuan
            if to_unit == "Celsius":
                result = celsius
            elif to_unit == "Reamur":
                result = celsius * 4/5
            elif to_unit == "Fahrenheit":
                result = celsius * 9/5 + 32
            
            st.success(f"**{temperature}° {from_unit}** = **{result:.2f}° {to_unit}**")
            
            # Menampilkan konversi ke semua satuan
            st.info("**Konversi lengkap:**")
            celsius_val = celsius
            reamur_val = celsius * 4/5
            fahrenheit_val = celsius * 9/5 + 32
            
            st.write(f"• Celsius: {celsius_val:.2f}°C")
            st.write(f"• Reamur: {reamur_val:.2f}°R")
            st.write(f"• Fahrenheit: {fahrenheit_val:.2f}°F")
            
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")

def fibonacci_sequence():
    st.header("🔢 Deret Fibonacci")
    st.write("Generate deret Fibonacci hingga n buah nilai")
    
    n = st.number_input("Masukkan jumlah nilai Fibonacci (n):", min_value=1, max_value=100, value=10, step=1)
    
    if st.button("Generate Deret Fibonacci", key="fib"):
        try:
            fibonacci_list = generate_fibonacci(n)
            
            st.success(f"**Deret Fibonacci untuk {n} nilai pertama:**")
            
            # Menampilkan dalam bentuk yang mudah dibaca
            fib_str = " → ".join(map(str, fibonacci_list))
            st.write(f"**{fib_str}**")
            
            # Menampilkan dalam bentuk tabel untuk nilai yang banyak
            if n > 10:
                st.write("**Dalam bentuk tabel:**")
                import pandas as pd
                
                # Membuat DataFrame untuk ditampilkan
                df_data = []
                for i, val in enumerate(fibonacci_list, 1):
                    df_data.append({"Posisi": i, "Nilai Fibonacci": val})
                
                df = pd.DataFrame(df_data)
                st.dataframe(df, hide_index=True)
            
            # Informasi tambahan
            st.info(f"**Informasi:**")
            st.write(f"• Nilai terbesar: {max(fibonacci_list)}")
            st.write(f"• Jumlah total: {sum(fibonacci_list)}")
            
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")

def generate_fibonacci(n):
    """Generate deret Fibonacci hingga n nilai"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_list = [0, 1]
    for i in range(2, n):
        next_fib = fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(next_fib)
    
    return fibonacci_list

# Menjalankan aplikasi
if __name__ == "__main__":
    # Konfigurasi halaman
    st.set_page_config(
        page_title="Aplikasi Multi-Fungsi",
        page_icon="🔧",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Menjalankan aplikasi utama
    main()
    
   