import Libreriascomplex as lc
import unittest

class TestSCplxOperations(unittest.TestCase):

    def test_sumacplx(self):
        self.assertEqual(lc.sumacplx((3,5),(-2.6,6.8)),(0.3999999999999999,11.8))
    def test_sumacplx(self):
        self.assertEqual(lc.sumacplx((2,-8),(-6,1)),(-4,-7))


    def test_producto(self):
        self.assertEqual(lc.producto((3,5),(-2.6,6.8)),(-41.8, 7.399999999999999))
    def test_producto(self):
        self.assertEqual(lc.producto((2,-8),(-6,1)),(-4, 50))

    def test_resta(self):
        self.assertEqual(lc.resta((3,5),(-2.6,6.8)),(5.6, -1.7999999999999998))
    def test_resta(self):
        self.assertEqual(lc.resta((2,-8),(-6,1)),(8, -9))


    def test_division(self):
        self.assertEqual(lc.division((3,5),(-2.6,6.8)),(0.4943396226415095, -0.6301886792452831))
    def test_division(self):
        self.assertEqual(lc.division((2,-8),(-6,1)),(-0.5405405405405406, 1.2432432432432432))

    def test_modulo(self):
        self.assertEqual(lc.modulo((3,5)),5.830951894845301)
    def test_modulo(self):
        self.assertEqual(lc.modulo((-6,1)),6.082762530298219)

    def test_conjugado(self):
        self.assertEqual(lc.conjugado((3,5)),(3,-5))
    def test_conjugado(self):
        self.assertEqual(lc.conjugado((-6,1)),(-6,-1))

    def test_fase(self):
        self.assertEqual(lc.fase((3,5)),(1.0303768265243125))
    def test_fase(self):
        self.assertEqual(lc.fase((-6,1)),(-0.16514867741462683))

if __name__ == '__main__':
    unittest.main()
