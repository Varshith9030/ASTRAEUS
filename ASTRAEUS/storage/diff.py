def diff_scans(old, new):
    old_ids = {f["title"] for f in old}
    new_ids = {f["title"] for f in new}

    return {
        "new": list(new_ids - old_ids),
        "fixed": list(old_ids - new_ids),
        "persistent": list(old_ids & new_ids)
    }
