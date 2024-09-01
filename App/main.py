import os
from BinReader import BinReader

current_script_abs_path = os.path.dirname(__file__)
bin_file_rel_path = "../Binaries/file_01.bin"
bin_file_abs_path = os.path.join(current_script_abs_path, bin_file_rel_path)

txt_file_rel_path = "../Txt/file_01.txt"
txt_file_abs_path = os.path.join(current_script_abs_path, txt_file_rel_path)

def main():
    
    bin_reader = BinReader(bin_file_abs_path)
    bin_reader.read()
    bin_reader.show(starter_address=0, final_address=15)
    bin_reader.save(txt_file_abs_path, starter_address=0, final_address=8192)

if __name__ == "__main__":
    main()
