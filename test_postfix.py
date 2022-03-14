from postfix import postfix_evaluation

def test_postfix_number():
    ret = postfix_evaluation("12345+-*/")
    assert ret == 12

def test_postfix_alphabet():
    ret = postfix_evaluation("qwerty")
    assert ret == None
