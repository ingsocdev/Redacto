#!/usr/bin/env python3
import configparser
from time import sleep
from os import getcwd, listdir, remove
from os.path import isfile, join
from pathlib import Path
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def transform_pdf(files, input_dir, output_dir, split_into_multiple_pages, poppler_path):
    images = [convert_from_path(join(input_dir, f).replace('\\', '/'), output_folder=output_dir,
                                output_file=f, single_file=(not split_into_multiple_pages), fmt='png', dpi=200,
                                poppler_path=poppler_path) for f in files]

    for i in images[0]:
        image_path = i.filename.replace('\\', '/')
        new_filename = image_path.replace('.png', '.pdf')

        image = Image.open(image_path).convert('RGB')
        # Save the image as a PDF
        image.save(Path(join(output_dir, new_filename)))
        print('processed {0}'.format(new_filename))

        # Close the BufferedReader so we can delete the images after
        i.fp.close()
        # Remove the image
        remove(image_path)

    # Remove the input files when we're done
    [remove(join(input_dir, f).replace('\\', '/')) for f in files]


if __name__ == '__main__':
    application_dir = getcwd()
    config = configparser.ConfigParser()
    config.read('config.ini')

    input_dir = config['DEFAULT']['InputDirectory']
    output_dir = config['DEFAULT']['OutputDirectory']
    split_into_multiple_pages = config['DEFAULT'].getboolean('SplitIntoMultiplePages')

    poppler_path = join(application_dir, 'poppler-0.68.0', 'bin')

    print('Redacto (c) 2020 Tom Brown')

    while True:
        print('listening for pdf files in {0}'.format(input_dir))
        list_of_input_files = [f for f in listdir(input_dir) if isfile(join(input_dir, f))]

        if list_of_input_files:
            [print('Found: {0}'.format(f)) for f in list_of_input_files]

            transform_pdf(list_of_input_files, input_dir, output_dir, split_into_multiple_pages, poppler_path)
        sleep(10)

