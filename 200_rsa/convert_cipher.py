#!/usr/bin/python
import binascii

dec_num = bin(71175655094365510043263808848786722857227222116838633004069795456707064192489654424640458266528806706546030491880127054743217358636395191037202557252511200)
binary = binascii.hexlify(dec_num)
print binascii.b2a_base64(binary)