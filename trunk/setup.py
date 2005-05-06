#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2003 Fundación Via Libre
#
# This file is part of PAPO.
#
# PAPO is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PAPO is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PAPO; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307 USA

from distutils.core import setup

setup(name='cimarron',
      version='0.2',
      description='Cimarrón GUI component framework',
      long_description='''
Hab'ia una vez un coso.
Blah, blah, blah.

Yeah, that's about it.
''',
      author='Fundación Vía Libre - PAPO team',
      author_email='cimarron-hackers@berlios.de',
      url='http://papo.vialibre.org.ar/',
      license='GPL',
      packages=['papo',
                'papo.cimarron',
                'papo.cimarron.skins',
                'papo.cimarron.skins.common',
                'papo.cimarron.skins.gtk2',
                'papo.cimarron.tools',
                'papo.cimarron.controllers',
                ],
      classifiers=['Development Status :: 3 - Alpha',
                   # some day:
                   # 'Environment :: Win32 (MS Windows)',
                   # 'Environment :: Console',
                   # 'Environment :: Web Environment'
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Natural Language :: Spanish',
                   'Natural Language :: English',
                   'Operating System :: POSIX',
                   # untested:
                   # 'Operating System :: Microsoft :: Windows :: Windows 95/98/2000',
                   # 'Operating System :: Microsoft :: Windows :: Windows NT/2000',
                   # 'Operating System :: MacOS',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: User Interfaces',
                   ],
      )
