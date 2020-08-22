![Django Vue GraphQL](https://user-images.githubusercontent.com/41876764/90949742-c89b2d80-e3ff-11ea-8119-502574320d13.png)

# dja_vue_gql

This is a Tutorial for using Django with Vue and GraphQL

## Table of contents

- [Setting up the project](#setting-up-the-project)
- [Setting up the project with Docker](#setting-up-the-project-with-docker)
- [Cleaning up the Container and Image](#cleaning-up-the-container-and-image)
- [Inspiration](#inspiration)
- [Contact](#contact)

## Setting up the project

  Start by cloning the project with the command:
  ```
  $ git clone https://github.com/rmiyazaki6499/dja_vue_gql.git
  ```
  
  ## Setting up the project with Docker

  For those that are not interested in setting up the project manually or would simply not have to worry about downloading node.js and its dependencies, I have created a Dockerfile and docker-compose.yml file to help create a container with everything you would need to run the **project**.

  ### Install Docker

  To make this as easy as possible, we will be using *Docker Compose* to creat our container.

  - If you do not have Docker yet, start by downloading it here if you are on a Mac or Windows:
  https://www.docker.com/products/docker-desktop

  - Or if you are on a Linux Distribution follow the directions here:
  https://docs.docker.com/compose/install/

  - To confirm you have Docker Compose, open up your terminal and run the command below:

  ```
  $ docker-compose --version
  docker-compose version 1.26.2, build eefe0d31
  ```
  
  - Go into the project directory to build and run the container with:

  ```
  $ cd tour-of-heros/
  $ docker-compose up -d --build
  ```

  **This may take a few moments**
  
  Navigate to http://localhost:8000/graphql to view the site on the local server.
  
  ### Cleaning up the Container and Image

  - To stop the container from running, use `<Ctrl-C>` twice.
  - To close down the container use the command:

  ```
  $ docker-compose down
  ```
  - Then to clean up the container and image which we are no longer using use the command:

  ```
  $ docker system prune -fa
  ```

  - Confirm that the container and image is no longer there with:

  ```
  $ docker system df -v
  ```

## Inspiration

Django Vue.js and GraphQL - Step by step
by Arkadiusz Klemenko
https://alexiej.github.io/django-vue-graphql/#_1-create-django-project

## Contact

[Ryuichi Miyazaki](https://github.com/rmiyazaki6499)
