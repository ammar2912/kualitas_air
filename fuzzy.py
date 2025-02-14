import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import random
import time



# def hitung_kualitas_air(ph_input, suhu_input):
#     # deklarasi batas batas nilai
#     ph = ctrl.Antecedent(np.arange(0.0, 30.0, 0.1), 'ph')
#     suhu = ctrl.Antecedent(np.arange(0.0, 100.0, 0.1), 'suhu')

#     # deklarasi kualitas air
#     kualitas_air = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'kualitas_air')

#     # membership function ph
#     ph['asam'] = fuzz.trimf(ph.universe, [0.0, 0.0, 6.0])
#     ph['netral'] = fuzz.trimf(ph.universe, [6.0, 7.0, 8.0])
#     ph['basa'] = fuzz.trimf(ph.universe, [8.0, 15.0, 30.0])

#     # membership function suhu
#     suhu['poor1'] = fuzz.trapmf(suhu.universe, [0.0, 10.0, 15.0, 18.0])
#     suhu['optimal'] = fuzz.trapmf(suhu.universe, [18.0, 22.0, 25.0, 28.0])
#     suhu['poor2'] = fuzz.trapmf(suhu.universe, [28.0, 35.0, 40.0, 50.0])

#     # membership function kualitas
#     kualitas_air['bagus'] = fuzz.trimf(kualitas_air.universe, [0, 0, 0.5])
#     kualitas_air['buruk'] = fuzz.trimf(kualitas_air.universe, [0.5, 1, 1])

#    # Definisi aturan fuzzy
#     rules = [
#         ctrl.Rule(ph['asam'] & suhu['poor1'], kualitas_air['buruk']),
#         ctrl.Rule(ph['asam'] & suhu['optimal'], kualitas_air['buruk']),
#         ctrl.Rule(ph['asam'] & suhu['poor2'], kualitas_air['buruk']),
        
#         ctrl.Rule(ph['netral'] & suhu['poor1'], kualitas_air['buruk']),
#         ctrl.Rule(ph['netral'] & suhu['optimal'], kualitas_air['bagus']),
#         ctrl.Rule(ph['netral'] & suhu['poor2'], kualitas_air['buruk']),

#         ctrl.Rule(ph['basa'] & suhu['poor1'], kualitas_air['buruk']),
#         ctrl.Rule(ph['basa'] & suhu['optimal'], kualitas_air['buruk']),
#         ctrl.Rule(ph['basa'] & suhu['poor2'], kualitas_air['buruk']),
       
#        ctrl.Rule(suhu['poor1'] & ph['asam'], kualitas_air['buruk']),
#        ctrl.Rule(suhu['poor1'] & ph['netral'], kualitas_air['buruk']),
#        ctrl.Rule(suhu['poor1'] & ph['basa'], kualitas_air['buruk']),

#        ctrl.Rule(suhu['optimal'] & ph['asam'], kualitas_air['buruk']),
#        ctrl.Rule(suhu['optimal'] & ph['netral'], kualitas_air['bagus']),
#        ctrl.Rule(suhu['optimal'] & ph['basa'], kualitas_air['buruk']),

#        ctrl.Rule(suhu['poor2'] & ph['asam'], kualitas_air['buruk']),
#        ctrl.Rule(suhu['poor2'] & ph['netral'], kualitas_air['buruk']),
#        ctrl.Rule(suhu['poor2'] & ph['basa'], kualitas_air['buruk']),
#     ]

#     kualitas_ctrl = ctrl.ControlSystem(rules)
#     kualitas = ctrl.ControlSystemSimulation(kualitas_ctrl)

#     kualitas.input['ph'] = ph_input
#     kualitas.input['suhu'] = suhu_input

#     try:
#         # Hitung kualitas
#         kualitas.compute()
#         kualitas_nilai = kualitas.output['kualitas_air']

#         # Menampilkan output dan label
#         print(f"Nilai Kualitas Air: {kualitas_nilai:.4f}")
#         print(f"Input pH: {ph_input}")
#         print(f"Input Suhu: {suhu_input}")

#         # Penetapan label berdasarkan nilai kualitas
#         if kualitas_nilai <= 0.5:  # Menggunakan <= untuk memasukkan nilai 0.5 sebagai "Bagus"
#             label = "Bagus"
#         else:
#             label = "Buruk"
#         print(f"Kualitas Air: {label}")

#     except ValueError:
#         # Jika terjadi kesalahan dalam defuzzifikasi, output otomatis jadi "Buruk"
#         print("Error: Tidak ada aturan yang aktif, menetapkan kualitas air menjadi 'Buruk'.")
#         label = "Buruk"

#     return label



    
    
    

def hitung_kualitas_air(ph, suhu):

     # deklarasi batas batas nilai
    ph = ctrl.Antecedent(np.arange(0.0, 30.0, 0.1), 'ph')
    suhu = ctrl.Antecedent(np.arange(0.0, 100.0, 0.1), 'suhu')
    ##membership funtion ph
    # 'asam' should cover the range from acidic pH (0-6)
    ph['asam'] = fuzz.trimf(ph.universe, [0.0, 0.0, 6.0])

    # 'netral' should cover the range around pH 7 (neutral)
    ph['netral'] = fuzz.trimf(ph.universe, [6.0, 7.0, 8.0])

    # 'basa' should cover the range from pH 8 to 15 (alkaline)
    ph['basa'] = fuzz.trimf(ph.universe, [8.0, 15.0, 15.0])


    ph['optimal'] = fuzz.trapmf(ph.universe, [7.0, 7.2, 7.4, 7.6])
    ph['moderate'] = fuzz.trapmf(ph.universe, [6.5, 7.0, 7.6, 8.0])

    ph['poor'] = fuzz.trapmf(ph.universe, [5.5, 6.0, 6.5, 7.0])
    ph['very_poor'] = fuzz.trapmf(ph.universe, [0.0, 0.5, 5.5, 6.0])


    ##deklarasi suhu
    suhu['dingin'] = fuzz.trimf(suhu.universe, [9.0, 20.0, 25.0])
    suhu['normal'] = fuzz.trimf(suhu.universe, [20.0, 25.0, 30.0])
    suhu['panas'] = fuzz.trimf(suhu.universe, [25.0, 30.0, 30.0])

    suhu['optimal'] = fuzz.trapmf(suhu.universe, [22.0, 23.0, 25.0, 26.0])
    suhu['moderate'] = fuzz.trapmf(suhu.universe, [18.0, 22.0, 26.0, 28.0])

    suhu['poor'] = fuzz.trapmf(suhu.universe, [14.0, 18.0, 28.0, 30.0])
    suhu['very_poor'] = fuzz.trapmf(suhu.universe, [0.0, 10.0, 30.0, 40.0])


    #deklarasi do
    # do['rendah'] = fuzz.trimf(do.universe, [3.0, 5.0, 6.0])
    # do['normal'] = fuzz.trimf(do.universe, [5.0, 6.0, 7.0])
    # do['tinggi'] = fuzz.trimf(do.universe, [7.0, 10, 10])

    # do['optimal'] = fuzz.trapmf(do.universe, [6.0, 7.0, 9.0, 10.0])
    # do['moderate'] = fuzz.trapmf(do.universe, [4.0, 5.0, 7.0, 8.0])

    # do['poor'] = fuzz.trapmf(do.universe, [2.0, 3.0, 5.0, 6.0])
    # do['very_poor'] = fuzz.trapmf(do.universe, [0.0, 1.0, 3.0, 4.0])


    # Plotting Grafik untuk PH
    ph.view()

    # Plotting Grafik untuk Suhu
    suhu.view()

    # Plotting Grafik untuk DO
    do.view()

    # Menampilkan semua grafikwh
    plt.show()

    # Deklarasi kualitas air






    random_ph = random.uniform(0, 8) 
    random_suhu = random.uniform(0, 40)
    # random_do = random.uniform(0, 10)


    kualitas = hitung_kualitas_air(random_ph, random_suhu)

    kualitas.input['do'] = random_do

    start_time = time.time()
    end_time = time.time()


    execution_time = end_time - start_time
    print(f"Waktu eksekusi: {execution_time:.5f} detik")





