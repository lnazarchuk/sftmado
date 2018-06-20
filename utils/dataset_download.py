import os
import colab_fs


flags.DEFINE_string('models_path', '', '')
flags.DEFINE_string('drive_path', '', '')
FLAGS = flags.FLAGS


def main(_):
	assert FLAGS.models_path, '`models_path` is missing.'
	assert FLAGS.drive_path, '`drive_path` is missing.'

	
def load_data(fs):
    #base_dir = '/content/_data'
    base_dir = FLAGS.models_path

	dir = os.path.join(base_dir)
	drive_dir = os.path.join(drive_dir)
    removeAndCreateNewDir(dir)
    fs.load_file_from_drive(dest_dir = dir, filename=drive_dir)

	
def removeAndCreateNewDir(dirPath):
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        os.rmdir(dirpath)
    
    os.makedirs(dirpath)
	
	
if __name__=='__main__':
    fs = colab_fs.GoogleColabFS()
    load_data(fs)
