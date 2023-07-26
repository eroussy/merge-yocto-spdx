#!/bin/python3

import os
import glob
import argparse

from spdx_tools.spdx.parser.parse_anything import parse_file
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document
from spdx_tools.spdx.writer.write_anything import write_file

def parse_arguments():
    parser = argparse.ArgumentParser(description="SPDX Directory and Output Parser")

    parser.add_argument(
        "-d", "--spdx-directory",
        type=str,
        required=True,
        help="The directory containing SPDX files. Only .spdx.json file will be analyzed.",
    )
    parser.add_argument(
        "-m", "--main-file",
        type=str,
        required=True,
        help="The main SPDX file. It will be used as core document, all other packages will be added to it.",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="The output file. It can be a json file or spdx file depending of the extension you choose.",
    )

    args = parser.parse_args()
    return args

args = parse_arguments()

def list_files_in_directory(directory):
    file_list = []
    search_pattern = os.path.join(directory, '*.spdx.json')
    for file_path in glob.glob(search_pattern):
        if os.path.isfile(file_path):
            file_list.append(file_path)
    return file_list

spdx_files = list_files_in_directory(args.spdx_directory)

main_doc = parse_file(args.main_file)

for f in spdx_files:
    print("processing {}".format(f))
    try:
        doc = parse_file(f)
        main_doc.packages += doc.packages
    except:
        print("error reading : {} Drop the file and continue.".format(f))
        continue

# Write file
write_file(main_doc, args.output, validate=False)
