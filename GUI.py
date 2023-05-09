import sys
import os
import re
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QInputDialog, QMessageBox, QProgressDialog
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt

dir_path = os.path.dirname(os.path.realpath(__file__))


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Dynamism.Life')
        self.setStyleSheet("background-color: #353535;")
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap(os.path.join(dir_path, 'pics/Dynamism.LifeResized.png'))
        pixmap = pixmap.scaledToWidth(280)
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.width(), pixmap.height())
        label.move(55, 0)

        label = QLabel('Welcome!', self)
        label.move(150, 220)
        label.setFont(QFont('Helvetica', 17))  # set font for label
        label.setStyleSheet('color: white; font-weight: bold;')

        label = QLabel('Select one:', self)
        label.move(60, 270)
        label.setFont(QFont('Helvetica', 12))  # set font for label
        label.setStyleSheet('color: white; font-weight: bold;')

        button = QPushButton('Sender', self)
        button.move(50, 300)
        button.setStyleSheet("background-color: #e8e8e8; border: 2px solid white;")
        pixmap = QPixmap(os.path.join(dir_path, 'pics/sending.png'))
        button.setIcon(QIcon(pixmap))
        button.setIconSize(QSize(20, 20))
        button.clicked.connect(self.Sender_application)

        button = QPushButton('Receiver', self)
        button.move(240, 300)
        button.setStyleSheet("background-color: #e8e8e8; border: 2px solid white;")
        pixmap = QPixmap(os.path.join(dir_path, 'pics/receive.png'))
        button.setIcon(QIcon(pixmap))
        button.setIconSize(QSize(20, 20))
        button.clicked.connect(self.Receiver_application)

        button = QPushButton('Reset', self)
        button.move(10, 5)
        button.setStyleSheet("background-color: #e8e8e8; border: 2px solid white;")
        pixmap = QPixmap(os.path.join(dir_path, 'pics/Exclamation_mark.png'))
        button.setIcon(QIcon(pixmap))
        button.setIconSize(QSize(25, 25))
        # Set the fixed size of the button
        button.setFixedSize(70, 30)
        button.clicked.connect(self.Reset)

    def Sender_application(self):
        # Execute the ifconfig command and get its output
        output = subprocess.check_output(["ifconfig"])

        # Use regular expressions to extract the IPv4 address of the first non-loopback interface
        ipv4_regex = re.compile(r"inet (\d+\.\d+\.\d+\.\d+) ")
        match = ipv4_regex.search(str(output, "utf-8"))
        if match:
            ip = match.group(1)
            msg_box = QMessageBox()
            msg_box.information(self, 'Current IP Address',
                                f'<span style="color:white">The current IP address is: 192.168.1.196</span>')
            msg_box.setStyleSheet("QLabel{min-width: 300px;}")
        else:
            msg_box = QMessageBox()
            msg_box.information(self, 'Current IP Address',
                                f'<span style="color:white">Could not find IP Address</span>')
            msg_box.setStyleSheet("QLabel{min-width: 300px;}")

        # Get IP address input from user
        ip_addr, ok = QInputDialog.getText(None, 'Enter IP address', 'IP address:')
        if not ok:
            return

        # Set up progress dialog
        progress = QProgressDialog('<span style="color:white">Running scripts...</span>', 'Cancel', 0, 0, self)
        progress.setWindowTitle('Please wait')
        progress.setWindowModality(Qt.WindowModal)
        progress.setMinimumDuration(0)
        progress.show()
        app.processEvents()

        try:
            output = subprocess.check_output(['ping', '-c', '3', ip_addr], timeout=4)
            ping_success = '0% packet loss' in output.decode()
        except subprocess.TimeoutExpired:
            ping_success = False

        # ping_progress.close()

        if not ping_success:
            progress.close()
            QMessageBox.critical(self, 'Error',
                                 f'<span style="color:white">Unable to connect to IP address: {ip_addr}</span>',
                                 QMessageBox.Ok)
            return

        # Run long operation
        try:
            # Rest of the method
            os.system('echo "Y" | sudo apt-get install nfs-kernel-server nfs-common')
            os.system("sudo systemctl restart nfs-kernel-server")
            os.system("sudo mkdir /swap_share")
            os.system("sudo chmod 777 /swap_share")
            os.system(f'sudo sh -c "echo \'/swap_share {ip_addr}(rw,sync,no_subtree_check)\' >> /etc/exports"')
            os.system("sudo systemctl restart nfs-kernel-server")
            os.system("sudo fallocate -l 4G /swapfile_network")
            os.system("sudo chmod 600 /swapfile_network")
            os.system("sudo mkswap /swapfile_network")
            os.system("sudo mv /swapfile_network /swap_share/")
            os.system("sudo chmod 777 /swap_share/swapfile_network")
            # sys.exit()

            # Close progress dialog and show completion message
            progress.close()
            msg_box = QMessageBox()
            msg_box.setText('The operation completed successfully.')
            msg_box.setWindowTitle('Operation completed')
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.finished.connect(progress.close)
            msg_box.exec_()

        except Exception as e:
            # Close progress dialog and show error message
            progress.close()
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok)

    def Receiver_application(self):
        # Execute the ifconfig command and get its output
        output = subprocess.check_output(["ifconfig"])

        # Use regular expressions to extract the IPv4 address of the first non-loopback interface
        ipv4_regex = re.compile(r"inet (\d+\.\d+\.\d+\.\d+) ")
        match = ipv4_regex.search(str(output, "utf-8"))
        if match:
            ip = match.group(1)
            msg_box = QMessageBox()
            msg_box.information(self, 'Current IP Address',
                                f'<span style="color:white">The current IP address is: 192.168.1.196</span>')
            msg_box.setStyleSheet("QLabel{min-width: 300px;}")
        else:
            msg_box = QMessageBox()
            msg_box.information(self, 'Current IP Address',
                                f'<span style="color:white">Could not find IP Address</span>')
            msg_box.setStyleSheet("QLabel{min-width: 300px;}")

        # Get IP address input from user
        ip_addr, ok = QInputDialog.getText(None, 'Enter IP address', 'IP address:')
        if not ok:
            return

        # Set up progress dialog
        progress = QProgressDialog('<span style="color:white">Running scripts...</span>', 'Cancel', 0, 0, self)
        progress.setWindowTitle('Please wait')
        progress.setWindowModality(Qt.WindowModal)
        progress.setMinimumDuration(0)
        progress.show()
        app.processEvents()

        try:
            output = subprocess.check_output(['ping', '-c', '3', ip_addr], timeout=4)
            ping_success = '0% packet loss' in output.decode()
        except subprocess.TimeoutExpired:
            ping_success = False

        # ping_progress.close()

        if not ping_success:
            progress.close()
            QMessageBox.critical(self, 'Error',
                                 f'<span style="color:white">Unable to connect to IP address: {ip_addr}</span>',
                                 QMessageBox.Ok)
            return

        # Run long operation
        try:
            os.system('echo "Y" | sudo apt-get install nfs-kernel-server nfs-common')
            os.system("sudo systemctl restart nfs-kernel-server")
            os.system("sudo mkdir /swap_mount")
            os.system("sudo chmod 777 /swap_mount")
            os.system(f'sudo mount {ip_addr}:/swap_share /swap_mount')
            os.system("sudo swapon /swap_mount/swapfile_network")
            # sys.exit()

            # Close progress dialog and show completion message
            progress.close()
            msg_box = QMessageBox()
            msg_box.setText('The operation completed successfully.')
            msg_box.setWindowTitle('Operation completed')
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.finished.connect(progress.close)
            msg_box.exec_()


        except Exception as e:

            # Close progress dialog and show error message

            progress.close()

            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok)

    def Reset(self):
        msg = QMessageBox()
        msg.setWindowTitle("Reset Options")
        msg.setText("Which option do you want to reset?")
        msg.addButton("Sender", QMessageBox.AcceptRole)
        msg.addButton("Receiver", QMessageBox.RejectRole)

        # Show the prompt window and get the selected option
        option = msg.exec_()

        # Handle the selected option
        if option == QMessageBox.AcceptRole:
            # Reset Sender
            os.system("sudo swapoff -a")
            os.system("sudo truncate --size 0 /swap_share/swapfile_network")
            os.system("sudo chmod 0600 /swap_share/swapfile_network")
            os.system("sudo rm /swap_share/swapfile_network")
            os.system("sudo rmdir /swap_share")
            os.system("sudo sed -i '$d' /etc/exports")
            # sys.exit()


        elif option == QMessageBox.RejectRole:
            # Reset Receiver
            os.system("sudo swapoff -a")
            os.system("sudo systemctl stop nfs-kernel-server")
            os.system("sudo umount /swap_mount")
            os.system("sudo rmdir /swap_mount")
            # sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MyWindow()

    window.show()
    sys.exit(app.exec_())
