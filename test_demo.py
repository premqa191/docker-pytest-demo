import os

def test_addition():
    assert 10 + 20 == 30

def test_docker_upper():
    assert 'docker'.upper() == 'DOCKER'

def test_environment_variable():
    # ????? ??? ????? ???? TEST_ENV ??????? ?????
    current_env = os.environ.get('TEST_ENV', 'local')
    print(f'\nRunning tests against: {current_env}')
    assert current_env in ['staging', 'prod', 'local']
