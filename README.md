# recon

## Purpose of the System

The system is a web-based tool for users, who want to gain a total overview which would give them complete control over their financial situation. 

Recon allows a user to keep track of their net worth, by making entries on passives and assets and graphing the results. Each month will be shown in a stacked area chart, where the influence of each category can be seen.

The user should sign in through a site, with their username and password. The password will be checked in the database, to see if it exists. If this is the case, the user is signed in and has access to the routes which require a sign in.

# Design

An explanation of how the system will be implemented.

## UML Class diagram

[https://app.diagrams.net/#G10RxW33EdBzllMn-QZ37ZrhiGSTSRU5KO](https://app.diagrams.net/#G10RxW33EdBzllMn-QZ37ZrhiGSTSRU5KO)

## Entity Relation diagram

[https://app.diagrams.net/#G1_bErnE_pVYwQWMrDqNIXDUz8er32ksrk](https://app.diagrams.net/#G1_bErnE_pVYwQWMrDqNIXDUz8er32ksrk)

## Login

The login part of the system will use [Flask-Login](https://flask-login.readthedocs.io/en/latest/#your-user-class).  The database will store a hashed/salted version of the password and e-mail, to keep the data secure.

## Budget

The budget page will display a pie chart, based on the entries that a user has entered. The data could be loaded into a tuple to increase overview of the situation

Required entries from user:

- Monthly income
- Monthly expenses
- Amount saved each month
- Amount invested

Pie chart:

- 100% equal to monthly income
