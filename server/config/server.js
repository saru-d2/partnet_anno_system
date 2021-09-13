var server = exports;

// SET UP HERE!
server.HOST = 'localhost';
server.PORT = '8080';
server.DB_HOST = "localhost";
server.DB_USER = "root";
server.DB_PASSWORD = "";
server.DB_NAME = "partnet_anno_system";
server.CODE_DIR = "/usr/app/partnet_anno_system/"

// DO NOT CHANGE!
server.DIR = server.CODE_DIR + "/storage/";
server.DATA_DIR = 'data';
server.ORI_PART_DIR = 'leaf_part_obj_normalized';
server.DOWNLOAD_DIR = 'downloads';
server.ANNO_DIR = 'annotations';
server.REMESH_PART_DIR = 'remesh_parts';
server.NEW_PART_DIR = 'new_parts';
server.ANNO_RES_DIR = 'anno_results';
server.PART_HIER_DIR = 'part_hier_templates';
server.SCREENSHOT_DIR = 'screenshots';

// set the maximum number of annotations per model
server.MAX_NUM_ANNOS_PER_MODEL = 1;
