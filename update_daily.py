# -*- coding: utf-8 -*-
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from secwiki_today import scraw as secwiki_scraw
from xuanwu_today import scraw as xuanwu_scraw
from mills import SQLiteOper
from mills import get_special_date
import visual


def scraw(proxy=None):
    """

    :return:
    """

    so = SQLiteOper("data/scrap.db")

    secwiki_scraw(so, proxy=proxy, delta=10)

    xuanwu_scraw(so, proxy=proxy, delta=10)


def update_github():
    """

    :return:
    """
    ts = get_special_date(format="%Y-%m-%d %H:%m:%S")
    cmd = "git add . && git commit -m '%s' && git push origin master" % (ts)

    ret = os.system(cmd)
    if ret != 0:
        print "%s failed" % cmd


if __name__ == "__main__":
    """
    """
    proxy = {
        "socks:": "socks://127.0.0.1:8420",

    }
    proxy = None

    scraw(proxy=proxy)

    visual.draw_readme()

    update_github()
