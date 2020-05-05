import click, logging, os
from app import ProcessExecutor

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

@click.command()
@click.option(
    '--input',
    required=True,
    help='Path to the instruction file.'
)
@click.option(
    '--output',
    required=True,
    help='Path to output directory.'
)
def main(input, output):
    """
    CLI for applying coordinate instructions on rovers
    """
    try:
        logging.info("Process started")
        
        #create process executor
        executor = ProcessExecutor()
        
        #generate the report for input and output
        executor.execute_rover_instructions(input, output)

    except Exception as e:
        logging.error(e)
    finally:
        logging.info("Process finished")
    
if __name__ == "__main__":
    main()
