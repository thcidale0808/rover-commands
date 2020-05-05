import pytest, os, csv
from fixtures.instructions import *
from app import ProcessExecutor

def test_instruction_for_one_rover(document_with_one_rover):
    executor = ProcessExecutor()

    executor.execute_rover_instructions(document_with_one_rover, os.path.splitext(document_with_one_rover)[0])
    
    output_path = os.path.join(os.path.splitext(document_with_one_rover)[0],'result.csv')
    
    output_file = csv.DictReader(open(output_path))
    
    for row in output_file:
        assert row['x'] == '1'
        assert row['y'] == '3'
        assert row['direction'] == 'N'

def test_instruction_for_two_rovers(document_with_two_rovers):
    executor = ProcessExecutor()

    executor.execute_rover_instructions(document_with_two_rovers, os.path.splitext(document_with_two_rovers)[0])
    
    output_path = os.path.join(os.path.splitext(document_with_two_rovers)[0],'result.csv')
    
    output_file = csv.DictReader(open(output_path))
    
    for index, row in enumerate(output_file):
        if index == 0:
            assert row['x'] == '1'
            assert row['y'] == '3'
            assert row['direction'] == 'N'
        elif index ==1:
            assert row['x'] == '5'
            assert row['y'] == '1'
            assert row['direction'] == 'E'

def test_invalid_instructions_for_one_rover(document_with_one_rover_invalid_instructions):
    with pytest.raises(Exception) as excinfo:
        executor = ProcessExecutor()

        executor.execute_rover_instructions(document_with_one_rover_invalid_instructions, os.path.splitext(document_with_one_rover_invalid_instructions)[0])

    assert 'Invalid instructions for rover' in str(excinfo.value)