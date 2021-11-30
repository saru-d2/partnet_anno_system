var be_config = exports;

// Host and Port Information (SET UP HERE!)
be_config.remoteHost = 'http://localhost';
be_config.remotePort = '8080';

// get annotation info (Don't Change!)
be_config.get_anno_info = '/annotation/get_info';
be_config.save_anno_json = '/annotation/save_json';
be_config.get_anno_json = '/annotation/get_json';
be_config.save_anno_snapshot = '/annotation/save_snapshot';
be_config.update_anno_version = '/annotation/update_version';
be_config.get_anno_obj_list = '/annotation/get_obj_list';
be_config.save_anno_obj_list = '/annotation/save_obj_list';
be_config.get_qa_data = '/annotation/get_qa';
be_config.save_qa_data = '/annotation/save_qa';

// get files (Don't Change!)
be_config.get_original_part = '/file/original-part';
be_config.get_remesh_part = '/file/remesh-part';
be_config.get_new_part = '/file/new-part';
be_config.get_original_scene_graph = '/file/original-scene-graph';
be_config.get_remesh_cut_json = '/file/remesh-cut-output-json';
be_config.get_model_screenshot = '/file/model-sceneshot';

// remesh related (Don't Change!)
be_config.request_remesh = '/remesh';
be_config.submit_remesh = '/submit_remesh_cut';

// user anno list viewer (Don't Change!)
be_config.anno_list_viewer = '/part_anno_list_viewer';
