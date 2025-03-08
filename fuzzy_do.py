import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

def interpretasi_sugeno(nilai):
    if nilai <= 20:
        return "Sangat Buruk"
    elif nilai <= 40:
        return "Buruk"
    elif nilai <= 60:
        return "Cukup"
    elif nilai <= 80:
        return "Baik"
    else:
        return "Sangat Baik"



# Fungsi untuk menghitung output Sugeno manual
def hitung_sugeno(input_suhu, input_oksigen, input_ph, input_tds):

    # Variabel Input
    suhu_var = ctrl.Antecedent(np.arange(0, 50, 1), 'suhu')
    kadar_oksigen_var = ctrl.Antecedent(np.arange(0, 40, 1), 'kadar_oksigen')
    ph_var = ctrl.Antecedent(np.arange(0, 14, 1), 'ph')
    tds_var = ctrl.Antecedent(np.arange(0, 700, 1), 'tds')

    # Membership Functions untuk Input
    suhu_var['dingin'] = fuzz.trimf(suhu_var.universe, [0, 10, 20])
    suhu_var['normal'] = fuzz.trimf(suhu_var.universe, [15, 25, 35])
    suhu_var['panas'] = fuzz.trimf(suhu_var.universe, [30, 40, 50])

    kadar_oksigen_var['rendah'] = fuzz.trimf(kadar_oksigen_var.universe, [0, 2, 4])
    kadar_oksigen_var['sedang'] = fuzz.trimf(kadar_oksigen_var.universe, [3, 5, 7])
    kadar_oksigen_var['tinggi'] = fuzz.trimf(kadar_oksigen_var.universe, [6, 8, 40])

    ph_var['asam'] = fuzz.trimf(ph_var.universe, [0, 3, 7])
    ph_var['netral'] = fuzz.trimf(ph_var.universe, [6, 7, 8])
    ph_var['basa'] = fuzz.trimf(ph_var.universe, [7, 10, 14])

    tds_var['kecil'] = fuzz.trimf(tds_var.universe, [0, 40, 80])
    tds_var['menengah'] = fuzz.trimf(tds_var.universe, [70, 120, 155])
    tds_var['besar'] = fuzz.trimf(tds_var.universe, [150, 350, 700])

    # Nilai konsekuen dalam Sugeno (konstanta)
    nilai_kualitas_air = {
        'sangat buruk': 10,
        'buruk': 30,
        'cukup': 50,
        'baik': 70,
        'sangat baik': 90
    }

    # Aturan Fuzzy dengan Nilai Sugeno
    aturan_sugeno = [
        (['dingin', 'rendah', 'asam', 'kecil'], 'sangat buruk'),
        (['dingin', 'rendah', 'asam', 'menengah'], 'sangat buruk'),
        (['dingin', 'rendah', 'asam', 'besar'], 'sangat buruk'),
        (['dingin', 'rendah', 'netral', 'kecil'], 'buruk'),
        (['dingin', 'rendah', 'netral', 'menengah'], 'buruk'),
        (['dingin', 'rendah', 'netral', 'besar'], 'buruk'),
        (['dingin', 'rendah', 'basa', 'kecil'], 'sangat buruk'),
        (['dingin', 'rendah', 'basa', 'menengah'], 'sangat buruk'),
        (['dingin', 'rendah', 'basa', 'besar'], 'sangat buruk'),

        (['dingin', 'sedang', 'asam', 'kecil'], 'buruk'),
        (['dingin', 'sedang', 'asam', 'menengah'], 'buruk'),
        (['dingin', 'sedang', 'asam', 'besar'], 'buruk'),
        (['dingin', 'sedang', 'netral', 'kecil'], 'cukup'),
        (['dingin', 'sedang', 'netral', 'menengah'], 'cukup'),
        (['dingin', 'sedang', 'netral', 'besar'], 'cukup'),
        (['dingin', 'sedang', 'basa', 'kecil'], 'buruk'),
        (['dingin', 'sedang', 'basa', 'menengah'], 'buruk'),
        (['dingin', 'sedang', 'basa', 'besar'], 'buruk'),

        (['dingin', 'tinggi', 'asam', 'kecil'], 'sangat buruk'),
        (['dingin', 'tinggi', 'asam', 'menengah'], 'buruk'),
        (['dingin', 'tinggi', 'asam', 'besar'], 'buruk'),
        (['dingin', 'tinggi', 'netral', 'kecil'], 'cukup'),
        (['dingin', 'tinggi', 'netral', 'menengah'], 'cukup'),
        (['dingin', 'tinggi', 'netral', 'besar'], 'cukup'),
        (['dingin', 'tinggi', 'basa', 'kecil'], 'buruk'),
        (['dingin', 'tinggi', 'basa', 'menengah'], 'buruk'),
        (['dingin', 'tinggi', 'basa', 'besar'], 'buruk'),

        (['normal', 'rendah', 'asam', 'kecil'], 'buruk'),
        (['normal', 'rendah', 'asam', 'menengah'], 'buruk'),
        (['normal', 'rendah', 'asam', 'besar'], 'buruk'),
        (['normal', 'rendah', 'netral', 'kecil'], 'buruk'),
        (['normal', 'rendah', 'netral', 'menengah'], 'buruk'),
        (['normal', 'rendah', 'netral', 'besar'], 'buruk'),
        (['normal', 'rendah', 'basa', 'kecil'], 'buruk'),
        (['normal', 'rendah', 'basa', 'menengah'], 'buruk'),
        (['normal', 'rendah', 'basa', 'besar'], 'buruk'),

        (['normal', 'sedang', 'asam', 'kecil'], 'cukup'),
        (['normal', 'sedang', 'asam', 'menengah'], 'cukup'),
        (['normal', 'sedang', 'asam', 'besar'], 'cukup'),
        (['normal', 'sedang', 'netral', 'kecil'], 'baik'),
        (['normal', 'sedang', 'netral', 'menengah'], 'baik'),
        (['normal', 'sedang', 'netral', 'besar'], 'baik'),
        (['normal', 'sedang', 'basa', 'kecil'], 'cukup'),
        (['normal', 'sedang', 'basa', 'menengah'], 'cukup'),
        (['normal', 'sedang', 'basa', 'besar'], 'cukup'),

        (['normal', 'tinggi', 'asam', 'kecil'], 'baik'),
        (['normal', 'tinggi', 'asam', 'menengah'], 'baik'),
        (['normal', 'tinggi', 'asam', 'besar'], 'baik'),
        (['normal', 'tinggi', 'netral', 'kecil'], 'sangat baik'),
        (['normal', 'tinggi', 'netral', 'menengah'], 'sangat baik'),
        (['normal', 'tinggi', 'netral', 'besar'], 'sangat baik'),
        (['normal', 'tinggi', 'basa', 'kecil'], 'baik'),
        (['normal', 'tinggi', 'basa', 'menengah'], 'baik'),
        (['normal', 'tinggi', 'basa', 'besar'], 'baik'),

        (['panas', 'rendah', 'asam', 'kecil'], 'sangat buruk'),
        (['panas', 'rendah', 'asam', 'menengah'], 'sangat buruk'),
        (['panas', 'rendah', 'asam', 'besar'], 'sangat buruk'),
        (['panas', 'rendah', 'netral', 'kecil'], 'buruk'),
        (['panas', 'rendah', 'netral', 'menengah'], 'buruk'),
        (['panas', 'rendah', 'netral', 'besar'], 'buruk'),
        (['panas', 'rendah', 'basa', 'kecil'], 'sangat buruk'),
        (['panas', 'rendah', 'basa', 'menengah'], 'sangat buruk'),
        (['panas', 'rendah', 'basa', 'besar'], 'sangat buruk'),

        (['panas', 'sedang', 'asam', 'kecil'], 'buruk'),
        (['panas', 'sedang', 'asam', 'menengah'], 'buruk'),
        (['panas', 'sedang', 'asam', 'besar'], 'buruk'),
        (['panas', 'sedang', 'netral', 'kecil'], 'cukup'),
        (['panas', 'sedang', 'netral', 'menengah'], 'cukup'),
        (['panas', 'sedang', 'netral', 'besar'], 'cukup'),
        (['panas', 'sedang', 'basa', 'kecil'], 'buruk'),
        (['panas', 'sedang', 'basa', 'menengah'], 'buruk'),
        (['panas', 'sedang', 'basa', 'besar'], 'buruk'),

        (['panas', 'tinggi', 'asam', 'kecil'], 'cukup'),
        (['panas', 'tinggi', 'asam', 'menengah'], 'cukup'),
        (['panas', 'tinggi', 'asam', 'besar'], 'cukup'),
        (['panas', 'tinggi', 'netral', 'kecil'], 'baik'),
        (['panas', 'tinggi', 'netral', 'menengah'], 'baik'),
        (['panas', 'tinggi', 'netral', 'besar'], 'baik'),
        (['panas', 'tinggi', 'basa', 'kecil'], 'cukup'),
        (['panas', 'tinggi', 'basa', 'menengah'], 'cukup'),
        (['panas', 'tinggi', 'basa', 'besar'], 'cukup')
    ]

    numerator = 0
    denominator = 0
    
    for kondisi, konsekuen in aturan_sugeno:
        # Hitung derajat keanggotaan untuk setiap aturan
        mu_suhu = fuzz.interp_membership(suhu_var.universe, suhu_var[kondisi[0]].mf, input_suhu)
        mu_oksigen = fuzz.interp_membership(kadar_oksigen_var.universe, kadar_oksigen_var[kondisi[1]].mf, input_oksigen)
        mu_ph = fuzz.interp_membership(ph_var.universe, ph_var[kondisi[2]].mf, input_ph)
        mu_tds = fuzz.interp_membership(tds_var.universe, tds_var[kondisi[3]].mf, input_tds)
        
        # Nilai firing strength (derajat aktivasi aturan)
        firing_strength = np.fmin.reduce([mu_suhu, mu_oksigen, mu_ph, mu_tds])
        
        konsekuen_value = nilai_kualitas_air[konsekuen]
        
        # Weighted sum formula untuk Sugeno
        numerator += firing_strength * konsekuen_value
        denominator += firing_strength

    if denominator == 0:
        hasil = 0  # Jika tidak ada aturan yang aktif, hasilnya 0
    else:
        hasil = numerator / denominator

    label = interpretasi_sugeno(hasil)

    return label, hasil

    print(f"Firing Strength Suhu ({input_suhu}): {mu_suhu}")
    print(f"Firing Strength DO ({input_oksigen}): {mu_oksigen}")
    print(f"Firing Strength pH ({input_ph}): {mu_ph}")
    print(f"Firing Strength TDS ({input_tds}): {mu_tds}")
# # Contoh Input
#input_suhu = 25
#input_oksigen = 7
#input_ph = 7
#input_tds = 5

# # Hitung output Sugeno
# kategori_kualitas = hitung_sugeno(input_suhu, input_oksigen, input_ph, input_tds)

# print(f"Kualitas Air (Sugeno): {kategori_kualitas}")
