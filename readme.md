# Darts
## _How good is your eye_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Darts is a web application that allows you to create and manage dart games.

- Create players and track down their progress.
- Organize games and enjoy with friends!
- ✨Magic ✨

## Features

- Create players
- Organize dart games

## Install

Darts is running with flask in debug mode, the container exposes the port 5000. You need to build the image and attach that port to anyone free in your host. For example:

    docker build -t darts .
    docker run docker run -d -p 8080:80 darts