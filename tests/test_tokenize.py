from ie_nlp_utils import tokenize  # This will fail right away!
import pytest

@pytest.mark.parametrize("input, lower, expected", [
	("This is a sentence.", True, ["this", "is", "a", "sentence."]),
	("This is a sentence.", False, ["This", "is", "a", "sentence."]),
])

def test_tokenize_returns_expected_list(input,lower,expected):
    
    tokens = tokenize(input, lower=lower)

    assert tokens == expected
