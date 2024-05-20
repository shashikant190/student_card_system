import time
from barcode import Code128
from barcode.writer import ImageWriter

def generate_unique_barcode():
    
    timestamp = str(int(time.time()))  
    barcode_value = f'STUDENT-{timestamp}'  

    
    barcode = Code128(barcode_value, writer=ImageWriter())
    barcode_filename = barcode.save('studentcard/static/barcodes/barcode')

    return f'/static/barcodes/{barcode_filename}'
