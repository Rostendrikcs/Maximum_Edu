#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def counter(string):
    for i in set(string):
        c = 0
        for e in string:
            if i == e:
                c += 1
        print(i, c)
counter('abbc')


# In[ ]:


def counter(string):
    el = {}
    for i in string:
        el[i] = el.get(i, 0) + 1
    for e, c in el.items():
        print(e, c)
counter('abbc')

