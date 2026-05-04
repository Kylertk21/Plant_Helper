from planteye import create_app

# Test setup
def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
