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

from Dialog import Dialog, _
import cimarron


class MsgDialog (Dialog):
    __FIXME__=True
    def __init__(self, **kw):
        message = kw['message']
        image = kw['image']
        del kw['message']
        del kw['image']
        super(MsgDialog, self).__init__(**kw)
        image.setPadding((12, 6))
        contents = cimarron.getEngine().HBox()
        contents.addChild(image)
        contents.addChild(message)
        self.setContents(contents)

class WarningDialog(MsgDialog):
    __FIXME__=True
    def __init__(self, message=_("<big><b>You are about to do something dangerous.</b></big>\n\nAre you sure you want to proceed?"), yea=_("_Proceed"), nay=_("_Abort"), **kw):
        ui = cimarron.getEngine()
        nay = ui.Button(label=nay, stockImage="no", value=0)
        yea = ui.Button(label=yea, stockImage="ok", value=1)
        msg = ui.Label(label=message, useMarkup=True, lineWrap=True)
        image = ui.Image(fromStock=("dialog_warning", "dialog"))
        
        super(WarningDialog, self).__init__(message=msg,
                                            image=image,
                                            buttons=(nay, yea),
                                            default=nay,
                                            **kw
                                            )
    def run(self):
        return super(WarningDialog, self).run() == 1

class QuestionDialog(MsgDialog):
    __FIXME__=True
    def __init__(self, **kw):
        ui = cimarron.getEngine()
        msg = kw.pop('message', None) or \
              _("<big><b>You are about to do something strange or time-consuming.</b></big>\n\nAre you sure you want to proceed?")
        yea = kw.pop('yea', None) or _("_Proceed")
        nay = kw.pop('nay', None) or _("_Abort")
        nay = ui.Button(label=nay, stockImage="no", value=0)
        yea = ui.Button(label=yea, stockImage="ok", value=1)
        msg = ui.Label(label=msg, useMarkup=True, lineWrap=True)
        image = ui.Image(stock=("dialog_question", "dialog"))
        
        super(QuestionDialog, self).__init__(msg,
                                             image,
                                             buttons=(nay, yea),
                                             default=yea,
                                             **kw
                                             )
    def run(self):
        return super(QuestionDialog, self).run() == 1



if 0:        
    ui= cimarron.getEngine ()

    # stock button lists
    ok= ui.Button (stock='ok', value=True)
    cancel= ui.Button (stock='cancel', value=False)
    close= ui.Button (stock='close', value=0)
    yes= ui.Button (stock='yes', value=0)
    no= ui.Button (stock='no', value=0)
    stockOkCancel= [ok, cancel]
    stockOk= [ok]
    stockClose= [close]
    stockCancel= [cancel]
    stockYesNo= [yes, no]

    # types
    warning= 'WARNING'
    question= 'QUESTION'
    error= 'ERROR'
    info= 'INFO'
    def __init__ (self, title, type, message, buttons=stockOkCancel):
        contents= MsgDialog.ui.HBox ()
        icon= MsgDialog.ui.Image ()
        icon.fromStock ('STOCK_DIALOG_%s' % type, 'ICON_SIZE_DIALOG')
        contents.addChild (icon)
        contents.addChild (MsgDialog.ui.Label (label=message, useMarkup=True))
        super (MsgDialog, self).__init__ (title=title,
                                          contents=contents,
                                          buttons=buttons)
