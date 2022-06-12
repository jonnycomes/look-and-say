from look_and_say import *

### Tests for standard decimal Chemistry ##########

decimal = LookAndSay()
decimal_chem = Chemistry(decimal)
decimal_chem.generate_elements('9')

def test_generating_elements_92_plus_2():
    '''Testing the seed '9' generates the right number of elements'''
    assert len(decimal_chem.get_elements()) == 94

def test_generating_transuranic_elements():
    '''Testing that both the strings Pu and Np are generated'''
    element_strings = [e.get_string() for e in decimal_chem.get_elements()]
    Pu = '312211322212221121123222119'
    Np = '13112221133211322112211213322119'
    assert Pu in element_strings and Np in element_strings

def test_order_elements_by_string_length():
    '''Testing the order_elements method by the string length'''
    decimal_chem.order_elements('string length')
    elements = decimal_chem.get_elements()
    assert elements[0].get_string() == '3'
    assert len(elements[-1].get_string()) == 42

def test_order_elements_by_string():
    '''Testing the order_elements method by the string'''
    decimal_chem.order_elements('string', reverse=True)
    elements = decimal_chem.get_elements()
    assert elements[0].get_name() == 'Co'
    assert elements[-1].get_name() == 'K'

def test_order_elements_by_name():
    '''Testing the order_elements method by the name'''
    decimal_chem.order_elements('name')
    elements = decimal_chem.get_elements()
    assert elements[0].get_name() == 'Ac'
    assert elements[-1].get_name() == 'Zr'

def test_order_elements_by_abundance():
    '''Testing the order_elements method by the abundance'''
    decimal_chem.order_elements('abundance')
    elements = decimal_chem.get_elements()
    assert elements[0].get_name() == 'H'
    assert elements[-3].get_name() == 'As'
    assert {e.get_name() for e in elements[-2:]} == {'Pu9', 'Np9'}

def test_clear_elements():
    '''Testing the clear_elements method'''
    decimal_chem.clear_elements()
    assert len(decimal_chem.get_elements()) == 0

#### Tests for negafibnary Chemistry ############

def negafibnary_say(num):
    assert num < 9
    say = {1:'1', 2:'100', 3:'101', 4:'10010', 5:'10000', 6:'10001', 7:'10100', 8:'10101'}
    return say[num]

negafibnary = LookAndSay(negafibnary_say)
negafibnary_chem = BinaryChemistry(negafibnary)
negafibnary_chem.generate_elements('0')

def test_generating_negafibnary_elements():
    '''Testing the negafibnary look and say sequence with seed '0' has the correct elements'''
    assert set(['10', '1110']) == {e.get_string() for e in negafibnary_chem.get_elements()}

def test_negafibnary_periodic_table():
    '''Testing the periodic table for the negafibnary Chemistry'''
    negafibnary_chem.order_elements('abundance')
    nf_pt = negafibnary_chem.get_periodic_table(dec_places=1, abundance_sum = 100)
    print(nf_pt)
    E1, E2 = negafibnary_chem.get_elements()
    assert nf_pt['E1']['string'] == '1110'
    assert nf_pt['E1']['abundance'] == 61.8
    assert nf_pt['E1']['decay'] == [E2, E1]
    assert nf_pt['E2']['string'] == '10'
    assert nf_pt['E2']['abundance'] == 38.2
    assert nf_pt['E2']['decay'] == [E1]

def test_negafibnary_get_decay_matrix():
    '''Testing the decay matrix for the negafibnary Chemistry'''
    negafibnary_chem.order_elements('abundance')
    assert negafibnary_chem.get_decay_matrix() == [[1,1],[1,0]]

def test_negafibnary_max_eigenvalue():
    '''Testing the max eigenvalue for the negafibnary Chemistry'''
    assert round(negafibnary_chem.get_max_eigenvalue(), 3) == 1.618

def test_negafibnary_char_poly():
    '''Testing the characteristic polynomial for the negafibnary Chemistry'''
    assert sympy.poly(negafibnary_chem.get_char_poly()).all_coeffs() == [1, -1, -1]
   
