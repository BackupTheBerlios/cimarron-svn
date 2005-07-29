# -*- coding: utf-8 -*-
#
# Copyright 2005 Fundación Via Libre
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

from testCommon import abstractTestDelegate

class abstractTestDelegateGenerated(abstractTestDelegate):
    def testChainDelegationyy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyyy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyyn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyyY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyyN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationyyu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyny(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationynn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationynY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationynN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationynu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyYy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyYn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyYY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyYN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyYu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationyNy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationyNn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationyNY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationyNN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationyNu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationyu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyuy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyun(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyuY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationyuN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationyuu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationny(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnyy(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnyn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnyY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnyN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnyu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnny(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnnn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnnY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnnN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnnu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnYy(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnYn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnYY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnYN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnYu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnNy(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnNn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnNY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnNN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnNu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnuy(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnun(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnuY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationnuN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationnuu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationYy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYyy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYyn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYyY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYyN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYyu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYny(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYnn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYnY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYnN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYnu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYYy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYYn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYYY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYYN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYYu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYNy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYNn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYNY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYNN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYNu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYuy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYun(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYuY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYuN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationYuu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationNy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNyy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNyn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNyY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNyN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNyu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNny(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNnn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNnY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNnN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNnu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNYy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNYn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNYY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNYN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNYu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNNy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNNn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNNY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNNN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNNu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNuy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNun(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNuY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNuN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationNuu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuyy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuyn(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuyY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuyN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuyu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationun(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuny(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationunn(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationunY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationunN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationunu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuYy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuYn(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuYY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuYN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuYu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuNy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuNn(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuNY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuNN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuNu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuuy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuun(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuuY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assert_(self.widget.delegate('foo'))
    def testChainDelegationuuN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assert_(not self.widget.delegate('foo'))
    def testChainDelegationuuu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assert_(self.widget.delegate('foo'))
