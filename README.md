# merge-yocto-spdx

This tool is intended to merge the "package" part of each SPDX generated by Yocto.
The generated SPDX file will contain the name and version of each package contained in the yocto image.

The original intent was to merge Yocto SPDX in one file in order to provide it to Daggerboard SBOM analysis tool (https://github.com/nyph-infosec/daggerboard)

## Usage

A [cqfd](https://github.com/savoirfairelinux/cqfd) usage is recommended.
Use `cqfd init` to create the Docker image and `cqfd run ./merge_spdx.py -h` to list options for the script.

### SPDX_DIRECTORY option

The `-d` option must point to a directory containing all yocto generated spdx.
It is basically the content of the `my-image.spdx.tar.zst` provided by Yocto

When decompressing Yocto SPDX archive, please remove all `recipe*.spdx.json` and `runtime*.spdx.json`
They will not be understood by daggerboard and will just pollute your data.

### MAIN_FILE option

This option must point to the `my-image.spdx.json` provided by yocto.
This document will be the root document in which all other packages will be added.

### OUTPUT option

This will be the name of the document written by the tool. It can be either a `.json` file or a `.spdx` file.

## Troubleshooting

Analyzing yocto SPDX can be very long for big files. From my experience, sdpx files over 3M can take several minutes to be parsed.
