from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi
import sys

class Assignment7(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load file UI
        loadUi('week7.ui', self)

        # Connect tombol Submit dan Hapus
        self.submitButton.clicked.connect(self.submit_tugas)
        self.hapusButton.clicked.connect(self.hapus_tugas)

    def submit_tugas(self):
        # Ambil data dari form
        nama = self.lineEditTugas.text()
        batas = self.dateEditDeadline.date().toString("yyyy-MM-dd")
        kategori = self.comboBoxKategori.currentText()
        prioritas = ""

        if self.radioButtonPenting.isChecked():
            prioritas = "Penting"
        elif self.radioButtonSedang.isChecked():
            prioritas = "Sedang"
        elif self.radioButtonRendah.isChecked():
            prioritas = "Rendah"

        # Cek dulu, jangan sampai nama tugas kosong
        if nama.strip() == "":
            warning_box = QMessageBox(self)
            warning_box.setIcon(QMessageBox.Warning)
            warning_box.setWindowTitle("Peringatan")
            warning_box.setText("Nama tugas tidak boleh kosong!")
            warning_box.setStyleSheet(
                "QLabel { color: white; font-size: 12pt; }"
                "QPushButton { background-color: gray; color: white; }"
            )
            warning_box.exec_()
            return

        # Buat item untuk daftar tugas
        item_text = f"{nama} | {batas} | {kategori} | {prioritas}"
        self.listWidgetTugas.addItem(item_text)

        # Tampilan pop-up sukses
        info_box = QMessageBox(self)
        info_box.setIcon(QMessageBox.Information)
        info_box.setWindowTitle("Sukses")
        info_box.setText("Tugas berhasil ditambahkan!")
        info_box.setStyleSheet(
            "QLabel { color: white; font-size: 12pt; }"
            "QPushButton { background-color: gray; color: white; }"
        )
        info_box.exec_()

        # Reset form setelah submit
        self.lineEditTugas.clear()
        self.dateEditDeadline.setDate(QDate.currentDate())
        self.comboBoxKategori.setCurrentIndex(0)
        self.radioButtonPenting.setAutoExclusive(False)
        self.radioButtonPenting.setChecked(False)
        self.radioButtonSedang.setChecked(False)
        self.radioButtonRendah.setChecked(False)
        self.radioButtonPenting.setAutoExclusive(True)

    def hapus_tugas(self):
        selected_items = self.listWidgetTugas.selectedItems()
        if not selected_items:
            warning_box = QMessageBox(self)
            warning_box.setIcon(QMessageBox.Warning)
            warning_box.setWindowTitle("Peringatan")
            warning_box.setText("Pilih tugas yang ingin dihapus!")
            warning_box.setStyleSheet(
                "QLabel { color: white; font-size: 12pt; }"
                "QPushButton { background-color: gray; color: white; }"
            )
            warning_box.exec_()
            return

        for item in selected_items:
            self.listWidgetTugas.takeItem(self.listWidgetTugas.row(item))

        # Tampilan pop-up sukses setelah hapus
        success_box = QMessageBox(self)
        success_box.setIcon(QMessageBox.Information)
        success_box.setWindowTitle("Sukses")
        success_box.setText("Tugas berhasil dihapus!")
        success_box.setStyleSheet(
            "QLabel { color: white; font-size: 12pt; }"
            "QPushButton { background-color: gray; color: white; }"
        )
        success_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Assignment7()
    window.show()
    sys.exit(app.exec_())
