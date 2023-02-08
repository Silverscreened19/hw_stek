from main import Stack, balanced
import pytest


class TestClass:
    def test_p_b_1(self):
        line = '[([])((([[[]]])))]{()}'
        res = balanced(line)
        assert res == 'balanced'

    def test_p_b_2(self):
        line = '(((([{}]))))'
        res = balanced(line)
        assert res == 'balanced'

    def test_p_b_3(self):
        line = '{{[()]}}'
        res = balanced(line)
        assert res == 'balanced'

    def test_p_nb_1(self):
        line = '}{}'
        res = balanced(line)
        assert res == 'not balanced not equal'

    def test_p_nb_2(self):
        line = '{{[(])]}}'
        res = balanced(line)
        assert res == 'not balanced not equal'

    def test_p_nb_3(self):
        line = '[[{())}]'
        res = balanced(line)
        assert res == 'not balanced not paired'
