"""
File: dirbot_braun.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Hint: See the Textbook, Skill Drills, and GUIDES for code snippets to help complete this module.

Author: Chris Braun

"""

#####################################
# Import Modules at the Top
#####################################

# Import from the Python Standard library
import pathlib
import sys      

# Import packages from requirements.txt
import loguru   

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
import utils_chrisbraun

# Import time for Function 4
import time 

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare global variables
#####################################

# Create a project path object for the root directory of the project.
ROOT_DIR = pathlib.Path.cwd()
YEAR_ROOT = pathlib.Path.cwd() / "years"
NAMED_ROOT = pathlib.Path.cwd() / "names"
PREFIXED_LC_ROOT = pathlib.Path.cwd() / "prefixes"
TIMED_ROOT = pathlib.Path.cwd() / "timed"
STANDARD_ROOT = pathlib.Path.cwd() / "standardized"

REGIONS = [
    "North America", 
    "South America", 
    "Europe", 
    "Asia", 
    "Africa", 
    "Oceania", 
    "Middle East"
]

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.

    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''

    # Log function name and parameters
    logger.info("FUNCTION: create_folders_for_range()")
    logger.info(f"PARAMETERS: start_year = {start_year}, end_year = {end_year}")

    YEAR_ROOT.mkdir(exist_ok=True)
 
    for year in range(start_year, end_year +1):
        year_path = YEAR_ROOT / str(year)
        year_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {year_path}")

  
#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################

def create_folders_from_list(folder_list: list, force_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders based on a list of folder names.
    
    Arguments:
    folder_list -- A list of strings representing folder names.
    '''

    logger.info("FUNCTION: create_folders_from_list()")
    logger.info(f"PARAMETER: folder_list = {folder_list}")
    logger.info(f"PARAMETER: force_lowercase = {force_lowercase}")
    logger.info(f"PARAMETER: remove_spaces = {remove_spaces}")

    NAMED_ROOT.mkdir(exist_ok=True)

    
    for folder_name in folder_list:  # Fixed: removed parentheses after folder_list
        # Process the folder name
        processed_name = str(folder_name).strip()  # Fixed: changed 'name' to 'folder_name'
        
        if force_lowercase:
            processed_name = processed_name.lower()
        
        if remove_spaces:
            processed_name = processed_name.replace(" ", "")
        
        # Skip empty names after processing
        if not processed_name:
            logger.warning(f"Skipping empty folder name from: {folder_name}")
            continue
        
        folder_path = NAMED_ROOT / processed_name
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")

    pass


  
#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################

def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each item in a list 
    using a concise form of a for loop called a list comprehension.

    Arguments:
    folder_list -- A list of strings (e.g., ['csv', 'excel']).
    prefix -- A string to prefix each name (e.g., 'output-').
    '''

    logger.info("FUNCTION: create_prefixed_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, prefix = '{prefix}'")

    # Ensure the root directory exists
    PREFIXED_LC_ROOT.mkdir(exist_ok=True)

    # Create directories using list comprehension for process and loop for creation
    [ (PREFIXED_LC_ROOT /f"{prefix}{folder_name}").mkdir(exist_ok=True)
      for folder_name in folder_list ]
    
    # Log the created folders
    for folder_name in folder_list:
        folder_path = PREFIXED_LC_ROOT / f"{prefix}{folder_name}"
        logger.info(f"Created prefixed folder: {folder_path}")


  

#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically over time.

    Arguments:
    duration_seconds -- The number of seconds to wait between folder creations.
    '''    
    logger.info("FUNCTION: create_folders_periodically()")
    logger.info(f"PARAMETER: duration_seconds = {duration_seconds}")

    # Ensure the directory exists
    TIMED_ROOT.mkdir(exist_ok=True)

    # Use a counter to control how many folders to make
    folder_count = 5
    counter = 1
    
    while counter <= folder_count:
        # Create folder with timestamp in name
        folder_name = f"timed_folder_{counter}_{int(time.time())}"
        folder_path = TIMED_ROOT / folder_name

        # Create the folder
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")

        # Log the wait time
        if counter < folder_count: 
            logger.info(f"Waiting {duration_seconds} seconds before the next folder...")
            time.sleep(5)

        counter += 1

    logger.info(f"Created {folder_count} folders periodically")
  


#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################

def create_standardized_folders(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of names with options to standardize names.

    Arguments:
    folder_list -- A list of strings representing folder names.
    to_lowercase -- If True, convert names to lowercase.
    remove_spaces -- If True, remove spaces from names.
    '''

    logger.info("FUNCTION: create_standardized_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, to_lowercase = {to_lowercase}, remove_spaces = {remove_spaces}")

    # Ensure the root directory exists
    STANDARD_ROOT.mkdir(exist_ok=True)

    for folder_name in folder_list:
        # Standardize the folder name
        processed_name = str(folder_name).strip()

        # Make lowercase
        if to_lowercase:
            processed_name = processed_name.lower()

        # Remove spaces
        if remove_spaces:
            processed_name = processed_name.replace(" ", "")

        # Skip empty names after processing
        if not processed_name:
            logger.warning(f"Skipping empty folder name from {folder_name}")
            continue

        #Create the standardized folder
        folder_path = STANDARD_ROOT / processed_name
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Create standardized folder: {folder_path}")


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    logger.info("#####################################")
    logger.info("# Starting execution of main()")
    logger.info("#####################################\n")

    logger.info(f"Byline: {utils_chrisbraun.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using list comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'output-'
    create_prefixed_folders_using_list_comprehension(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call function 5 to create standardized folders, no spaces, lowercase
    create_standardized_folders(REGIONS, to_lowercase=True, remove_spaces=True)

    logger.info("\n#####################################")
    logger.info("# Completed execution of main()")
    logger.info("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()