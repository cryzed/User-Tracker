import hexchat


__module_name__ = 'User Tracker'
__module_description__ = "Monitors messages in joined channels and fakes a JOIN-event in case a message was received by a user that isn't in the userlist."
__module_version__ = '0.1'
__module_author__ = 'cryzed <cryzed@googlemail.com>'

RAW_JOIN_COMMAND_TEMPLATE = 'RECV :{0} JOIN {1}'


def join(identity, channel, context=hexchat):
    command = RAW_JOIN_COMMAND_TEMPLATE.format(identity, channel, channel)
    context.command(command)


def callback(word, word_eol, userdata):
    identity = word[0][1:]
    nickname = identity.split('!', 1)[0]
    users = hexchat.get_list('users')

    if not nickname in [user.nick for user in users]:
        channel = word[2]
        join(identity, channel)

    return hexchat.EAT_NONE


def main():
    hexchat.hook_server('PRIVMSG', callback)


if __name__ == '__main__':
    main()
