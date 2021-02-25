def compute_pdu_checksum(pdu: list):
    if not isinstance(pdu, list):
        raise ValueError(f'pdu is not list, {pdu}')
    _checksum = 0
    for x in pdu:
        _checksum ^= x
    return _checksum
