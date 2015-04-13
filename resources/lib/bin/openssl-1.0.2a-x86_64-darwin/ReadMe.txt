=============================================================================
OpenSSL v1.0.2a                                Precompiled Binaries for OSX
-----------------------------------------------------------------------------

                         *** Release Information ***

Release Date:     Apr 13, 2015

Author:           Andrew Leech (andrew@alelec.net)

Dependencies:     The libraries have no noteworthy dependencies (I hope)

Installation:     Copy both dylib files into your application directory

Supported OS:     OSX

-----------------------------------------------------------------------------

                          *** Legal Disclaimer ***

THIS SOFTWARE IS PROVIDED BY ITS AUTHOR "AS IS" AND ANY 
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY 
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND 
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF 
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

OpenSSL license terms are provided in the file "OpenSSL License.txt".

PLEASE CHECK IF YOU NEED TO COMPLY WITH EXPORT RESTRICTIONS FOR CRYPTOGRAPHIC
SOFTWARE AND/OR PATENTS.

-----------------------------------------------------------------------------

                       *** Build Information Win64 ***

Built with:       OSX Yosemite 10.10.2
                  Darwin alelec.local 14.1.0 
                  Darwin Kernel Version 14.1.0: Thu Feb 26 19:26:47 PST 2015; 
                  root:xnu-2782.10.73~1/RELEASE_X86_64 x86_64

                  # cc --version
                  Apple LLVM version 6.1.0 (clang-602.0.49) (based on LLVM 3.6.0svn)
                  Target: x86_64-apple-darwin14.1.0
                  Thread model: posix

Commands:         

#############################################################################

#!/bin/bash
OPENSSL_VERSION="1.0.2a"

# Download
curl -O http://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz
tar -xvzf openssl-$OPENSSL_VERSION.tar.gz

# Build
cd openssl-$OPENSSL_VERSION
./Configure darwin64-x86_64-cc -shared --openssldir="@rpath"
make
cd ../

# Copy to output folder
mkdir -p openssl-$OPENSSL_VERSION-x86_64-darwin
mv openssl_x86_64/libcrypto.1.0.0.dylib openssl-$OPENSSL_VERSION-x86_64-darwin/
mv openssl_x86_64/libssl.1.0.0.dylib openssl-$OPENSSL_VERSION-x86_64-darwin/

#############################################################################