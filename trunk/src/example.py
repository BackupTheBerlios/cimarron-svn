#!/usr/bin/env python
# -*- python -*- coding: ISO-8859-1 -*-
import cimarron
import sys

class exampleWindowDelegate(object):
    def will_delete(self, window, args, delegate_args):
        app = window.getParent()
        windows = app.getChildren()
        if len(windows) > 1 and delegate_args == 1:
            return cimarron.Failed
        else:
            return cimarron.Accept

def main():
    eng=None
    if len(sys.argv) > 1:
        eng = sys.argv[1]
    cimarron.setEngine(eng)
    ui = cimarron.getEngine()
    app = ui.Application()
    win = ui.Window(parent=app,
                    title='Test Window')

    nbk = ui.Notebook(parent=win)

    vbox = ui.VBox()
    nbk.appendPage(child=vbox,
                   label='Why should tabs have short labels?')

    about = ui.Label(label=u'This example © 2004 the PAPO team')
    nbk.appendPage(child=about,
                   label='''What was the question again?''')

    misc_frame = ui.Frame(label='HBox',
                          borderWidth=4,
                          parent=vbox
                          )
    misc_hbox = ui.HBox(parent=misc_frame)

    image = ui.Image(parent=misc_hbox,
                     tip=u'Image')
    image.setFromStock('dialog_info', 'dialog')

    label = ui.Label(parent=misc_hbox,
                     tip=u'Label',
                     useMarkup=True,
                     label='<span size="xx-large"><b>A big, fat, label</b></span>')
    

    entry_frame = ui.Frame(parent=vbox,
                           label='VBox',
                           borderWidth=4)
    entry_hbox = ui.VBox(parent=entry_frame)
    tentry = ui.TextEntry(parent=entry_hbox,
                          tip='TextEntry')
    nentry = ui.NumEntry(parent=entry_hbox,
                         tip="NumEntry", range=(0, 100), increments=(1, 10))

    class DateModel (object):
        def __init__ (self, value=None):
            self.setValue (value)
        
        def setValue (self, value, *ignore):
            self._value= value

        def getValue (self, *ignore):
            return self._value
    dateModel= DateModel ()
            
    dentry = ui.DateEntry(parent=entry_hbox,
                          tip='DateEntry',
                          valueLoader= dateModel.getValue,
                          action= dateModel.setValue,
                          )

    bbox_frame = ui.Frame(parent=vbox,
                          label='HButtonBox',
                          borderWidth=4)
    bbox = ui.HButtonBox(parent=bbox_frame)
    b1 = ui.Button(image="/usr/share/pixmaps/other/Shout.png",
                   parent=bbox,
                   tip="button that pops up a dialog")
    b2 = ui.Button(label="another button",
                   parent=bbox,
                   tip="button")
    bb1 = ui.BoolEntry(parent=bbox,
                       label=u"a boolentry",
                       defaultValue=False,
                       tip="boolentry")
    bb2 = ui.BoolEntry(parent=bbox,
                       label=u"«inconsistent»\nboolentry",
                       tip="troolentry :)")

    leftButton = ui.Button(label=u'_Argh!', defaultValue=0)
    leftButton.setImage ('/usr/share/pixmaps/other/Shout.png')
    rightButton = ui.Button(label=u'_Muere, maldito!', defaultValue=1)
    msg = ui.WarningDialog(parent=win,
                           title=u'Bang! Bang! Estás liquidado...',
                           message=u'<big><b>Todos tus archivos han sido eliminados.</b></big>\n\nY ahora, ¿¡qué hacemos!?',
                           yea="_Seguir", nay="_Abandonar")

    def handler(*a):
        if msg.run():
            win.pushStatus('Siguiendo...', timeout=2, icon="error")
        else:
            win.pushStatus('Abandonando...', timeout=2, icon="warn")
    
    b1.setAction (handler)

    table = ui.Table(size=(3,3),
                     homogeneous=False,
                     parent=vbox)
    table.attach(ui.Button(label="1"),0,1,0,1)
    table.attach(ui.Button(label="2"),1,2,1,2)
    table.attach(ui.Button(label="3"),2,3,2,3)
 
    dlgt = exampleWindowDelegate()
    win.addDelegation(dlgt)
    win.pushStatus('Listo.')
    win.show()

    win2 = ui.Window(parent=app,
                     title='another window')
    l2 = ui.Label(label='Please close the other windows first',
                  parent=win2)
    win2.addDelegation(dlgt, 1)
    win2.show()

    app.run()


if __name__ == '__main__':
    main()
