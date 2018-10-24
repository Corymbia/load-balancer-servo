# Copyright 2012 Eucalyptus Systems, Inc.
#
# Redistribution and use of this software in source and binary forms,
# with or without modification, are permitted provided that the following
# conditions are met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
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

from distutils.core import setup
import setuptools

def getVersion():
    try:
        return open('VERSION').read().rstrip()
    except IOError:
        return "0"

setup (name="Eucalyptus Loadbalancer Servo",
    version = getVersion(),
    description = "Eucalyptus Loadbalancer Servo",
    long_description = "Eucalyptus Loadbalancer Servo",
    author = "Sang-Min Park",
    author_email = "community@eucalyptus.com",
    license = "BSD",
    url = "http://eucalyptus.cloud",
    packages = ['servo', 'servo/haproxy', 'servo/ws', 'servo/mon', 'servo/security', 'servo/floppy', 'servo/workflow'],
    scripts = ['load-balancer-servo'],
    data_files = [('/etc/load-balancer-servo/',
        ['scripts/haproxy_template.conf',
         'scripts/boto.cfg',
         'scripts/boto3.cfg',
         'scripts/503.http'])],
    entry_points={
        'console_scripts': [
            'load-balancer-servo-workflow=servo.workflow.client:main',
        ]
    },
)

