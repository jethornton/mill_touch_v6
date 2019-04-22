from functools import partial

from qtpyvcp.plugins import getPlugin

def errorSetup(parent):

    parent.nChannel = getPlugin("notifications")
    #parent.nChannel.info_message.notify(partial(threadFormFwd, parent))
    #parent.nChannel.warn_message.notify(partial(threadFormFwd, parent))
    #parent.nChannel.debug_message.notify(partial(threadFormFwd, parent))
    parent.nChannel.error_message.notify(partial(errorMsg, parent))

def errorMsg(parent, message):
    #print(message)
    parent.errorList.insertItem(0, message)





