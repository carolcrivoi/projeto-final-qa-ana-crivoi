class CalculadoraSimples:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

import unittest

class TestRegressaoCalculadora(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Executado uma vez antes de todos os testes"""
        cls.calc = CalculadoraSimples()
        # Dados históricos de resultados esperados
        cls.resultados_historicos = {
            'soma': [
                {'input': (2, 3), 'output': 5},
                {'input': (-1, 1), 'output': 0},
                {'input': (0, 0), 'output': 0}
            ],
            'subtracao': [
                {'input': (5, 3), 'output': 2},
                {'input': (10, 10), 'output': 0},
                {'input': (0, 5), 'output': -5}
            ],
            'multiplicacao': [
                {'input': (3, 4), 'output': 12},
                {'input': (-2, 5), 'output': -10},
                {'input': (0, 100), 'output': 0}
            ],
            'divisao': [
                {'input': (10, 2), 'output': 5},
                {'input': (1, 3), 'output': 1/3},
                {'input': (0, 1), 'output': 0}
            ],
            'divisao_por_zero': [
                {'input': (10, 0), 'output': ValueError}
            ]
        }
    
    def test_regressao_soma(self):
        """Verifica se os resultados de soma continuam consistentes"""
        for caso in self.resultados_historicos['soma']:
            with self.subTest(caso=caso):
                self.assertEqual(
                    self.calc.somar(*caso['input']),
                    caso['output']
                )
    
    def test_regressao_subtracao(self):
        """Verifica se os resultados de subtração continuam consistentes"""
        for caso in self.resultados_historicos['subtracao']:
            with self.subTest(caso=caso):
                self.assertEqual(
                    self.calc.subtrair(*caso['input']),
                    caso['output']
                )
    
    def test_regressao_multiplicacao(self):
        """Verifica se os resultados de multiplicação continuam consistentes"""
        for caso in self.resultados_historicos['multiplicacao']:
            with self.subTest(caso=caso):
                self.assertEqual(
                    self.calc.multiplicar(*caso['input']),
                    caso['output']
                )
    
    def test_regressao_divisao(self):
        """Verifica se os resultados de divisão continuam consistentes"""
        for caso in self.resultados_historicos['divisao']:
            with self.subTest(caso=caso):
                self.assertAlmostEqual(
                    self.calc.dividir(*caso['input']),
                    caso['output']
                )
    
    def test_regressao_divisao_por_zero(self):
        """Verifica se a divisão por zero ainda levanta exceção"""
        for caso in self.resultados_historicos['divisao_por_zero']:
            with self.subTest(caso=caso):
                with self.assertRaises(caso['output']):
                    self.calc.dividir(*caso['input'])

# Execução no Google Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
