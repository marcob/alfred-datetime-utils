#!/usr/bin/python
# encoding: utf-8

import sys
from datetime import datetime
from time import mktime
from workflow import Workflow

class Item(object):
    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle

def main(wf):
    if not len(wf.args):
        return

    args = wf.args

    try:
        epoch_to_date(float(args[0]))
    except ValueError:
        string_to_date(args[0])
        pass

    wf.send_feedback()

def string_to_date(arg):
    import parsedatetime as pdt
    c = pdt.Constants()
    c.BirthdayEpoch = 80
    p = pdt.Calendar(c)
    date_struct,flag = p.parse(arg)

    if flag == 0:
        return

    epoch_ts = mktime(date_struct)
    d = datetime.fromtimestamp(epoch_ts)

    add_items([Item(str(epoch_ts), u'epoch'), Item(str(d), u'datetime'), Item(str(d.date()), u'date'), Item(str(d.time()), u'time')])


def epoch_to_date(epoch_time):
    d = datetime.fromtimestamp(epoch_time)

    add_items([Item(str(d), u'datetime'), Item(str(d.date()), u'date'), Item(str(d.time()), u'time')])


def add_items(items):
    for item in items:
        wf.add_item(title = item.title, subtitle = item.subtitle, valid = True, arg = item.title, copytext = item.title)
if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
