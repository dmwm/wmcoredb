-- Index creation statements for MariaDB
CREATE INDEX wmbs_fileset_files_idx_fileset ON wmbs_fileset_files(fileset);
CREATE INDEX wmbs_fileset_files_idx_fileid ON wmbs_fileset_files(fileid);
CREATE INDEX wmbs_file_runlumi_map_fileid ON wmbs_file_runlumi_map(fileid);
CREATE INDEX wmbs_file_location_fileid ON wmbs_file_location(fileid);
CREATE INDEX wmbs_file_location_pnn ON wmbs_file_location(pnn);
CREATE INDEX wmbs_file_parent_parent ON wmbs_file_parent(parent);
CREATE INDEX wmbs_file_parent_child ON wmbs_file_parent(child);
CREATE INDEX idx_wmbs_workf_out_workflow ON wmbs_workflow_output(workflow_id);
CREATE INDEX idx_wmbs_workf_out_fileset ON wmbs_workflow_output(output_fileset);
CREATE INDEX idx_wmbs_workf_mout_fileset ON wmbs_workflow_output(merged_output_fileset);

-- Continue with all other index creation statements... 