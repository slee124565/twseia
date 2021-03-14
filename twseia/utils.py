import enum


def compute_pdu_checksum(pdu: list):
    # todo: move to twseia.packets module
    if not isinstance(pdu, list):
        raise ValueError(f'pdu is not list, {pdu}')
    _checksum = 0
    for x in list(pdu):
        _checksum ^= x
    return _checksum


def append_checksum(pdu: list) -> list:
    _pdu = list(pdu)
    _checksum = 0
    for x in list(_pdu):
        _checksum ^= x
    _pdu.append(_checksum)
    return _pdu


def convert_enum_to_value_list(enum_type):
    if isinstance(enum_type, enum.EnumMeta):
        return [e.value for e in list(enum_type)]
    else:
        raise Exception(f'Object class type invalid, {type(enum_type)}')


__all__ = ['append_checksum', 'compute_pdu_checksum', 'convert_enum_to_value_list']
