# ytcorp

## Project Overview

This project provides a relational database builder designed to organize and store a corpus of YouTube videos, including metadata and transcriptions, for research purposes.
At its current stage, the system is a work in progress, implementing only the database schema and populating it with data collected from the associated research project.
Planned developments include dashboard or web-based interfaces to enable data exploration and facilitate data science analyses of the corpus.

### Research Context
The corpus originates from a research project focused on analyzing regulatory framework proposals aimed at fostering the diffusion of Community Microgrids in Brazil, as a strategy to promote the sustainable integration of intermittent distributed renewable energy sources, particularly within electricity distribution systems.

### Project Structure

The project is structured as follows:

- `models.py`: implements data models via SQLAlchemy ORM for the database tracking YouTube videos, speakers, events, etc. It is also responsible for droping any existing database and creating a new one.
- `setupdb.py`: that is the main script to be run to create the database and populate it with data. When it is loaded, it imports models.py and creates the database, and then populates it with data.

### How to run the project

1. First, make sure you have the required dependencies installed, as described in the [Requirements](#requirements) section.
2. Before running the project, make sure you have a PostgreSQL database created and configured. You must create a database that yoiu can name it freely (e.g. `ytcorp` or `corpus-youtube`) using the PostgreSQL client or any other database management tool (unfortunately and curiously, I could not find a way to do it using Python in a practical way for this simple builder, using SQLAlchemy and PostgreSQL, so you will have to do it manually).
3. Run the project using the following command:

```bash
python setupdb.py
```

4. The script will create the database and populate it with data, so you can start using it right away using psql or any other database management application, and ordinary SQL queries or other tools.


## Requirements

1. **Linux Ubuntu 20.04** (or any compatible Linux distro) or later
1. **Python 3.8.10** or higher  
1. **PostgreSQL 12** or higher  
1. **SQLAlchemy 2.0.25** or higher  

## Setup

### 1. Install dependencies

    Install the dependencies listed in the `requirements.txt` file (using `pip install -r requirements.txt`).    

### 2. PostgreSQL

- Configure database access (remote or local) according to your intended usage (_local_ or _remote_; _peer_, _trust_, _md5_, etc.).  
- Create the database **before** running the model. You can name it freely (e.g. `ytcorp` or `corpus-youtube`)
- Set the following environment variables in the `~/.bashrc` file (in your HOME directory), using values consistent with your database setup:

```bash
export YT_DB_NAME="your_database_name"
export YT_DB_USER="your_username"
export YT_DB_PASSWORD="your_password"
export YT_DB_HOST="your_host"
export YT_DB_HOST_PORT="your_port"
```

- Restart your terminal session to apply the changes, or run `source ~/.bashrc`

