import os
import colab_fs

def load_data(fs):
    base_dir = '/content/_data'

	newDir = os.path.join(base_dir, 'Img')
    removeAndCreateNewDir(newDir)
    fs.load_file_from_drive(dest_dir = newDir, filename='Category and Attribute Prediction Benchmark/Img/img.zip')
    fs.unzip_file(newDir, os.path.join(base_dir, 'Img','img.zip'))

    newDir = os.path.join(base_dir, 'Eval')
	removeAndCreateNewDir(newDir)
    fs.load_file_from_drive(dest_dir = newDir, filename='Category and Attribute Prediction Benchmark/Eval/list_eval_partition.txt')

    newDir = os.path.join(base_dir, 'Anno')
	removeAndCreateNewDir(newDir)
    base_path = 'Category and Attribute Prediction Benchmark/Anno'
    anno_files = ['list_landmarks.txt', 'list_category_img.txt', 'list_category_cloth.txt', 'list_attr_img.txt', 'list_attr_cloth.txt', 'list_bbox.txt']
    for anno_file in anno_files:
        full_name = os.path.join(base_path, anno_file)
        fs.load_file_from_drive(dest_dir = os.path.join(base_dir, 'Anno'), filename=full_name)

def removeAndCreateNewDir(dirPath):
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        os.rmdir(dirpath)
    
    os.makedirs(dirpath)

		
if __name__=='__main__':
    fs = colab_fs.GoogleColabFS()
    load_data(fs)
