from ie_nlp_utils import tokenize  # This will fail right away!

def test_tokenize_returns_expected_list():
    sentence = "This is a sentence"
    expected_tokens = ["This", "is", "a", "sentence"]

    tokens = tokenize(sentence)

    assert tokens == expected_tokens
