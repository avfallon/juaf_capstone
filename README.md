# ZehnFunds Customer Rewards System

### Senior Project of Jeffrey Umanzor and Andrew Fallon

## Project Overview

This is a student project concerned with creating and implementing an automated, customer facing rewards program for the ecommerce website ZehnTek. Customer accounts are given one "ZehnFund" for every cent that is spent on the site, and the status of those ZehnFunds can be seen and interacted with on the website that we have created. 

Our project also involves creating a separate (but connected) administrative program that allows for account access and automated email alerts for ZehnTek customers. Both the website and administrator program are connected to a normalized MySQL database, which stores all user accounts and accesses the larger, external database that ZehnTek uses to track their purchases.


## Implemented Features

Our database communication system is almost exclusively through PHP scripts, and we have implemented all PHP scripts that we will need to relay data between both the website and the administrator program. 

We have created a website for user interaction with the program, and established the framework for communication for the database and between different pages in the website.

The administrative program is not entirely complete, but we have implemented a simple interface for the administrator to interact with the program, as well as the PHP scripts necessary to interact with the database for the automated email program


## Not Yet Implemented Features

We are continuing to fully link up our database to our website, and implementing javascript to receive the results of the PHP scripts and translate it to the front-end of the website. We also are not providing a fully customer-facing front end, as ZehnTek has their own style guidelines for their front-end that their developers will implement upon delivery. However, we still have to fully flesh out our front end to make it as realistic and presentable as possible.

We still need to implement the automated email functionality of our administrative program, as well as extending the user interface to include that expanded functionality. 


## Dependencies

**Database:** We use the mysqli extension for PHP to interact with our MySQL database.

**Website:** Our website is currently built and hosted on Loyola's studentvhost servers, which is currently for testing purposes and will be unnecessary upon handoff, as ZehnTek has their own servers.

**Admin Program:** Our program requires use of the Unix command line for operation and accesses the Python SMTP library for the implementation of the email functionality.


## Instructions For Compilation

Our code can be found at https://github.com/avfallon/juaf_capstone

**Website:** 

**Admin Program:**


## Instructions for Running

**Website:** 

**Admin Program:**



