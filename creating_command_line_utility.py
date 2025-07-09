import argparse
import requests

def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

#Add command line argument
parser.add_argument("url", help="url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", help="Name of the file", default=None)


# parse the argument
args = parser.parse_args()

# use the argument in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)


# cd F:\Python\CWH_Python\Python_Day85
# python creating_command_line_utility.py https://imagej.net/images/Cell_Colony2.jpg -o pranav.jpg
# python creating_command_line_utility.py https://imagej.net/images/Cell_Colony2.jpg
# python creating_command_line_utility.py https://imagej.net/images/Cell_Colony2.jpg -o mycell.jpg