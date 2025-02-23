-- Table creation statements for MariaDB
CREATE TABLE wmbs_fileset (
    id          INTEGER      PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(1250) NOT NULL,
    open        INT(1)       NOT NULL DEFAULT 0,
    last_update INTEGER      NOT NULL,
    UNIQUE (name)
);

CREATE TABLE wmbs_file_details (
    id           INTEGER      PRIMARY KEY AUTO_INCREMENT,
    lfn          VARCHAR(1250) NOT NULL,
    filesize     BIGINT,
    events       BIGINT UNSIGNED,
    first_event  BIGINT       UNSIGNED NOT NULL DEFAULT 0,
    merged       INT(1)       NOT NULL DEFAULT 0,
    UNIQUE (lfn)
);

CREATE TABLE wmbs_fileset_files (
    fileid      INTEGER   NOT NULL,
    fileset     INTEGER   NOT NULL,
    insert_time INTEGER   NOT NULL,
    UNIQUE (fileid, fileset),
    FOREIGN KEY(fileset) references wmbs_fileset(id)
);

-- ... rest of the CREATE TABLE statements ... 