from PyQt5 import QtWidgets, QtCore,QtGui
import PyQt5
import pyshark
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tkinter
from matplotlib import cm
from ui_packetdetails import Ui_MainWindow

class PacketDetailsWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):

    unique_ports=None
    unique_ports_count = None
    packets_ports=None
    packets_count=None


    def __init__(self):
        super().__init__();
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setFixedSize(self.size())
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.horizontalHeader().setStretchLastSection(True);

        self.barchart.clicked.connect(self.barchartButtonpressed)
        self.piechart.clicked.connect(self.piechartButtonpressed)

        global unique_ports
        global unique_ports_count
        global packets_ports
        global packet_count
        packet_count = 0
        unique_ports = []
        unique_ports_count = []
        packets_ports = []
        file = open("ports.lists.json")
        ports_list = json.load(file)
        print("Button pressed")


        f = open("test.pcap", "rb")
        cap = pyshark.FileCapture(f)

        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem("Source IP"))
        self.table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem("DestinationIP"))
        self.table.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem("Sorce Port"))
        self.table.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem("Destination Port"))
        self.table.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem("Protocol"))

        self.table.item(rowPosition, 0).setBackground(QtGui.QColor("blue"))
        self.table.item(rowPosition, 1).setBackground(QtGui.QColor("blue"))
        self.table.item(rowPosition, 2).setBackground(QtGui.QColor("blue"))
        self.table.item(rowPosition, 3).setBackground(QtGui.QColor("blue"))
        self.table.item(rowPosition, 4).setBackground(QtGui.QColor("blue"))


        for pkt in cap:

            if pkt.transport_layer and 'ip' in pkt:
                src_port = pkt[pkt.transport_layer].srcport
                dst_port = pkt[pkt.transport_layer].dstport
                rowPosition=self.table.rowCount()
                self.table.insertRow(rowPosition)
                self.table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(pkt.ip.src)))
                self.table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(pkt.ip.dst)))
                self.table.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(src_port)))
                self.table.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(dst_port)))

                if src_port in ports_list and "Official" in ports_list[src_port][0]["status"]:
                    packets_ports.append(ports_list[src_port][0]["description"])
                    self.table.setItem(rowPosition, 4,QtWidgets.QTableWidgetItem("%s" %ports_list[src_port][0]["description"]))
                    self.table.item(rowPosition, 2).setBackground(QtGui.QColor("lightgreen"))
                    # print (ports_list[src_port][0]["description"])
                    if unique_ports.count(ports_list[src_port][0]["description"]) == 0:
                        unique_ports.append(ports_list[src_port][0]["description"])
                elif dst_port in ports_list and "Official" in ports_list[dst_port][0]["status"]:
                    packets_ports.append(ports_list[dst_port][0]["description"])
                    self.table.setItem(rowPosition, 4,QtWidgets.QTableWidgetItem("%s" %ports_list[dst_port][0]["description"]))
                    self.table.item(rowPosition, 3).setBackground(QtGui.QColor("lightgreen"))
                    #  print (ports_list[dst_port][0]["description"])
                    if unique_ports.count(ports_list[dst_port][0]["description"]) == 0:
                        unique_ports.append(ports_list[dst_port][0]["description"])
                else:
                    packets_ports.append("Unclassified")
                    if unique_ports.count("Unclassified") == 0:
                        unique_ports.append("Unclassified")
                        self.table.setItem(rowPosition, 4,QtWidgets.QTableWidgetItem("Unclassified"))
                        self.packetTable.item(rowPosition, 4).setBackground(QtGui.QColor("red"))
                        #   print ("Unclassified")


            packet_count += 1

        for type in unique_ports:
            unique_ports_count.append(packets_ports.count(type))

        print("test")
        print(packet_count)

        for i in range(len(unique_ports)):
            print("Protocol: "),
            print(unique_ports[i]),
            print(" | Packets: "),
            print(unique_ports_count[i]),

        self.table.resizeColumnsToContents()
        self.totalpackets.setText(str(packet_count))
        self.show()





    def barchartButtonpressed(self):

        x_axis = np.arange(len(unique_ports))
        cmap = plt.get_cmap('viridis')
        colors = cmap(np.linspace(0, 1, len(unique_ports)))
        patches = plt.bar(x_axis, unique_ports_count, align='center', alpha=0.5, color=colors)
        plt.legend(patches, unique_ports, loc="best", )
        # plt.xticks(y_axis, labels)
        for a, b in zip(x_axis, unique_ports_count):
            plt.text(a, b, str(b))

        plt.tight_layout()
        plt.show()

    def piechartButtonpressed(self):
        global unique_ports
        global unique_ports_count

        cmap = plt.get_cmap('viridis')
        colors = cmap(np.linspace(0, 1, len(unique_ports)))
        patches, texts = plt.pie(unique_ports_count, colors=colors, startangle=90)
        plt.legend(patches, unique_ports, loc="best", )
        plt.axis('equal')
        plt.tight_layout()
        plt.show()