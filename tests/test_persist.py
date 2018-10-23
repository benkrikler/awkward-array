#!/usr/bin/env python

# Copyright (c) 2018, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import struct
import unittest
import zlib

import numpy

from awkward import *
from awkward.persist import *

class Test(unittest.TestCase):
    def runTest(self):
        pass

    def test_uncompressed_numpy(self):
        storage = {}
        a = numpy.arange(100, dtype=">u2").reshape(-1, 5)
        serialize(a, storage, compression=None)
        b = deserialize(storage)
        assert numpy.array_equal(a, b)
        assert a.dtype == b.dtype
        assert a.shape == b.shape

    def test_compressed_numpy(self):
        storage = {}
        a = numpy.arange(100, dtype=">u2").reshape(-1, 5)
        serialize(a, storage, compression=zlib.compress)
        b = deserialize(storage)
        assert numpy.array_equal(a, b)
        assert a.dtype == b.dtype
        assert a.shape == b.shape

    def test_jagged(self):
        storage = {}
        a = awkward.JaggedArray.fromiter([[1.1, 2.2, 3.3], [], [4.4, 5.5]])
        serialize(a, storage)
        b = deserialize(storage)
        assert a.tolist() == b.tolist()
