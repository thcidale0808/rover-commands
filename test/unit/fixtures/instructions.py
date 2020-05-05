import pytest
import os

@pytest.fixture()
def document_with_one_rover(tmpdir):
    
    temp_directory = tmpdir.mkdir("files")
    
    temp_file = temp_directory.join("document.txt")
    
    temp_file.write("5 5\n1 2 N\nLMLMLMLMM")
    
    assert temp_file.read()=="5 5\n1 2 N\nLMLMLMLMM"

    yield os.path.join(temp_file.dirname, temp_file.basename)

@pytest.fixture()
def document_with_two_rovers(tmpdir):
    
    temp_directory = tmpdir.mkdir("files")
    
    temp_file = temp_directory.join("document.txt")
    
    temp_file.write("5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM")
    
    assert temp_file.read()=="5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"

    yield os.path.join(temp_file.dirname, temp_file.basename)

@pytest.fixture()
def document_with_one_rover_invalid_instructions(tmpdir):
    
    temp_directory = tmpdir.mkdir("files")
    
    temp_file = temp_directory.join("document.txt")
    
    temp_file.write("2 2\n1 2 N\nLMLMLMLMM")
    
    assert temp_file.read()=="2 2\n1 2 N\nLMLMLMLMM"

    yield os.path.join(temp_file.dirname, temp_file.basename)