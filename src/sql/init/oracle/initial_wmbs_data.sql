-- Initial data inserts for Oracle

-- Job states, dependent on src/python/WMCore/JobStateMachine/Transitions.py
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'new');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'created');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'executing');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'complete');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'success');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'retrydone');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'exhausted');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'killed');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'createcooloff');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'createfailed');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'createpaused');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'submitcooloff');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'submitfailed');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'submitpaused');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'jobcooloff');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'jobfailed');
INSERT INTO wmbs_job_state (id, name) VALUES (wmbs_job_state_SEQ.nextval, 'jobpaused');

-- Subscription types
INSERT INTO wmbs_sub_types (id, name, priority) VALUES (wmbs_sub_types_SEQ.nextval, 'Production', 0);
INSERT INTO wmbs_sub_types (id, name, priority) VALUES (wmbs_sub_types_SEQ.nextval, 'Processing', 0);
INSERT INTO wmbs_sub_types (id, name, priority) VALUES (wmbs_sub_types_SEQ.nextval, 'Cleanup', 1);
INSERT INTO wmbs_sub_types (id, name, priority) VALUES (wmbs_sub_types_SEQ.nextval, 'LogCollect', 2);
INSERT INTO wmbs_sub_types (id, name, priority) VALUES (wmbs_sub_types_SEQ.nextval, 'Skim', 3);
INSERT INTO wmbs_sub_types (id, name, priority) VALUES (wmbs_sub_types_SEQ.nextval, 'Merge', 4);
INSERT INTO wmbs_sub_types (id, name, priority) VALUES (wmbs_sub_types_SEQ.nextval, 'Harvesting', 5);

-- Location states
INSERT INTO wmbs_location_state (id, name) VALUES (wmbs_location_state_SEQ.nextval, 'Normal');
INSERT INTO wmbs_location_state (id, name) VALUES (wmbs_location_state_SEQ.nextval, 'Down');
INSERT INTO wmbs_location_state (id, name) VALUES (wmbs_location_state_SEQ.nextval, 'Draining');
INSERT INTO wmbs_location_state (id, name) VALUES (wmbs_location_state_SEQ.nextval, 'Aborted');

-- Checksum types
INSERT INTO wmbs_checksum_type (id, type) VALUES (wmbs_checksum_type_SEQ.nextval, 'cksum');
INSERT INTO wmbs_checksum_type (id, type) VALUES (wmbs_checksum_type_SEQ.nextval, 'adler32');
INSERT INTO wmbs_checksum_type (id, type) VALUES (wmbs_checksum_type_SEQ.nextval, 'md5'); 