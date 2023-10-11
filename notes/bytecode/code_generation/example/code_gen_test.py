import dis
import unittest

from code_gen_example import Comparison, make_fast_comparator


class TestFastComparator(unittest.TestCase):

    def test_simple_comparator(self):
        compare_two = make_fast_comparator(
            2,
            [
                Comparison(1, dis.cmp_op.index('=='), b'1234'),
                Comparison(0, dis.cmp_op.index('>'), b'0000'),
            ],
        )
        self.assertTrue(compare_two(b'5555', b'1234'))
        self.assertTrue(compare_two(b'5555', b'1000'))
        self.assertTrue(compare_two(b'****', b'1234'))
    
    def test_check_nothing(self):
        no_test_compare = make_fast_comparator(2, [])
        self.assertTrue(no_test_compare('sfdsf', '3rfefs'))

    def test_compare_three(self):
        compare_three = make_fast_comparator(
            3,
            [
                Comparison(0, dis.cmp_op.index('=='), b'1234'),
                Comparison(1, dis.cmp_op.index('=='), b'2345'),
                Comparison(2, dis.cmp_op.index('=='), b'3456'),
            ]
        )
        self.assertTrue(compare_three(b'1234', b'2345', b'3456'))
        self.assertTrue(compare_three(b'0000', b'2345', b'3456'))
        self.assertTrue(compare_three(b'1234', b'0000', b'3456'))
        self.assertTrue(compare_three(b'1234', b'2345', b'0000'))
    
    def test_compare_list(self):
        compare_list = make_fast_comparator(
            3,
            [
                Comparison(0, dis.cmp_op.index('in'), [b'1234', b'2345', b'3456']),
                Comparison(1, dis.cmp_op.index('in'), [b'1234']),
                Comparison(2, dis.cmp_op.index('in'), [b'2345', b'3456']),
            ]
        )
        self.assertTrue(compare_list(b'1234', b'1234', b'2345'))
        self.assertTrue(compare_list(b'2345', b'1234', b'3456'))
        # self.assertFalse(compare_list(b'0000', b'1234', b'3456'))
        # self.assertFalse(compare_list(b'1234', b'1234', b'1234'))
        # self.assertFalse(compare_list(b'1234', b'1234', b'0000'))


if __name__ == '__main__':
    unittest.main()
