[![SQL Linting](https://github.com/amaltaro/wmcoredb/actions/workflows/sql-lint.yml/badge.svg)](https://github.com/amaltaro/wmcoredb/actions/workflows/sql-lint.yml)
[![MariaDB Schema Validation](https://github.com/amaltaro/wmcoredb/actions/workflows/mariadb-schema-test.yml/badge.svg)](https://github.com/amaltaro/wmcoredb/actions/workflows/mariadb-schema-test.yml)
[![Oracle Schema Validation](https://github.com/amaltaro/wmcoredb/actions/workflows/oracle-schema-test.yml/badge.svg)](https://github.com/amaltaro/wmcoredb/actions/workflows/oracle-schema-test.yml)

# WMCore Database Schema

Database schema definitions for WMCore components, including both MariaDB and Oracle backends.

WMBS (Workload Management Bookkeeping Service) provides the database schema for managing 
workloads and jobs.

## CI/CD Pipeline

The continuous integration pipeline is split into three workflows:

### SQL Linting
Validates SQL syntax and formatting using SQLFluff:
* MariaDB files using default SQLFluff rules
* Oracle files using custom rules defined in `.sqlfluff.oracle`
* Enforces consistent SQL style and formatting
* Runs on every push and pull request

### MariaDB Schema Validation
Automatically tests schema deployment in MariaDB:
* Runs only after successful linting
* Tests against multiple MariaDB versions:
  - 10.6 (LTS)
  - 10.11 (LTS)
  - 11.4 (Latest)
* Deploys and validates:
  - TestDB Schema
  - WMBS Schema
  - Agent Schema
  - DBS3Buffer Schema
  - BossAir Schema
  - ResourceControl Schema
* Verifies table structures and relationships
* Checks for any critical database errors

### Oracle Schema Validation
Tests schema deployment in Oracle:
* Runs only after successful linting
* Uses Oracle XE 18.4.0-slim container
* Deploys and validates the same schemas as the MariaDB workflow:
  - TestDB Schema
  - WMBS Schema (tables, indexes, and initial data)
  - Agent Schema
  - DBS3Buffer Schema
  - BossAir Schema
  - ResourceControl Schema
* Verifies table structures, indexes, foreign key relationships, and initial data
* Ensures cross-database compatibility between MariaDB and Oracle backends

## Directory Structure

The database schema files are organized as follows:

```
project_root/
├── sql/                   # Database schema files
│   ├── tier0/             # Tier0 schema definitions
│   │   ├── oracle/       # Oracle-specific Tier0 SQL files
│   │   │   ├── create_tier0_tables.sql    # Table definitions with constraints
│   │   │   ├── create_tier0_indexes.sql   # Index definitions
│   │   │   ├── create_tier0_functions.sql # Helper functions
│   │   │   └── initial_tier0_data.sql     # Initial data for Tier0 tables
│   │   └── mariadb/      # MariaDB-specific Tier0 SQL files: NOT IMPLEMENTED
│   ├── wmbs/              # WMBS schema definitions
│   │   ├── oracle/       # Oracle-specific WMBS SQL files
│   │   │   ├── create_wmbs_tables.sql     # Table definitions with constraints
│   │   │   ├── create_wmbs_indexes.sql    # Index definitions
│   │   │   ├── create_wmbs_sequences.sql  # Sequence definitions
│   │   │   └── create_wmbs_functions.sql  # Helper functions
│   │   └── mariadb/      # MariaDB-specific WMBS SQL files
│   │       ├── create_wmbs_tables.sql     # Table definitions with constraints
│   │       ├── create_wmbs_indexes.sql    # Index definitions
│   │       └── create_wmbs_functions.sql  # Helper functions
│   ├── agent/             # WMCore.Agent.Database schema
│   │   ├── oracle/
│   │   └── mariadb/
│   ├── bossair/           # WMCore.BossAir schema
│   │   ├── oracle/
│   │   └── mariadb/
│   ├── dbs3buffer/        # WMComponent.DBS3Buffer schema
│   │   ├── oracle/
│   │   └── mariadb/
│   └── resourcecontrol/   # WMCore.ResourceControl schema
│       ├── oracle/
│       └── mariadb/
│   └── testdb/            # WMQuality.TestDB schema
│       ├── oracle/
│       │   └── create_testdb.sql  # Test table definitions
│       └── mariadb/
│           └── create_testdb.sql  # Test table definitions
└── src/
    └── python/
        └── db/            # Schema generation code
            ├── wmbs/
            ├── agent/
            ├── bossair/
            ├── dbs3buffer/
            ├── resourcecontrol/
            └── testdb/
            └── execute_wmbs_sql.py
```

## Schema Components

The WMAgent database schema consists of several components:

1. **WMBS** (`sql/wmbs/`)
   - Core workload and job management
   - Tables for jobs, subscriptions, and file tracking
   - Initial data for job states and subscription types

2. **Agent Database** (`sql/agent/`)
   - Core agent functionality
   - Component and worker management

3. **BossAir** (`sql/bossair/`)
   - Job submission and tracking
   - Grid and batch system integration

4. **DBS3Buffer** (`sql/dbs3buffer/`)
   - Dataset and file management
   - Checksum and location tracking

5. **ResourceControl** (`sql/resourcecontrol/`)
   - Site and resource management
   - Threshold control

6. **Test Database** (`sql/testdb/`)
   - Simple test tables for database validation
   - Used for testing database connectivity and basic operations
   - Includes tables with different data types and constraints
   - Available for both Oracle and MariaDB backends

## WMBS Schema Initialization

The WMBS schema is initialized first and consists of three files:

```
sql/wmbs/{oracle,mariadb}/
├── create_wmbs_tables.sql   # Core WMBS tables
├── create_wmbs_indexes.sql  # Indexes for performance
└── initial_wmbs_data.sql   # Initial data like job states
```

These files are executed in order by `execute_wmbs_sql.py` to set up the base WMBS schema before other components are initialized.

## Database Backend Support

The schema supports two database backends:

- **Oracle**
  - Uses `NUMBER(11)` for integers
  - Uses `VARCHAR2` for strings
  - Uses `GENERATED BY DEFAULT AS IDENTITY` for auto-increment

- **MariaDB**
  - Uses `INT` for integers
  - Uses `VARCHAR` for strings
  - Uses `AUTO_INCREMENT` for auto-increment
  - Uses `ENGINE=InnoDB ROW_FORMAT=DYNAMIC`

## Schema Generation

The SQL schema files are generated from Python code in `src/python/db/`. Each component has its own schema generation code:

```python
from WMCore.Database.DBCreator import DBCreator

class Create(DBCreator):
    def __init__(self, logger=None, dbi=None, params=None):
        # Schema definition in Python
```

The schema files can be executed using `execute_wmbs_sql.py`, which handles:
- Database backend detection
- Schema file location
- Transaction management
- Error handling

## Logs

Some relevant logs from the WMAgent 2.3.9.2 installation:
```
Start: Performing init_agent
init_agent: triggered.
Initializing WMAgent...
init_wmagent: MYSQL database: wmagent has been created
DEBUG:root:Log file ready
DEBUG:root:Using SQLAlchemy v.1.4.54
INFO:root:Instantiating base WM DBInterface
DEBUG:root:Tables for WMCore.WMBS created
DEBUG:root:Tables for WMCore.Agent.Database created
DEBUG:root:Tables for WMComponent.DBS3Buffer created
DEBUG:root:Tables for WMCore.BossAir created
DEBUG:root:Tables for WMCore.ResourceControl created
checking default database connection
default database connection tested
...
_sql_write_agentid: Preserving the current WMA_BUILD_ID and HostName at database: wmagent.
_sql_write_agentid: Creating wma_init table at database: wmagent
_sql_write_agentid: Inserting current Agent's build id and hostname at database: wmagent
_sql_dumpSchema: Dumping the current SQL schema of database: wmagent to /data/srv/wmagent/2.3.9/config/.wmaSchemaFile.sql
Done: Performing init_agent
```
## WMAgent DB Initialization

It starts in the CMSKubernetes [init.sh](https://github.com/dmwm/CMSKubernetes/blob/master/docker/pypi/wmagent/init.sh#L465) script, which executes `init_agent()` method from the CMSKubernetes [manage](https://github.com/dmwm/CMSKubernetes/blob/master/docker/pypi/wmagent/bin/manage#L112) script.

The database optios are enriched dependent on the database flavor, such as:
```bash
    case $AGENT_FLAVOR in
        'mysql')
            _exec_mysql "create database if not exists $wmaDBName"
            local database_options="--mysql_url=mysql://$MDB_USER:$MDB_PASS@$MDB_HOST/$wmaDBName "
        'oracle')
            local database_options="--coredb_url=oracle://$ORACLE_USER:$ORACLE_PASS@$ORACLE_TNS "
```

It then executes WMCore code, calling a script called [wmagent-mod-config](https://github.com/dmwm/WMCore/blob/master/bin/wmagent-mod-config).

with command line arguments like:
```bash
    wmagent-mod-config $database_options \
                       --input=$WMA_CONFIG_DIR/config-template.py \
                       --output=$WMA_CONFIG_DIR/config.py \
```

which internally parses the command line arguments into `parameters` and modifies the standard [WMAgentConfig.py](https://github.com/dmwm/WMCore/blob/master/etc/WMAgentConfig.py), saving it out as the new WMAgent configuration file, with something like:
```
    cfg = modifyConfiguration(cfg, **parameters)
    saveConfiguration(cfg, outputFile)
```

With the WMAgent configuration file properly updated, named `config.py`, now the `manage` script calls [wmcore-db-init](https://github.com/dmwm/WMCore/blob/master/bin/wmcore-db-init), with arguments like:

```bash
wmcore-db-init --config $WMA_CONFIG_DIR/config.py --create --modules=WMCore.WMBS,WMCore.Agent.Database,WMComponent.DBS3Buffer,WMCore.BossAir,WMCore.ResourceControl;
```

This `wmcore-db-init` script itself calls the [WMInit.py](https://github.com/dmwm/WMCore/blob/master/src/python/WMCore/WMInit.py) script, executing basically the next four commands:
```python
wmInit = WMInit()
wmInit.setLogging('wmcoreD', 'wmcoreD', logExists = False, logLevel = logging.DEBUG)
wmInit.setDatabaseConnection(dbConfig=config.CoreDatabase.connectUrl, dialect=dialect, socketLoc = socket)
wmInit.setSchema(modules, params = params)
```

In summary, the WMAgent database schema is an aggregation of the schema defined under each of the following WMAgent python directories:
```
WMCore.WMBS             --> originally under src/python/db/wmbs
WMCore.Agent.Database   --> originally under src/python/db/agent
WMCore.BossAir          --> originally under src/python/db/bossair
WMCore.ResourceControl  --> originally under src/python/db/resourcecontrol
WMComponent.DBS3Buffer  --> originally under src/python/db/dbs3buffer
```

The `wmcore-db-init` script itself calls the [WMInit.py](https://github.com/dmwm/WMCore/blob/master/src/python/WMCore/WMInit.py) script, executing basically the next four commands:
```python
wmInit = WMInit()
wmInit.setLogging('wmcoreD', 'wmcoreD', logExists = False, logLevel = logging.DEBUG)
```

## Contributing

We welcome contributions to WMCoreDB! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:
- Commit message conventions
- Release process
- Development workflow
- Code style guidelines

## Database Compatibility

The SQL files are designed to be compatible with:
- Oracle 19c
- MariaDB 10.6.21

## Usage

To create the database schema:

1. For Oracle:
```sql
@sql/oracle/create_oracle.sql
@sql/testdb/oracle/create_testdb.sql
@sql/tier0/oracle/create_tier0_tables.sql
@sql/tier0/oracle/create_tier0_indexes.sql
@sql/tier0/oracle/create_tier0_functions.sql
@sql/tier0/oracle/initial_tier0_data.sql
@sql/wmbs/oracle/create_wmbs_tables.sql
@sql/wmbs/oracle/create_wmbs_indexes.sql
@sql/wmbs/oracle/create_wmbs_sequences.sql
@sql/wmbs/oracle/create_wmbs_functions.sql
```

2. For MariaDB:
```sql
source sql/testdb/mariadb/create_testdb.sql
source sql/tier0/mariadb/create_tier0_tables.sql
source sql/tier0/mariadb/create_tier0_indexes.sql
source sql/tier0/mariadb/create_tier0_functions.sql
source sql/wmbs/mariadb/create_wmbs_tables.sql
source sql/wmbs/mariadb/create_wmbs_indexes.sql
source sql/wmbs/mariadb/create_wmbs_functions.sql
```

## License

This project is licensed under the terms of the Apache License 2.0.

## WMBS Schema

The WMBS (Workload Management Bookkeeping System) schema is designed to track and manage workflows and jobs. It includes tables for:

- Workflow and job tracking
- File and dataset management
- Subscription and processing information
- Job state and status tracking

### Oracle Implementation

The Oracle implementation uses:
- Sequences for ID generation
- Foreign key constraints
- Organization index tables
- Deterministic functions

### MariaDB Implementation

The MariaDB implementation provides equivalent functionality using:
- AUTO_INCREMENT for ID generation
- Foreign key constraints
- Appropriate indexes
- Compatible function definitions

## Tier0 Schema

The Tier0 schema is designed to support the Tier0 data processing system. It includes tables for:

- Run management and tracking
- Stream and dataset associations
- Lumi section processing
- Configuration management
- Workflow monitoring

### Oracle Implementation

The Oracle implementation uses modern features like:
- IDENTITY columns for auto-incrementing IDs
- Inline foreign key constraints
- Organization index tables for performance
- Deterministic functions for state validation

The schema initialization includes:
- Table definitions with constraints
- Index definitions for performance
- Helper functions for state validation
- Initial data for run states, processing styles, and event scenarios

### MariaDB Implementation

Tier0 system does not - yet - support multiple database backends. For the moment, we have not converted the Tier0 schema to be compliant with MariaDB/MySQL.

## Test Database Schema

The Test Database schema provides a simple set of tables for testing database connectivity and basic operations. It includes:

- Tables with different data types (INT, VARCHAR, DECIMAL)
- Primary key constraints
- Table and column comments
- Cross-database compatibility

### Oracle Implementation

The Oracle implementation uses:
- NUMBER for numeric columns
- VARCHAR2 for string columns
- Table and column comments
- Primary key constraints

### MariaDB Implementation

The MariaDB implementation provides equivalent functionality using:
- INT and DECIMAL for numeric columns
- VARCHAR for string columns
- InnoDB engine specification
- Compatible comment syntax