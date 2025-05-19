# MIT License
#
# Copyright (c) 2025 Andrey Zhdanov (rivitna)
# https://github.com/rivitna
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import sys
import io
import struct



def decrypt_nqf_data(enc_data):
    """Decrypt NQF data"""

    data = bytearray(enc_data)

    for i in range(len(data)):
        data[i] = ((data[i] - 84) & 0xFF) ^ 0xA5

    return bytes(data)


#
# Main
#
if len(sys.argv) != 2:
    print('Usage:', sys.argv[0], 'nqf_file')
    sys.exit(0)

filename = sys.argv[1]

with io.open(filename, 'rb') as f:
    enc_data = f.read()

# Decrypt NQF data
data = decrypt_nqf_data(enc_data)

dec_filename = filename + '.dec'
with io.open(dec_filename, 'wb') as f:
    f.write(data)

print('Done!')
