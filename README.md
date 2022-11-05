# Exercise2: GitHub Command line interface (CLI)

## Purpose

This is the second exercise for the professional python course. The purpose is to build a proper CLI using the github API.
The task is (copied from the professional python course): 

Create a python program to interact with GitHub and retrieve data.
Add the following commands:

- Count all stars of all repos of yourself, a specified user or an organization.
- Print out details about yourself, a user or organization.
  Allow a nicely printed format as default and offer output as json too.
- One of the following:
  - (easy) Modify your user description by adding a tea emoji and a heart.
  - (difficult) Set your user status (top-right when clicking on username)
    to a tea emoji with the message "Drinking Tea".

Focus points:

- End-users will use your program so focus on usability
- Integrate previous lessons as much as it makes sense

## Quickstart

### Installing

This repository uses poetry to install the dependencies and taskfile to execute the most basic functionality. 
After having installed taskfile onto your system you can simply use ```task install``` to install the necessary dependendcies into a virtual environment. 4
Besides the dependencies you will need a GitHub Access Token to use this program. Get it [here]("https://github.com/settings/tokens).

### Usage

Promt ```task``` to get a list of the tasks availabe and go for one of the options: 

```bash
$ task
task: Available tasks for this project:
* build:                Builds the puthon package
* docs-publish:         Publish the documentation to gh-pages
* docs-serve:           Serve the documentation locally
* getdetails:           Get details of a given user and print it to console
* getdetailsjson:       Get details of a given user in json
* install:              Installs the dependecies based on the poetry file
* lint:                 Runs formatting and linting
* sbom:                 Generate the Software Bill of Materials
* stars:                Get the number of stars of the given user's repositories
* starsjson:            Get the number of stars of the given user's repositories in json format
* status:               Set the status of your user to something delicous
* test:                 Runs tests on the code
```

The other way of using this tool is directly with calling etiher poetry or native python to start on of the functions, like 

```bash
poetry run python professional_python_exercises_2_githubcli/github_cli.py setstatus
```
