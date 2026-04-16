import tkinter as tk
from tkinter import messagebox

database_kerusakan = {
    "RAM Rusak": {
        "gejala": ["layar_blank", "bunyi_beep_berulang"],
        "solusi": "Coba lepas RAM dan bersihkan pin emasnya menggunakan penghapus pensil, lalu pasang kembali."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["sering_restart_sendiri", "pc_tidak_mau_nyala"],
        "solusi": "Cek tegangan PSU dengan multitester atau coba ganti dengan PSU cadangan yang normal."
    },
    "Overheat (Prosesor)": {
        "gejala": ["tiba_tiba_mati", "kipas_berisik"],
        "solusi": "Bersihkan debu pada heatsink dan ganti thermal paste pada prosesor."
    },
    "VGA Bermasalah": {
        "gejala": ["layar_bergaris", "warna_layar_aneh"],
        "solusi": "Update driver VGA atau pastikan kabel HDMI/VGA terpasang dengan kuat di slotnya."
    },
    "Hardisk Corrupt": {
        "gejala": ["loading_sangat_lama", "sering_blue_screen"],
        "solusi": "Lakukan pengecekan bad sector atau pertimbangkan untuk migrasi data ke SSD."
    }
}

semua_gejala = [
    ("layar_blank", "Apakah layar monitor blank/tidak tampil?"),
    ("bunyi_beep_berulang", "Apakah terdengar bunyi beep berulang saat menyalakan?"),
    ("sering_restart_sendiri", "Apakah komputer sering restart secara tiba-tiba?"),
    ("pc_tidak_mau_nyala", "Apakah komputer sama sekali tidak mau menyala?"),
    ("tiba_tiba_mati", "Apakah komputer tiba-tiba mati setelah digunakan beberapa lama?"),
    ("kipas_berisik", "Apakah suara kipas terdengar sangat berisik/kencang?"),
    ("layar_bergaris", "Apakah muncul garis-garis aneh pada layar?"),
    ("warna_layar_aneh", "Apakah warna tampilan layar terlihat pecah atau tidak normal?"),
    ("loading_sangat_lama", "Apakah proses loading Windows/aplikasi terasa sangat lambat?"),
    ("sering_blue_screen", "Apakah sering muncul pesan error 'Blue Screen of Death' (BSOD)?")
]

class SistemPakarKomputer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Komputer")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        
        self.label_tanya = tk.Label(root, text="Klik tombol untuk mulai diagnosa", font=("Arial", 11), wraplength=350)
        self.label_tanya.pack(pady=30)
        
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai_diagnosa, width=20)
        self.btn_mulai.pack(pady=10)
        
        self.frame_tombol = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_tombol, text="YA", width=10, command=lambda: self.proses_jawaban('y'))
        self.btn_tidak = tk.Button(self.frame_tombol, text="TIDAK", width=10, command=lambda: self.proses_jawaban('t'))
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_diagnosa(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_tombol.pack(pady=20)
        self.update_pertanyaan()

    def update_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            _, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.jalankan_inferensi()

    def proses_jawaban(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
        self.index_pertanyaan += 1
        self.update_pertanyaan()

    def jalankan_inferensi(self):
        hasil_diagnosa = []
        for nama, data in database_kerusakan.items():
            if all(s in self.gejala_terpilih for s in data["gejala"]):
                hasil_diagnosa.append((nama, data["solusi"]))
        
        if hasil_diagnosa:
            pesan = "Hasil Diagnosa:\n\n"
            for nama, solusi in hasil_diagnosa:
                pesan += f" {nama}\nSolusi: {solusi}\n\n"
        else:
            pesan = "Gejala tidak cocok dengan data kerusakan manapun."
            
        messagebox.showinfo("Selesai", pesan)
        self.frame_tombol.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Siap mendiagnosa lagi?")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    app = SistemPakarKomputer(root)
    root.mainloop()