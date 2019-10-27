# Python REST Server with Status Web Pages

This project is a bootstrap template for using Flask as a REST Server.

## Description

It took me a while to setup things but this template is based off the microscoft template for flask application. I first added the dash framework to generate plots and added a test case for two dummy graphs.

The application starts with the views.py file houses the routes for the flask server while the rest_ends has the REST API End points. To add more REST End points, replicate the class for actions and then add endpoint urls and strings.

For generating the graphs, the dashboard.html page calls the /graphs end point using the JQuery calls in the inderpreet.js script.

These calls are handled by the views.py and data_methods.py functions.

## Prerequisites

VirtualEnv and Python are required.
See requirements.txt

Requires an Internet Connection since the plotly.js scripts are accessed from elsewhere. 

## Installation/Building

run the setup.sh script. It should take care of everything

## Making Changes

## Troubleshooting and FAQ

## Contributing

## Author and License

Designed by [Inderpreet Singh](https://inderpreet.github.io)

This software may be distributed and modified under the terms of the GNU
General Public License version 2 (GPL2) as published by the Free Software
Foundation and appearing in the file LICENSE.TXT included in the packaging of
this file. Please note that GPL2 Section 2[b] requires that all works based
on this software must also be made publicly available under the terms of
the GPL2 ("Copyleft").

We put a lot of time and effort into our project and hence this copyright 
notice ensures that people contribute as well as each contribution is 
acknowledged. Please retain this original notice and if you make changes
please document them below along with your details.

The latest copy of this project/library can be found at: 
https://github.com/inderpreet/
