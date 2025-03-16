
import json
import time
import subprocess
import pandas as pd 


def galaxy_names():
    """
    Reads a list of galaxy names from a tab-separated values file.

    The function loads the data from 'galaxies.txt', which contains a column 
    labeled 'Object' representing the galaxy names. It returns these names as 
    a list of strings.

    Returns:
        List[str]: A list of galaxy names.
    """

    df = pd.read_csv('galaxies.txt', sep='\t')
    galaxy_names = df['Object'].to_list()

    return galaxy_names


def get_galaxy_coords(galaxy_name):
    """
    Fetches the coordinates (RA and Dec) of a given galaxy from the Nasa/IPAC Extragalactic Database (NED).
    
    Args:
        galaxy_name (str): The name of the galaxy to be searched in NED.
    
    Returns:
        tuple: The coordinates (RA and Dec) of the given galaxy as a tuple of strings.
    """

    url = 'https://ned.ipac.caltech.edu/srs/ObjectLookup'
    post_data = f'json={{"name":{{"v":"{galaxy_name}"}}}}'
    curl_command = ["curl", "-s", "-X", "POST", "--data", post_data, url]
 
    output = subprocess.run(curl_command, capture_output=True, text=True)

    try:
        data = json.loads(output.stdout)
        ra = data.get('Preferred', {}).get('Position', {}).get('RA', "Não encontrado")
        dec = data.get('Preferred', {}).get('Position', {}).get('Dec', "Não encontrado")
    except json.JSONDecodeError:
        print("Error decoding JSON")

    return ra, dec


if __name__ == '__main__':

    galaxy_names = galaxy_names()

    file_name = 'galaxies_coords.txt'

    with open(file_name, 'w') as f:
        f.write('Galaxy Name\tRA\tDEC\n')

        init = time.time()
        for i in range(len(galaxy_names)):
            ra,dec = get_galaxy_coords(galaxy_names[i])

            f.write(f'{galaxy_names[i]}\t{ra}\t{dec}\n')

        end = time.time()
        print(f'Execution time: {round(end - init, 1)} seconds')