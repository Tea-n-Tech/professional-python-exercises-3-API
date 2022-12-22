# Exercise3: API

## Purpose

This is the third exercise for the professional python course. The purpose is to build an API for the GitHub CLI (from exercise 2).
The inital state is a fork from the 2nd exercise (Solution from Codie)

## Task (copied from Tea-n-Tech)

This task will be an advancement of the previous one by wrapping the
functionality in an API.
Create an API with the following routes:

- GET `/health/ping` to check if the API is up (can be unauthenticated)
- Require a GitHub token as authentication header and use this token for
  your API calls to GitHub within your API
- GET `/user` to get details about the currently authenticated user
- GET `/user/stars` to retrieve the amount of GitHub stars of all repos from the
  authenticated user
- GET `/user/status` to get the current status of the authenticated user (see
  task 2)
- POST `/user/status` to set the users status to drinking tea (see task 2)
- GET `/users/{username}` to get data about the specified user
- GET `/users/{username}/stars` to get the amount of total stars from all repos
  of the specified user

What is important?

- Document your API endpoints (hint: if you do this right, it is done
  automatically)
- The API needs to be wrapped and published as a docker image
- Add a task command to start the docker image (makes life easier)


## Quickstart

### Installing

TBD

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

Find the documentation TBD
