def trim_strongholds(strongholds):
    if strongholds:
        del strongholds[0]
    del strongholds[-2:]
    return strongholds
