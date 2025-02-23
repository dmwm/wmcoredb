-- Initial data inserts for MariaDB

-- Job states
INSERT INTO wmbs_job_state (name) VALUES ('none');
INSERT INTO wmbs_job_state (name) VALUES ('new');
INSERT INTO wmbs_job_state (name) VALUES ('created');
INSERT INTO wmbs_job_state (name) VALUES ('executing');
INSERT INTO wmbs_job_state (name) VALUES ('complete');
INSERT INTO wmbs_job_state (name) VALUES ('exhausted');
INSERT INTO wmbs_job_state (name) VALUES ('killed');
INSERT INTO wmbs_job_state (name) VALUES ('failed');

-- Subscription types
INSERT INTO wmbs_sub_types (name, priority) VALUES ('Processing', 0);
INSERT INTO wmbs_sub_types (name, priority) VALUES ('Merge', 4);
INSERT INTO wmbs_sub_types (name, priority) VALUES ('Harvesting', 5);
INSERT INTO wmbs_sub_types (name, priority) VALUES ('Cleanup', 1);
INSERT INTO wmbs_sub_types (name, priority) VALUES ('LogCollect', 2);
INSERT INTO wmbs_sub_types (name, priority) VALUES ('Skim', 3);
INSERT INTO wmbs_sub_types (name, priority) VALUES ('Production', 0);

-- Location states
INSERT INTO wmbs_location_state (name) VALUES ('Normal');
INSERT INTO wmbs_location_state (name) VALUES ('Down');
INSERT INTO wmbs_location_state (name) VALUES ('Draining');
INSERT INTO wmbs_location_state (name) VALUES ('Aborted');

-- Checksum types
INSERT INTO wmbs_checksum_type (type) VALUES ('cksum');
INSERT INTO wmbs_checksum_type (type) VALUES ('adler32');
INSERT INTO wmbs_checksum_type (type) VALUES ('md5');

-- ... rest of the initial data inserts ... 