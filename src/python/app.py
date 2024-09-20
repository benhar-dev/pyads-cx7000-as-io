import pyads

plc = pyads.Connection('5.137.185.168.1.1', 27905)
plc.open()

myInput = plc.get_symbol(index_group=0xF031, index_offset=0x1E0, plc_datatype=pyads.PLCTYPE_BOOL)
myOutput = plc.get_symbol(index_group=0xF021, index_offset=0x138, plc_datatype=pyads.PLCTYPE_BOOL)
myAInput = plc.get_symbol(index_group=0xF030, index_offset=0x36, plc_datatype=pyads.PLCTYPE_INT)

print(myInput.read())
print(myAInput.read())

myOutput.write(False)

plc.close()