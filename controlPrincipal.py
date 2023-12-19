import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
from PyQt5 import uic

class mainWindow(QDialog):    
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        self.boton_serie.clicked.connect(self.serie)
        self.boton_paralelo.clicked.connect(self.paralelo)
        self.boton_p2b.clicked.connect(self.p2b)
        self.boton_b2p.clicked.connect(self.b2p)
        self.boton_adm.clicked.connect(self.admitancia)
        self.boton_fpi.clicked.connect(self.fpi)
        self.boton_2x2.clicked.connect(self.determinante_2x2)
        self.boton_3x3.clicked.connect(self.determinante_3x3)

    def serie(self):
        try:
            z1 = complex(self.z1_serie.text())
            z2 = complex(self.z2_serie.text())
            Zeq = z1+z2
            self.resultado_serie.setText(f'{Zeq: .2f}'[1:])
        except Exception as e:
            self.label_advertencia.setText(f'Hubo un problema: {e}')

    def paralelo(self):
        try:
            z1 = complex(self.z1_paralelo.text())
            z2 = complex(self.z2_paralelo.text())
            Y1 = 1/z1
            Y2 = 1/z2
            Yeq = Y1+Y2
            Zeq = 1/Yeq
            self.resultado_paralelo.setText(f'{Zeq: .2f}'[1:])
        except Exception as e:
            self.label_advertencia.setText(f'Hubo un problema: {e}')

    def p2b(self):
        try:
            real = float(str(float(self.modulo_p2b.text())*np.cos(float(self.fase_p2b.text())*np.pi/180))[0:6])
            real = float(f'{real: .2f}')
            imag = float(str(float(self.modulo_p2b.text())*np.sin(float(self.fase_p2b.text())*np.pi/180))[0:6])
            imag = float(f'{imag: .2f}')
            z = complex(real, imag)
            self.resultado_p2b.setText(str(z)[1:-1]) #quita parentesis
        except Exception as e:
            self.label_advertencia.setText(f'Hubo un problema: {e}')

    def b2p(self):
        try:
            z1 = complex(self.z1_b2p.text())
            modulo = ((z1.real**2)+(z1.imag**2))**(1/2)
            fase = np.arctan(z1.imag/z1.real)*180/np.pi
            self.resultado_b2p.setText(f'{modulo: .2f} ang {fase: .2f}')
        except Exception as e:
            self.label_advertencia.setText(f'Hubo un problema: {e}')

    def admitancia(self):
        try:
            z1 = complex(self.z1_adm.text())
            y1 = 1/z1
            self.resultado_adm.setText(f'{y1: .2f}j'[1:-1])
        except Exception as e:
            self.label_advertencia.setText(f'Hubo un problema: {e}')

    def fpi(self):
        try:
            P = float(self.line_fpi1.text())
            fp = float(self.line_fpi2.text())
            Q = float(self.line_fpi3.text())
            V = float(self.line_fpi4.text())
            f = float(self.line_fpi5.text())
            factor_potencia = P/((P**2+Q**2)**(1/2))
            angulo_radianes = np.arccos(factor_potencia)
            angulo = angulo_radianes*180/np.pi
            reactancia_deseada = P*np.tan(angulo_radianes)
            correccion = Q-reactancia_deseada #potencia a restar
            reactancia_correccion = (V**2)/correccion
            capacitancia = 1/(2*np.pi*f*reactancia_correccion)

            self.label_fpi1.setText(f'factor potencia {factor_potencia: .2f}')
            self.label_fpi2.setText(f'angulo para la correccion {angulo: .2f}')
            self.label_fpi3.setText(f'reactancia tolerada en el circuito {reactancia_deseada: .2f}')
            self.label_fpi4.setText(f'potencia reactiva para la correccion (a contrarrestar) {correccion: .2f}')
            self.label_fpi5.setText(f'reactancia para la correccion {reactancia_correccion: .2f}')
            self.label_fpi6.setText(f'capacitancia para la correccion {capacitancia: .2f}')
        except Exception as e:
            self.label_advertencia.setText(f'Hubo un problema: {e}')

    def determinante_2x2(self):
        try:
            a11 = complex(self.a11.text())
            a12 = complex(self.a12.text())
            a21 = complex(self.a21.text())
            a22 = complex(self.a22.text())
            matriz = np.array([[a11, a12], [a21, a22]])
            ar1 = complex(self.ar1.text())
            ar2 = complex(self.ar2.text())
            resultado = np.array([ar1, ar2])
            solucion = np.linalg.solve(matriz, resultado)
            self.resultado_2x2a.setText(f'{solucion[0]: .2f}'[1:])
            self.resultado_2x2b.setText(f'{solucion[1]: .2f}'[1:])
        except Exception as e:
            self.label_advertencia.setText(f'Hubo un problema: {e}')

    def determinante_3x3(self):
        try:
            b11 = complex(self.b11.text())
            b12 = complex(self.b12.text())
            b13 = complex(self.b13.text())
            b21 = complex(self.b21.text())
            b22 = complex(self.b22.text())
            b23 = complex(self.b23.text())
            b31 = complex(self.b31.text())
            b32 = complex(self.b32.text())
            b33 = complex(self.b33.text())
            matriz = np.array([[b11, b12, b13], [b21, b22, b23], [b31, b32, b33]])
            br1 = complex(self.br1.text())
            br2 = complex(self.br2.text())
            br3 = complex(self.br3.text())
            resultado = np.array([br1, br2, br3])
            solucion = np.linalg.solve(matriz, resultado)
            self.resultado_3x3a.setText(f'{solucion[0]: .2f}'[1:])
            self.resultado_3x3b.setText(f'{solucion[1]: .2f}'[1:])
            self.resultado_3x3c.setText(f'{solucion[2]: .2f}'[1:])
        except Exception as e:
            self.label_advertencia.setText(f'Hubo un problema: {e}')

App = QApplication(sys.argv)
Root = mainWindow()
Root.show()
App.exec_()