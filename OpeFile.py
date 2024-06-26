import os
import shutil
import re
def make_folder(folder_name, dir_file=None):
    """
    dir_file: フォルダを作成するディレクトリのパス（デフォルトはカレントディレクトリ）
    folder_name: 作成するフォルダの名前
    """
    if dir_file is None:
        dir_file = "."

    # ディレクトリが存在しない場合、エラーメッセージを出力して終了
    if not os.path.exists(dir_file):
        print(f"Error: Directory '{dir_file}' does not exist.")
        return
    
    # 作成するフォルダのパスを結合
    new_folder_path = os.path.join(dir_file, folder_name)
    
    # すでに同じ名前のフォルダが存在するかどうかをチェック
    if os.path.exists(new_folder_path):
        print(f"Folder '{folder_name}' already exists in '{dir_file}'.")
    else:
        # フォルダを作成
        os.mkdir(new_folder_path)
        print(f"Folder '{folder_name}' created successfully in '{dir_file}'.")
    return new_folder_path
def copy_rename_file(source_file, dest_folder, new_name):
    """
    source_file: コピーして名前を変更するファイルのパス
    dest_folder: コピーしたファイルを保存するフォルダのパス
    new_name: 新しいファイル名
    """
    # ファイルが存在しない場合、エラーメッセージを出力して終了
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        return
    
    # ディレクトリが存在しない場合、エラーメッセージを出力して終了
    if not os.path.exists(dest_folder):
        print(f"Error: Destination folder '{dest_folder}' does not exist.")
        return
    
    # ファイルのベース名と拡張子を取得
    base_name, extension = os.path.splitext(os.path.basename(source_file))
    
    # コピーして名前を変更したファイルのパス
    dest_file = os.path.join(dest_folder, new_name + extension)
    
    # ファイルをコピーして名前を変更して保存
    shutil.copyfile(source_file, dest_file)
    
    print(f"File copied and renamed successfully to '{dest_file}'.")


def get_numbered_files(folder, extension):
    """
    folder: フォルダのパス
    extension: 拡張子（例: '.txt', '.jpg'）
    """
    numbered_files = []

    # フォルダ内のファイルを走査
    for file_name in os.listdir(folder):
        # 拡張子が一致するかを確認
        if file_name.endswith(extension):
            # ファイル名の連番部分を正規表現で検索
            match = re.match(r'(.+?)(\d+)(\..+)', file_name)
            if match:
                numbered_files.append(file_name)
                
    # ファイル名の連番の部分でソート（数値の大小でソート）
    numbered_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    def _swap_first_and_second(lst):
        if len(lst) >= 2:
            lst[0], lst[1] = lst[1], lst[0]
        return lst
    # numbered_files=_swap_first_and_second(numbered_files)
                
    return numbered_files

folder_path = "."
extension = ".txt"
new_folder_name=["train", "val"]
ratio_train=0.7

original_name=get_numbered_files(folder_path,extension) 
total_img=len(original_name)
num_img=[int(total_img*ratio_train),total_img]

print(num_img)

for name in new_folder_name:
    make_folder(name)
for i,p in enumerate(original_name):
    if i <  num_img[0]: copy_rename_file( folder_path+"/"+p ,folder_path+"/"+new_folder_name[0] , new_folder_name[0] +str(i) )
    if num_img[0]<= i  <num_img[1] : copy_rename_file( folder_path+"/"+p ,folder_path+"/"+new_folder_name[1] , new_folder_name[1] +str(i) )

        


# for i,p in enumerate(get_numbered_files(folder_path,extension) ):
#     if i < start_num: continue
#     if i >= end_num : break
#     copy_rename_file( folder_path+"/"+p ,folder_path+"/"+new_folder_name , new_folder_name+str(i) )
        
    # break

# for file_name in os.listdir(folder_path):
#     print(file_name)