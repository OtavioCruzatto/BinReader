import os

MAXIMUM_QTY_BYTES = 8192

class BinReader:

    def __init__(self, file_path):

        self.file_name = ""
        self.file_path = ""
        self.bytes = []
        self.qty_max_bytes = MAXIMUM_QTY_BYTES
        self.actual_qty_bytes = 0
        self.file_found = False

        if os.path.isfile(file_path):
            self.file_path = file_path
            self.file_name = os.path.basename(self.file_path)
            self.actual_qty_bytes = os.stat(self.file_path).st_size
            self.file_found = True
            #print("File found")
        else:
             print("File do not exist")
    
    def __str__(self):
        return \
            f"\n========================================\n" \
            f"File name: {self.file_name}\n" \
            f"File path: {self.file_path}\n" \
            f"Actual qty bytes: {self.actual_qty_bytes}\n" \
            f"Max allowable qty bytes: {self.qty_max_bytes}\n" \
            f"========================================\n"

    def read(self):
        if self.file_found == True:
            with open(self.file_path, "rb") as bin_file:
                self.bytes = bin_file.read(self.actual_qty_bytes)

            #print("File read")
    
    def show(self, starter_address=0, final_address=MAXIMUM_QTY_BYTES):
        qty_bytes_to_show = 0
        start = 0
        stop = 0

        if self.file_found == True:
            if final_address > self.actual_qty_bytes:
                final_address = self.actual_qty_bytes
                print(f"Qty of bytes limited to {self.actual_qty_bytes}")

            print("              00 01 02 03 04 05 06 07 08 09 |   ASCII    |")
            qty_bytes_to_show = final_address - starter_address

            while (qty_bytes_to_show):
                start = final_address - qty_bytes_to_show
                if (qty_bytes_to_show > 10):
                    stop = final_address - qty_bytes_to_show + 10
                else:
                    stop = final_address

                aux_bytes = list(self.bytes[start:stop])
                aux_string = ""
                for i in range(len(aux_bytes)):
                    if((aux_bytes[i] >= 32) and (aux_bytes[i] <= 126)):
                        aux_string = aux_string + chr(aux_bytes[i])
                    else:
                        aux_string = aux_string + '.'

                qty_bytes_to_show -= 10
                #print(f"First address: {start:04d} | Last address: {stop-1:04d}")
                print(f"Address {start:04d}: {self.bytes[start:stop].hex(' '):29s} | {aux_string:10s} |")

                if(qty_bytes_to_show < 0):
                   break
    
    def save(self, file_path, starter_address=0, final_address=MAXIMUM_QTY_BYTES):
        qty_bytes_to_save = 0
        start = 0
        stop = 0

        if self.file_found == True:
            if final_address > self.actual_qty_bytes:
                final_address = self.actual_qty_bytes
                print(f"Qty of bytes limited to {self.actual_qty_bytes}")

            if os.path.isfile(file_path):
                
                open(file_path, "w").close()

                with open(file_path, "a") as txt_file:
                    line = \
                            "Address: Decimal base.\n" \
                            "Values: Hexadecimal base.\n" \
                            "Values: Ascii format when it exists, dot otherwise.\n\n" \
                            "              00 01 02 03 04 05 06 07 08 09 |   ASCII    |\n"
                    txt_file.write(line)

                    qty_bytes_to_save = final_address - starter_address

                    while (qty_bytes_to_save):
                        start = final_address - qty_bytes_to_save
                        if (qty_bytes_to_save > 10):
                            stop = final_address - qty_bytes_to_save + 10
                        else:
                            stop = final_address

                        aux_bytes = list(self.bytes[start:stop])
                        aux_string = ""
                        for i in range(len(aux_bytes)):
                            if((aux_bytes[i] >= 32) and (aux_bytes[i] <= 126)):
                                aux_string = aux_string + chr(aux_bytes[i])
                            else:
                                aux_string = aux_string + '.'
                        
                        qty_bytes_to_save -= 10
                        #print(f"First address: {start:04d} | Last address: {stop-1:04d}")
                        line = f"Address {start:04d}: {self.bytes[start:stop].hex(' '):29s} | {aux_string:10s} |\n"
                        txt_file.write(line)

                        if(qty_bytes_to_save < 0):
                            break
            else:
                print("Not file")
