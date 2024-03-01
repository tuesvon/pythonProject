#Напишите фикстуру, которая будет создавать временную директорию перед запуском тестов. Когда тесты завершатся,
# эта директория должна быть удалена.

import pytest
import os
import tempfile

@pytest.fixture(scope="function")
def temp_directory():
    temp_dir = tempfile.mkdtemp()
    print("Директория создана", temp_dir)

    yield temp_dir

    os.rmdir(temp_dir)
    print("Временная директория удалена", temp_dir)

def test_temp_directory(temp_directory):
    assert os.path.exists(temp_directory)


