def after_scenario(context, sceario):
    if not hasattr(context, 'cli_child'):
        return

    context.cli_child.sendline('exit\nexit\nexit\n')
