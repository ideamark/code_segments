from tkinter import *
import Pmw

eventDict = {
    '2':'KeyPress', '3':'KeyRelease', '4':'ButtonPress',
    '5':'ButtonRelease', '6':'Motion', '7':'Enter', 
    '8':'Leave', '9':'FocusIn', '10':'FocusOut', 
    '12':'Expose', '15':'Visibility', '17':'Destroy', 
    '18':'Unmap', '19':'Map', '21':'Reparent', 
    '22':'Configure', '24':'Gravity', '26':'Circulate', 
    '28':'Property', '32':'Colormap', '36':'Activate', 
    '37':'Deactivate', 
}

def reportEvent(event):
    rpt = '\n\n%s' % (80*'=')
    rpt = '%s\nEvent: type=%s (%s)' % (rpt, event.type, eventDict.get(event.type, 'Unknown'))
    rpt = '%s\ntime=%s' % (rpt, event.time)
    rpt = '%s widget=%s' % (rpt, event.widget)
    rpt = '%s x=%s,y=%s' % (rpt, event.x, event.y)
    rpt = '%s x_root=%s, y_root=%s' % (rpt, event.x_root, event.y_root)
    rpt = '%s y_root=%s' % (rpt, event.y_root)
    rpt = '%s\nserial=%s' % (rpt, event.serial)
    rpt = '%s num=%s' % (rpt, event.num)
    rpt = '%s height=%s' % (rpt, event.height)
    rpt = '%s width=%s' % (rpt, event.width)
    rpt = '%s keysym=%s' % (rpt, event.keysym)
    rpt = '%s ksNum=%s' % (rpt, event.keysym_num)

    #### Some event types don't have these attributes
    try:
        rpt = '%s focus=%s' % (rpt, event.focus)
    except:
        try:
            rpt = '%s send=%s' % (rpt, event.send_event)
        except:
            pass

    text2.yview(END)
    text2.insert(END, rpt)

root = Tk()
frame = Frame(root, takefocus=1, highlightthickness=2)
text = Entry(frame, width=10, takefocus=1, highlightthickness=2)
text2 = Pmw.ScrolledText(frame)

for event in eventDict.values():
    frame.bind('<%s>' % event, reportEvent)
    text.bind('<%s>' % event, reportEvent)

text.pack()
text2.pack(fill=BOTH, expand=YES)
frame.pack()
text.focus_set()
root.mainloop()
