# TOURNAMENT RESULTS

Done as a project for Udacity's "Full Stack Web Developer" Nanodegree .

### Technologies Used

* [vagrant] - enables users to create and configure lightweight, reproducible, and portable development environments
* [VirutalBox] - create virtual machines
* [python] - Programming Language
* [PostgreSQL] - DBMS

### Usage (on Ubuntu, or other GNU/Linux based Operating Systems)

* make sure virtualbox and vagrant are installed on your machine
* download the latest vm required (https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488015_fsnd-virtual-machine/fsnd-virtual-machine.zip)
* unzip the file
* cd <directory where file is unzipped>/vagrant
* enter "vagrant up" in the terminal (this sets up the vm, wait for the vm to be downloaded and setup for you)
* enter "vagrant ssh" in the terminal (ssh into the machine)
* cd /vagrant/tournament in the terminal (the project files are located here)
* download the latest files from (https://github.com/brucekaushik/tournamentdb)
* unzip and replace the files from the downloaded folder into the tournament folder on your host machine (find it from the location you unzipped the vm)
* enter "psql" in the terminal (to connect to PostgreSQL)
* enter "\i tournament.sql" in the terminal (to import the database and tables)
* enter "\q" in the terminal (to quit postgresql)
* enter "python tournament_test.py" (to run the unit tests)

if all the test are passed, then the project ran successfully!


