"""No-access smoke probe; not an authentication or Mac worker integration."""

def probe(args="", *, session_key=None, **_context):
    if type(args) is not str or len(args) > 64 or args.strip():
        return "Usage: /sdm-mac-probe (no arguments)"
    if type(session_key) is not str or not session_key or len(session_key) > 512:
        return "SDM probe: no usable session context; Mac not contacted."
    return "SDM probe: command ran with session context; Mac not contacted."

def register(ctx):
    ctx.register_command("sdm-mac-probe", probe, "Check the synthetic cloud command. No device access.")
