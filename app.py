import os,csv, logging
from rover import Rover

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

class ProcessExecutor:
    
    def execute_rover_instructions(self, input_path:str, output_path:str) -> None:
        """
        Execute all instructions for all rovers in the input file
        """    
        logging.debug(f'Start to process file: {input_path}')    
        
        #check if they entry if a valid file
        if os.path.isfile(input_path):
            
            #load instructions
            instructions = self.load_instructions(input_path)
            
            #process each rover instruction and return a list with the results
            result =  self.process_rovers(instructions)

            logging.debug(f'{len(result)} rovers processed')
            
            #define output full path and save the list of dictionaries to csv
            full_output_path = os.path.join(output_path,'result.csv')
            
            self.save_file(full_output_path, result)

            logging.debug(f'Finished process file: {input_path}')
   
    def process_rovers(self, instructions:list) -> list:
        """
        Read file and load the instructions
        """
        rovers = []
        
        line_number = 1
        
        boundaries = instructions[0].split(' ')
        
        #interate through all rover instructions and apply it to the coordinates
        while line_number < len(instructions):
            
            start_point = instructions[line_number].split(' ')
            
            instruction = instructions[line_number+1].rstrip()
            
            line_number+=2
            
            rover = Rover(int(boundaries[0].rstrip()), int(boundaries[1].rstrip()), 
                int(start_point[0].rstrip()),int(start_point[1].rstrip()), start_point[2].rstrip())
            
            rover.move_to_target(instruction)
            
            rovers.append(rover.to_dict())
        return rovers
    
    def load_instructions(self, full_input_path:str) ->list:
        """
        Read file and load the instructions
        """
        file = open(full_input_path,'r')

        return file.readlines()

    def save_file(self, full_output_path:str, result:list) -> None:
        """
        Save dictonary to csv
        """
        if len(result) > 0:
            #define csv header
            keys = result[0].keys()
            
            #create folder in case it doesn't exist
            os.makedirs(os.path.dirname(full_output_path), exist_ok=True)
            
            #create and write all dictionary content to csv file
            with open(full_output_path, 'w') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(result)
