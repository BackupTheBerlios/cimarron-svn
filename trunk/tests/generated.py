from commonTests import abstractTestDelegate

class abstractTestDelegateGenerated(abstractTestDelegate):
    def testChainDelegationyy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyyy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyyn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyyY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyyN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationyyu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyny(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationynn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationynY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationynN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationynu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyYy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyYn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyYY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyYN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyYu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationyNy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationyNn(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationyNY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationyNN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationyNu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationyu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyuy(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyun(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyuY(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationyuN(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationyuu(self):
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationny(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnyy(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnyn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnyY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnyN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnyu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnny(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnnn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnnY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnnN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnnu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnYy(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnYn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnYY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnYN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnYu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnNy(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnNn(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnNY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnNN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnNu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnuy(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnun(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnuY(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationnuN(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationnuu(self):
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationYy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYyy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYyn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYyY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYyN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYyu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYny(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYnn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYnY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYnN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYnu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYYy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYYn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYYY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYYN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYYu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYNy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYNn(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYNY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYNN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYNu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYuy(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYun(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYuY(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYuN(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationYuu(self):
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationNy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNyy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNyn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNyY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNyN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNyu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNny(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNnn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNnY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNnN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNnu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNYy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNYn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNYY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNYN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNYu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNNy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNNn(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNNY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNNN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNNu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNuy(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNun(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNuY(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNuN(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationNuu(self):
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuyy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuyn(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuyY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuyN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuyu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationun(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuny(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationunn(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationunY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationunN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationunu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuYy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuYn(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuYY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuYN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuYu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuNy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuNn(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuNY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuNN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuNu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuuy(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_yes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuun(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_no)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuuY(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedYes)
        self.assertEqual(self.widget.delegate('foo'), True)
    def testChainDelegationuuN(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_forcedNo)
        self.assertEqual(self.widget.delegate('foo'), False)
    def testChainDelegationuuu(self):
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.widget.delegates.append(self.delegate_unknown)
        self.assertEqual(self.widget.delegate('foo'), True)
