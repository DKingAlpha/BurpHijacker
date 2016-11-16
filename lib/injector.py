import json
from urllib import quote,unquote, urlencode
from base64 import b64encode as base64encode, b64decode as base64decode
import random

#args is Dict

#Judge whether a package is the target that youd like to modify.
def request_match(header,post,args):
    for i in header:
        if i.startswith(args['FLAG']):
            return True
    if post.startswith(args['FLAG']):
        return True
    else:
        return False


#header is a list 
def modifyheader(header,args):
    new_header = []
    for i in header:
        # handle with i (each line of header)
        if i.startswith('Accept-Language'):
            i = i.replace('zh-CN,','')
        new_header.append(i)
    return new_header


#post here is a string
def modifypost(post,args):
    newpost = unquote(post)        # %20 = >' '
    # newpost = newpost.split('&')
    # post_dict={}
    # for i in newpost:
        # tmp = i.split('=')
        # try:
            # post_dict[tmp[0]] = tmp[1]     #operation here
        # except:
            # pass
        # ##newpost = modifyjson(newpost,args)    #json
    # newpost = urlencode(post_dict)
    ##newpost=modifyjson(newpost,args)
    newpost=quote(newpost,'&=')
    return newpost



#alternative function to handle with JSON data,especially complicated ones.
#jsonpara are supposed to be a string like 
#"{'a':a,'b',b},{'c':'c,'d':'d'}"
def modifyjson(jsonpara,args):
    jsoncode = json.loads(jsonpara)
    #jscode[0]['date']['datenow']
    for item in jsoncode:
        item['id'] = str('test')
    return json.dumps(jsoncode)

