# Exercise3: API

## Purpose

This is the third exercise for the professional python course. The purpose is to build an API for the CLI from exercise2


### Task 3 - API

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

Promt ```task``` to get a list of the tasks availabe and go for one of the options.
Use ```task api``` to start the api / webserver. 
