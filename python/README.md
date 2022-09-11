# Python implementation for cosmos.proto

Currently, this repo contains generated python files for Terra 2 and Osmosis Blockchains supported Modules.

### Setup

1. Create virtual environment 

```
$ python3 -m venv env
$ source env/bin/activate
```

2. Install poetry
```
$ pip install poetry
```

3. Install packages,

```
$ pip install poetry
$ poetry install
```

If you encounter "version solving failed." error, try `poetry add <package_name>`, followed by `poetry lock` and then `poetry install`

### Generating python files for new proto files

We use `betterproto[compiler]` for generating python code from proto files, and it is party a manual process. Here are a few pointers to help you through the process - 


- `cd` into each module and make sure all *.proto files are in one place.
- For each .proto file, check the import paths and update them if needed. 
- Once the paths are corrected, use the following command to generate python files. 

```
$ protoc -I . --python_betterproto_out=<OUTPUT DIR NAME> <PROTO FILE NAMES>
```

For eq - protoc -I . --python_betterproto_out=py genesis.proto query.proto gov.proto feetoken.proto

To install `betterproto[compiler]`, use - 

```
pip install "betterproto[compiler]"
```



TO DO : Update the scripts