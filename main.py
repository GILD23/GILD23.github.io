__plugin_name__ = "SimplePlugin"
__plugin_version__ = "0.2-dev"

@hook.enable
def onEnable():
    print "saemple plugin enabled"

@hook.disable
def onDisable():
    print "saemple plugin disabled"

@hook.event("player_join", "normal")
def onPlayerJoin(event):
    msg = "welcome from the sample plugin, %s" % event.getPlayer().getName()
    print msg
    event.getPlayer().sendMessage(msg)

@hook.command("samplecommand", usage="/<command>", 
                desc="send a sample message")
def onSampleCommand(sender, command, label, args):
    msg = "sample plugin command"
    print msg
    sender.sendMessage(msg)
    return True

print "sample plugin main file run"