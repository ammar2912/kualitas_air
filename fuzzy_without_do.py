import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

def interpretasi_sugeno(nilai):
    return "Baik" if nilai > 50 else "Buruk"

def hitung_sugeno(suhu_input, tds_input, ph_input):
    # Definisi variabel fuzzy
    suhu_var = ctrl.Antecedent(np.arange(0, 100, 0.1), 'suhu')
    tds_var = ctrl.Antecedent(np.arange(0, 600, 0.1), 'tds')
    ph_var = ctrl.Antecedent(np.arange(0, 30, 0.1), 'ph')

    # Membership Functions untuk Input
    suhu_var['dingin'] = fuzz.trimf(suhu_var.universe, [0, 10, 20])
    suhu_var['normal'] = fuzz.trimf(suhu_var.universe, [15, 25, 35])
    suhu_var['panas'] = fuzz.trimf(suhu_var.universe, [30, 60, 100])

    tds_var['baik'] = fuzz.trimf(tds_var.universe, [0, 75, 151])
    tds_var['buruk'] = fuzz.trimf(tds_var.universe, [151, 400, 600])

    ph_var['asam'] = fuzz.trimf(ph_var.universe, [0, 3, 6])
    ph_var['netral'] = fuzz.trimf(ph_var.universe, [6, 7, 8])
    ph_var['basa'] = fuzz.trimf(ph_var.universe, [8, 15, 30])

    # Nilai konsekuen dalam Sugeno
    nilai_kualitas_air = {
        'buruk': 30,
        'baik': 70
    }

    # Aturan Fuzzy
    aturan_sugeno = [
        (['dingin', 'baik', 'asam'], 'baik'),
        (['dingin', 'baik', 'netral'], 'baik'),
        (['dingin', 'baik', 'basa'], 'baik'),
        (['dingin', 'buruk', 'asam'], 'buruk'),
        (['dingin', 'buruk', 'netral'], 'buruk'),
        (['dingin', 'buruk', 'basa'], 'buruk'),
        (['normal', 'baik', 'asam'], 'baik'),
        (['normal', 'baik', 'netral'], 'baik'),
        (['normal', 'baik', 'basa'], 'baik'),
        (['normal', 'buruk', 'asam'], 'buruk'),
        (['normal', 'buruk', 'netral'], 'buruk'),
        (['normal', 'buruk', 'basa'], 'buruk'),
        (['panas', 'baik', 'asam'], 'baik'),
        (['panas', 'baik', 'netral'], 'baik'),
        (['panas', 'baik', 'basa'], 'baik'),
        (['panas', 'buruk', 'asam'], 'buruk'),
        (['panas', 'buruk', 'netral'], 'buruk'),
        (['panas', 'buruk', 'basa'], 'buruk'),
    ]

    numerator = 0
    denominator = 0
    
    for kondisi, konsekuen in aturan_sugeno:
        # Hitung derajat keanggotaan untuk setiap aturan
        mu_suhu = fuzz.interp_membership(suhu_var.universe, suhu_var[kondisi[0]].mf, suhu_input)
        mu_tds = fuzz.interp_membership(tds_var.universe, tds_var[kondisi[1]].mf, tds_input)
        mu_ph = fuzz.interp_membership(ph_var.universe, ph_var[kondisi[2]].mf, ph_input)
        
        # Nilai firing strength
        firing_strength = np.fmin.reduce([mu_suhu, mu_tds, mu_ph])
        
        konsekuen_value = nilai_kualitas_air[konsekuen]
        
        # Weighted sum formula untuk Sugeno
        numerator += firing_strength * konsekuen_value
        denominator += firing_strength

    if denominator == 0:
        hasil = 0  # Jika tidak ada aturan yang aktif, hasilnya 0
    else:
        hasil = numerator / denominator

    label = interpretasi_sugeno(hasil)

    return label

# Contoh Input
input_suhu = 25
input_ph = 7
input_tds = 40

# Hitung output Sugeno
kategori_kualitas = hitung_sugeno(input_suhu, input_tds, input_ph)

print(f"Kualitas Air (Sugeno): {kategori_kualitas}")
