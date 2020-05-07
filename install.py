# installer for crt
# Copyright 2014-2017 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return CRTInstaller()

class CRTInstaller(ExtensionInstaller):
    def __init__(self):
        super(CRTInstaller, self).__init__(
            version="0.21",
            name='crt',
            description='Emit a Cumulus realtime.txt for LOOP data.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            process_services='user.crt.CumulusRealTime',
            config={
                'CumulusRealTime' : {
                    'filename': '/var/tmp/realtime.txt'}},
            files=[('bin/user', ['bin/user/crt.py'])]
            )
