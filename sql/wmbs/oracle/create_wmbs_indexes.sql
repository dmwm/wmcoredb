-- Index creation statements for Oracle

CREATE INDEX wmbs_fileset_files_idx_fileset ON wmbs_fileset_files(fileset)
    TABLESPACE &1;

CREATE INDEX wmbs_fileset_files_idx_fileid ON wmbs_fileset_files(fileid)
    TABLESPACE &1;

CREATE INDEX wmbs_file_runlumi_map_fileid ON wmbs_file_runlumi_map(fileid)
    TABLESPACE &1;

CREATE INDEX wmbs_file_location_fileid ON wmbs_file_location(fileid)
    TABLESPACE &1;

CREATE INDEX wmbs_file_location_pnn ON wmbs_file_location(pnn)
    TABLESPACE &1;

CREATE INDEX wmbs_file_parent_parent ON wmbs_file_parent(parent)
    TABLESPACE &1;

CREATE INDEX wmbs_file_parent_child ON wmbs_file_parent(child)
    TABLESPACE &1;

-- Workflow related indexes
CREATE INDEX wmbs_workflow_output_workflow ON wmbs_workflow_output(workflow_id)
    TABLESPACE &1;

CREATE INDEX wmbs_workflow_output_fileset ON wmbs_workflow_output(output_fileset)
    TABLESPACE &1;

CREATE INDEX wmbs_workflow_output_merged ON wmbs_workflow_output(merged_output_fileset)
    TABLESPACE &1;

-- Subscription related indexes
CREATE INDEX wmbs_subscription_fileset ON wmbs_subscription(fileset)
    TABLESPACE &1;

CREATE INDEX wmbs_subscription_workflow ON wmbs_subscription(workflow)
    TABLESPACE &1;

CREATE INDEX wmbs_subscription_subtype ON wmbs_subscription(subtype)
    TABLESPACE &1;

CREATE INDEX wmbs_sub_files_available_sub ON wmbs_sub_files_available(subscription)
    TABLESPACE &1;

CREATE INDEX wmbs_sub_files_available_file ON wmbs_sub_files_available(fileid)
    TABLESPACE &1;

CREATE INDEX wmbs_sub_files_acquired_sub ON wmbs_sub_files_acquired(subscription)
    TABLESPACE &1;

CREATE INDEX wmbs_sub_files_acquired_file ON wmbs_sub_files_acquired(fileid)
    TABLESPACE &1;

CREATE INDEX wmbs_sub_files_failed_sub ON wmbs_sub_files_failed(subscription)
    TABLESPACE &1;

CREATE INDEX wmbs_sub_files_failed_file ON wmbs_sub_files_failed(fileid)
    TABLESPACE &1;

CREATE INDEX wmbs_sub_files_complete_sub ON wmbs_sub_files_complete(subscription)
    TABLESPACE &1;

CREATE INDEX wmbs_sub_files_complete_file ON wmbs_sub_files_complete(fileid)
    TABLESPACE &1;

-- Job related indexes
CREATE INDEX wmbs_jobgroup_sub ON wmbs_jobgroup(subscription)
    TABLESPACE &1;

CREATE INDEX wmbs_jobgroup_output ON wmbs_jobgroup(output)
    TABLESPACE &1;

CREATE INDEX wmbs_job_jobgroup ON wmbs_job(jobgroup)
    TABLESPACE &1;

CREATE INDEX wmbs_job_state_idx ON wmbs_job(state)
    TABLESPACE &1;

CREATE INDEX wmbs_job_location_idx ON wmbs_job(location)
    TABLESPACE &1;

CREATE INDEX wmbs_job_assoc_job ON wmbs_job_assoc(job)
    TABLESPACE &1;

CREATE INDEX wmbs_job_assoc_file ON wmbs_job_assoc(fileid)
    TABLESPACE &1;

CREATE INDEX wmbs_job_mask_job ON wmbs_job_mask(job)
    TABLESPACE &1;

-- Workunit related indexes
CREATE INDEX wmbs_workunit_taskid ON wmbs_workunit(taskid)
    TABLESPACE &1;

CREATE INDEX wmbs_workunit_status ON wmbs_workunit(status)
    TABLESPACE &1;

CREATE INDEX wmbs_job_workunit_job ON wmbs_job_workunit_assoc(job)
    TABLESPACE &1;

CREATE INDEX wmbs_job_workunit_workunit ON wmbs_job_workunit_assoc(workunit)
    TABLESPACE &1;

CREATE INDEX frl_workunit_assoc_workunit ON wmbs_frl_workunit_assoc(workunit)
    TABLESPACE &1;

CREATE INDEX frl_workunit_assoc_fileid ON wmbs_frl_workunit_assoc(fileid)
    TABLESPACE &1;

CREATE INDEX frl_workunit_assoc_run ON wmbs_frl_workunit_assoc(run)
    TABLESPACE &1;

CREATE INDEX frl_workunit_assoc_lumi ON wmbs_frl_workunit_assoc(lumi)
    TABLESPACE &1;

-- Location related indexes
CREATE INDEX wmbs_location_pnns_loc_idx ON wmbs_location_pnns(location)
    TABLESPACE &1;

CREATE INDEX wmbs_location_pnns_pnn_idx ON wmbs_location_pnns(pnn)
    TABLESPACE &1;

-- Checksums related indexes
CREATE INDEX wmbs_file_checksums_type ON wmbs_file_checksums(typeid)
    TABLESPACE &1;

CREATE INDEX wmbs_file_checksums_file ON wmbs_file_checksums(fileid)
    TABLESPACE &1; 