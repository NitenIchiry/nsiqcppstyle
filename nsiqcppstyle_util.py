# Copyright (c) 2009 NHN Inc. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#    * Neither the name of NHN Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys

SINGLE_QUOTE = "'"
DOUBLE_QUOTE = '"'

def WeAreFrozen():
    return hasattr(sys, "frozen")


def ModulePath():
    if WeAreFrozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


def GetRuntimePath():
    "Return the path of this tool"
    if (sys.platform == "win32"):
        runtimePath = ModulePath()
    else:
        modename = globals()['__name__']
        module = sys.modules[modename]
        runtimePath = os.path.dirname(module.__file__)
    return runtimePath


def GetSystemKey():
    if (sys.platform == "win32"):
        return "window"
    else:
        return "linux"


def CmpObjects(a, b):
    return (a > b) - (a < b)


def RemoveOuterQuotes(raw_string):
    final_string = raw_string.strip()
    if final_string[0] == final_string[-1] and final_string[0] in [SINGLE_QUOTE, DOUBLE_QUOTE]:
        final_string = final_string[1:-1].strip()
    return final_string