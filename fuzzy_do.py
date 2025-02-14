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

# Variabel Input
suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kadar_oksigen = ctrl.Antecedent(np.arange(0, 11, 1), 'kadar_oksigen')
ph = ctrl.Antecedent(np.arange(0, 15, 1), 'ph')
tds = ctrl.Antecedent(np.arange(0, 11, 1), 'tds')

# Membership Functions untuk Input
suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 10, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])

kadar_oksigen['rendah'] = fuzz.trimf(kadar_oksigen.universe, [0, 2, 4])
kadar_oksigen['sedang'] = fuzz.trimf(kadar_oksigen.universe, [3, 5, 7])
kadar_oksigen['tinggi'] = fuzz.trimf(kadar_oksigen.universe, [6, 8, 10])

ph['asam'] = fuzz.trimf(ph.universe, [0, 3, 7])
ph['netral'] = fuzz.trimf(ph.universe, [6, 7, 8])
ph['basa'] = fuzz.trimf(ph.universe, [7, 10, 14])

tds['kecil'] = fuzz.trimf(tds.universe, [0, 2, 4])
tds['menengah'] = fuzz.trimf(tds.universe, [3, 5, 7])
tds['besar'] = fuzz.trimf(tds.universe, [6, 8, 10])

# Nilai konsekuen dalam Sugeno (konstanta)
nilai_kualitas_air = {
    'sangat buruk': 10, #1 3 mnt
    'buruk': 30, #1 2 mnt
    'cukup': 50, #1 1 mnt
    'baik': 70, #1 30 dtik
    'sangat baik': 90 #0
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

# Fungsi untuk menghitung output Sugeno manual
def hitung_sugeno(input_suhu, input_oksigen, input_ph, input_tds):
    numerator = 0
    denominator = 0
    
    for kondisi, konsekuen in aturan_sugeno:
        # Hitung derajat keanggotaan untuk setiap aturan
        mu_suhu = fuzz.interp_membership(suhu.universe, suhu[kondisi[0]].mf, input_suhu)
        mu_oksigen = fuzz.interp_membership(kadar_oksigen.universe, kadar_oksigen[kondisi[1]].mf, input_oksigen)
        mu_ph = fuzz.interp_membership(ph.universe, ph[kondisi[2]].mf, input_ph)
        mu_tds = fuzz.interp_membership(tds.universe, tds[kondisi[3]].mf, input_tds)
        
        # Nilai firing strength (derajat aktivasi aturan)
        firing_strength = np.fmin.reduce([mu_suhu, mu_oksigen, mu_ph, mu_tds])
        
        konsekuen_value = nilai_kualitas_air[konsekuen]
        
        # Weighted sum formula untuk Sugeno
        numerator += firing_strength * konsekuen_value
        denominator += firing_strength

    if denominator == 0:
        return 0  # Jika tidak ada aturan yang aktif, hasilnya 0
    return numerator / denominator

# Contoh Input
input_suhu = 25
input_oksigen = 7
input_ph = 7
input_tds = 5

# Hitung output Sugeno
hasil_sugeno = hitung_sugeno(input_suhu, input_oksigen, input_ph, input_tds)
kategori_kualitas = interpretasi_sugeno(hasil_sugeno)

print(f"Kualitas Air (Sugeno): {hasil_sugeno:.2f} → {kategori_kualitas}")
