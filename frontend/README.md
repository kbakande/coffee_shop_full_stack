# Coffee Shop Frontend

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI  is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

## Required Tasks

### Configure Enviornment Variables

Ionic uses a configuration file to manage environment variables. These variables ship with the transpiled software and should not include secrets.

- Open `./src/environments/environments.ts` and ensure each variable reflects the system you stood up for the backend.

## Running Your Frontend in Dev Mode

Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the `frontend` directory and run:

```bash
ionic serve
```

>_tip_: Do not use **ionic serve**  in production. Instead, build Ionic into a build artifact for your desired platforms.
[Checkout the Ionic docs to learn more](https://ionicframework.com/docs/cli/commands/build)

## Key Software Design Relevant to Our Coursework

The frontend framework is a bit beefy; here are the two areas to focus your study.

### Authentication

The authentication system used for this project is Auth0. `./src/services/auth.service.ts` contains the logic to direct a user to the Auth0 login page, managing the JWT token upon successful callback, and handle setting and retrieving the token from the local store. This token is then consumed by our DrinkService (`./src/services/auth.service.ts`) and passed as an Authorization header when making requests to our backend.

### Authorization

The Auth0 JWT includes claims for permissions based on the user's role within the Auth0 system. This project makes use of these claims using the `auth.can(permission)` method which checks if particular permissions exist within the JWT permissions claim of the currently logged in user. This method is defined in  `./src/services/auth.service.ts` and is then used to enable and disable buttons in `./src/pages/drink-menu/drink-form/drink-form.html`.


<!-- coffeeUser1

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk0RENhcElob1V0T3ZYV3RqM0VUQSJ9.eyJpc3MiOiJodHRwczovL2F1dGgyMDIwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjVlZmEyZTMzZjFjYzAwNzA3OGM5ZmUiLCJhdWQiOiJodHRwczovL2NvZmZlZV9hcGkuY29tIiwiaWF0IjoxNjAwMDg5NjQxLCJleHAiOjE2MDAwOTY4NDEsImF6cCI6IlpCNTE2bTQzODVNb01ObnBOZGdyVUx1SjBkUjJIMm1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.IXvAp3UCEorPwS79FOR8UBaB3rat9DwoyCsBWj7oldfaeAFWLWahjaEuaH1Ocx-BkMKhdT3yC1odlT7tMJihO4pmmqBl2H1cCYZCqi0Jmv7kBnGTEku4mEB-WBvaIgtiHYPvpGZDAFXaZ0RiRdGqZgmn9BB9juJQMj0VNnXQu-Rj005KT5sZipVdl6CVV3X8o8dy56AOYxmPlKhxIE1kGZG52oXUy4EJid3hjIXC26yprbP3Zg40dwbkD-5Ra22AkHej4ZvBXJ3PlmLtiXlCbVGA1eV9g61ng_MjjIcinhBPcppZAdbSIoJZI7tu5-u-YAIMRp-bKfvNeo4oQMyNTg -->


<!-- coffee user 2

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijk0RENhcElob1V0T3ZYV3RqM0VUQSJ9.eyJpc3MiOiJodHRwczovL2F1dGgyMDIwLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjVlZmE3YzRlY2E1ZjAwNzdiOTc1YWYiLCJhdWQiOiJodHRwczovL2NvZmZlZV9hcGkuY29tIiwiaWF0IjoxNjAwMDkwMDQ5LCJleHAiOjE2MDAwOTcyNDksImF6cCI6IlpCNTE2bTQzODVNb01ObnBOZGdyVUx1SjBkUjJIMm1HIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.KLr47qsWawE8kn4OS--3Lrkw23Jn1BuazLsvQwQxEo8f2E9TkVGE-ngQWHk9YHnFBjqGLvIjj1_i-X3i9TNe0TQMkvUvNhJBK_RqvVkUxIKjOK0QvTllob1049TtuiYFJDQnI2WrteeL8TcKvQP1cNtkTLRNa39uaWsiulZJQXLkC6UI-VVb2dfnIf9SXiZjLZfgugq-tMiNgcUIxuhCJ8ek7Un4UdNTw8nMswOXe8uGuRLNg6m7IMIO-oZk9qO02J7reuPP5bOa517CHO4-GVh8vLN-p1zX10qecOub0AYeAQXpc5wBoyL7GGJwAGn2E-yKnaGtWsfCWizUjVfV7g -->