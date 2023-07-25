import os
import glob
import argparse

from spdx_tools.spdx.parser.parse_anything import parse_file
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document
from spdx_tools.spdx.writer.write_anything import write_file

def parse_arguments():
    parser = argparse.ArgumentParser(description="SPDX Directory and Output Parser")

    # Add arguments for SPDX directory, main file, and output file.
    parser.add_argument(
        "-d", "--spdx-directory",
        type=str,
        required=True,
        help="The directory containing SPDX JSON files.",
    )
    parser.add_argument(
        "-m", "--main-file",
        type=str,
        required=True,
        help="The main SPDX JSON file.",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="The output SPDX filename.",
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
print("LOG : get json files OK")

main_doc = parse_file(args.main_file)

for f in spdx_files:
    print("doing {}".format(f))
    try:
        doc = parse_file(f)
        main_doc.packages += doc.packages
    except:
        print("error reading : {}".format(f))
        continue

print("LOG : parse json files OK")

validation_messages = validate_full_spdx_document(main_doc)
for validation_message in validation_messages:
    print("WARNING : {}".format(validation_message.validation_message))

# write file anyway
write_file(main_doc, args.output, validate=False)
