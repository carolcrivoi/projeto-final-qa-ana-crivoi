class CalculadoraSimples:
    def somar(self, a, b):
        """Soma dois números"""
        return a + b
    
    def subtrair(self, a, b):
        """Subtrai o segundo número do primeiro"""
        return a - b
    
    def multiplicar(self, a, b):
        """Multiplica dois números"""
        return a * b
    
    def dividir(self, a, b):
        """Divide o primeiro número pelo segundo"""
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

import unittest
from unittest.mock import patch
import io

class TesteAceitacaoCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = CalculadoraSimples()
    
    def test_fluxo_completo_usuario(self):
        """Testa um fluxo completo de uso como um usuário faria"""
        # 1. Cálculos básicos
        self.assertEqual(self.calc.somar(5, 3), 8)       # Usuário somando valores
        self.assertEqual(self.calc.subtrair(10, 4), 6)   # Usuário subtraindo
        self.assertEqual(self.calc.multiplicar(2, 6), 12) # Usuário multiplicando
        self.assertEqual(self.calc.dividir(9, 3), 3)      # Usuário dividindo
        
        # 2. Verificação de tratamento de erro
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)  # Usuário tentando dividir por zero
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_interface_simulada(self, mock_stdout):
        """Simula como um usuário interagiria via linha de comando"""
        # Simulando entradas de usuário
        def mock_input(prompt):
            if "primeiro número" in prompt:
                return "8"
            elif "segundo número" in prompt:
                return "2"
            elif "operação" in prompt:
                return "4"  # Divisão
        
        with patch('builtins.input', mock_input):
            # Simulando um mini-programa que usaria a calculadora
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            op = int(input("Escolha a operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))
            
            if op == 1:
                resultado = self.calc.somar(a, b)
            elif op == 2:
                resultado = self.calc.subtrair(a, b)
            elif op == 3:
                resultado = self.calc.multiplicar(a, b)
            elif op == 4:
                resultado = self.calc.dividir(a, b)
            
            print(f"Resultado: {resultado}")
        
        # Verifica se a saída está correta
        self.assertIn("Resultado: 4.0", mock_stdout.getvalue())

# Execução no Google Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
