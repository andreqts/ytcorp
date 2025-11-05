# ytcorp

## Requirements

1. **Linux Ubuntu 20** (or similar system)  
1. **Python 3.8.10** or higher  
1. **PostgreSQL 12** or higher  
1. **SQLAlchemy 2.0.25** or higher  

## Setup

### 1. PostgreSQL

- Configure access (remote or local) according to the intended use (_local_ or _remote_; _peer_, _trust_, _md5_, etc.).  
- Create the database **before** running the model.  
- Set the following environment variables in the `~/.bashrc` file (in your HOME directory):

```bash
export YT_DB_NAME="your_database_name"
export YT_DB_USER="your_username"
export YT_DB_PASSWORD="your_password"
export YT_DB_HOST="your_host"
export YT_DB_HOST_PORT="your_port"
