# -*- python -*- coding: ISO-8859-1 -*-
# Copyright 2004 Fundacion Via Libre
#
# This file is part of PAPO.
# 
# PAPO is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# PAPO is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with PAPO; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from Misc import Misc, _
from Exceptions import LabelError

class Label(Misc):
    """
    The Label widget displays a small amount of text.

    Labels may contain mnemonics. Mnemonics are underlined characters
    in the label, used for keyboard navigation. Mnemonics are created
    by providing a string with an underscore before the mnemonic
    character, such as "_File", to the method set_text_with_mnemonic().

    To make it easy to format text in a label (changing colors, fonts,
    etc.), label text can be provided in a simple markup format.
    
    Labels can be made selectable with set_selectable(). Selectable
    labels allow the user to copy the label contents to the
    clipboard. Only labels that contain useful-to-copy information -
    such as error messages - should be made selectable.

    Additional keyword arguments:
    """
    __kwargs = ('label', 'mnemonicWidget', 'justify', 'useMarkup',
                'useUnderline', 'selectable', 'lineWrap')
    __doc__ += "%s\n" % (__kwargs,)

    def setLabel(self, label):
        """
        Sets the text within the Label widget.
        """
        if self.delegate('will_set_label', args=label):
            try:
                self._doSetLabel(unicode(label))
            except:
                raise LabelError, _("Unable to set label")
            return True
        return False
    def getLabel(self):
        return self._doGetLabel()

    def setJustify(self, justify):
        """
        justify is one of 'left', 'right', 'center', 'fill', or None.

        Sets the alignment of the lines in the text of the label
        relative to each other. Left is the default value when the
        widget is first created. If you instead want to set the
        alignment of the label as a whole, use setAlignment()
        instead. setJustify() has no effect on labels containing only
        a single line.

        """
        if self.delegate('will_justify', args=justify):
            try:
                self._doSetJustify(justify)
            except:
                raise LabelError, _("Unable to set justification")
            return True
        return False
    def getJustify(self):
        """
        Returns the current justification (one of 'left', 'right',
        etc.)
        """
        return self._doGetJustify()
    
    def setMnemonicWidget(self, widget):
        """

        If the label has been set so that it has an mnemonic key
        (using use_underline()) the label can be associated with a
        widget that is the target of the mnemonic. When the label is
        inside a widget (like a Button or a Notebook tab) it is
        automatically associated with the correct widget, but
        sometimes (i.e. when the target is a Entry next to the label)
        you need to set it explicitly using this function.

        The target widget will be accelerated by emitting
        "mnemonic_activate" on it. The default handler for this signal
        will activate the widget if there are no mnemonic collisions
        and toggle focus between the colliding widgets otherwise.
        
        """
        if self.delegate('will_set_mnemonic_widget', args=widget):
            try:
                self._doSetMnemonicWidget(widget)
            except:
                raise LabelError, _("Unable to set mnemonic widget")
            return True
        return False
    def getMnemonicWidget(self):
        """
        This is probably very time-intensive; try not to use it.
        """
        return self._doGetMnemonicWidget()

    def setUseMarkup(self, use):
        """
        Sets whether the text of the label contains markup in Pango's
        text markup language.

        Takes one argument, a bool.
        """
        if self.delegate('will_use_markup', args=use):
            try:
                self._doSetUseMarkup(use)
            except:
                if use:
                    raise LabelError, _("Unable to use markup")
                else:
                    raise LabelError, _("Unable to stop using markup")
            return True
        return False
    def getUseMarkup(self):
        return self._doGetUseMarkup()
    

    def setUseUnderline(self, use):
        """
        Sets whether an underline in the text indicates the next
        character should be used for the mnemonic accelerator key.

        Takes one argument, a bool.
        """
        if self.delegate('will_use_underline', args=use):
            try:
                self._doSetUseUnderline(use)
            except:
                if use:
                    raise LabelError, \
                          _("Unable to use underlines for mnemonics")
                else:
                    raise LabelError, \
                          _("Unable to stop using underlines for mnemonics")
            return True
        return False
    def getUseUnderline(self):
        return self._doGetUseUnderline()
                
    
    def setSelectable(self, selectable):
        """
        Selectable labels allow the user to select text from the
        label, for copy-and-paste.

        Takes one argument, a bool.

        """
        if self.delegate('will_set_selectable', args=selectable):
            try:
                self._doSetSelectable(selectable)
            except:
                if selectable:
                    raise LabelError, _("Unable to make text selectable")
                else:
                    raise LabelError, _("Unable to make text unselectable")
            return True
        return False

    def getSelectable(self):
        return self._doGetSelectable()

    def setLineWrap(self, wrap):
        if self.delegate('will_set_line_wrap', args=wrap):
            try:
                self._doSetLineWrap(wrap)
            except:
                if wrap:
                    raise LabelError, _("Unable to wrap lines")
                else:
                    raise LabelError, _("Unable to stop wrapping lines")
            return True
        return False
    def getLineWrap(self):
        return self._doGetLineWrap()

