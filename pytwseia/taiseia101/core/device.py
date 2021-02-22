
from pdu import *

import json
import sys
import logging
logger = logging.getLogger(__name__)


class DeviceTextCmdUtil(object):

    @classmethod
    def get_txt_cmd_with_service_code_name(cls, code_name):
        parts = code_name.split('_')[:-1]
        return '_'.join([part.lower() for part in parts])

    @classmethod
    def get_dev_text_cmd_dict(cls, dev_cls):
        """return { '$CmdTxt': '$ServiceClass'}"""
        cmds = {}
        dev_serv_code_cls = dev_cls.get_service_code_class()
        codes = dev_serv_code_cls.inspect_code_members()
        for code in codes:
            code_name = code[0]
            txt_cmd = cls.get_txt_cmd_with_service_code_name(code_name)
            cmds[txt_cmd] = {
                'txt': txt_cmd,
                'serv_id': code[1],
                'serv_cls_name': dev_cls.inspect_service_cls_name_with_code_name(code_name)
            }
        return cmds


class GeneralDevice(object):

    data_kind = None  # {id, name}
    dev_class = None  # {id, name}
    dev_version = None  # (major, minor)
    dev_type = None  # {id, name}
    dev_brand = None  # str
    dev_model = None  # str
    services = {}  # device registerr services { '$ServiceCode.text': '$ServiceClass'}
    # cmds = {}  # device class text cmds suppors { '$CmdTxt': '$ServiceClass'}

    class ServiceCode(BaseObject):
        POWER_RW = 0x00

    def __init__(self):
        # self.cmds = DeviceTextCmdUtil.get_dev_text_cmd_dict(self.__class__)
        pass

    def __str__(self):
        return '{}({} {})'.format(self.__class__.__name__, self.dev_brand, self.dev_model)

    def to_json(self):
        data = {
            'product': [self.dev_brand, self.dev_model],
            'version': self.dev_version,
            'class': self.dev_class,
            'data_kind': self.data_kind,
            'services': {}
        }
        for key, service in self.services.items():
            data['services'][key] = service.to_json()
        return data

    @classmethod
    def module_name(cls):
        return __name__

    @classmethod
    def get_service_code_class(cls):
        serv_code_cls = getattr(cls, 'ServiceCode', None)
        logger.debug('{} get_service_code_class {}'.format(cls.__name__, serv_code_cls))
        return serv_code_cls
        # raise Exception('{} must define its own ServiceCode class'.format(cls.__name__))

    @classmethod
    def parse_register_response_pdu(cls, register_pdu):
        logger.debug('{} parse_register_response_pdu'.format(cls.__name__))
        logger.debug('>> {}'.format(get_byte_list_hex_str(register_pdu)))
        register_resp = RegisterResponse(register_pdu)
        idx = 0
        serv_code_cls = cls.get_service_code_class()

        logger.debug('>> serv_code_cls {}'.format(serv_code_cls))
        logger.debug('>> register_resp.data_kind_code {}'.format(register_resp.data_kind_code))
        if register_resp.data_kind_code == RegisterResponse.DataKindCode.GENERAL:
            if cls is not GeneralDevice:
                while idx < len(register_resp.datas):
                    logger.debug('>> serv spec pdu {}'.format(
                        get_byte_list_hex_str(register_resp.datas[idx:idx+3])))
                    serv_pdu = [0x06, register_resp.dev_type_id] + register_resp.datas[idx:idx+3] + [0xff]
                    logger.debug('>> serv_pdu {}'.format(get_byte_list_hex_str(serv_pdu)))
                    service = DeviceBaseService(serv_pdu)
                    serv_name = serv_code_cls.text(service.service_id)
                    serv_cls_name = cls.inspect_service_cls_name_with_code_name(serv_name)
                    module_members = cls.inspect_module_cls_members()
                    # logger.debug('module cls members {}'.format(module_members))
                    results = module_members.get(serv_cls_name, None)
                    logger.debug('>> serv_cls: {}'.format(results))
                    if results:
                        service_cls = results[1]
                        register_resp.services[serv_name] = service_cls(serv_pdu)
                        # logger.debug('add service {}'.format(register_resp.services[serv_name].to_spec()))
                    else:
                        if cls is not GeneralDevice:
                            logger.warning('{} not implement ServiceCode {} function {}'.format(
                                cls.__name__, serv_name, serv_cls_name))
                    idx += 3
        else:
            # while idx < len(register_resp.datas):
            raise Exception('{} parse_register_response_pdu for '
                            'RegisterResponse.DataKindCode.MULTIPLE not implemented'.format(
                cls.__name__))

        logger.debug('>> return {}'.format(register_resp))
        return register_resp

    @classmethod
    def parse_response_pdu(cls, response_pdu):
        resp_obj = BaseResponse(response_pdu)
        if resp_obj.dev_type_id == DeviceTypeCode.REGISTER:
            resp_obj = cls.parse_register_response_pdu(response_pdu)
            cls.config_with_register_response(resp_obj)
        else:
            if resp_obj.service_id == 0x7f:
                resp_obj = ErrorResponse(response_pdu)
            else:
                serv_id = resp_obj.service_id
                cls_module_name = cls.module_name()
                _, serv_cls = cls.inspect_service_cls_with_code(cls_module_name, serv_id)
                logger.debug('inspect serv cls {}'.format(serv_cls.__name__))
                resp_obj = serv_cls(response_pdu)
                logger.debug('{} parse_response_pdu as {}'.format(
                    cls_module_name, resp_obj))

        return resp_obj
        # raise Exception('{} abstract function "parse_response_pdu" not implemented'.format(
        #     self.__class__.__name__))

    @classmethod
    def set_data_kind(cls, data_kind_id):
        cls.data_kind = {
            'id': data_kind_id,
            'name': RegisterResponse.DataKindCode.text(data_kind_id)
        }

    @classmethod
    def set_dev_class(cls, dev_class_id):
        cls.dev_class = {
            'id': dev_class_id,
            'name': RegisterResponse.DeviceClassCode.text(dev_class_id)
        }

    @classmethod
    def set_dev_version(cls, major, minor):
        cls.dev_version = (major, minor)

    @classmethod
    def set_dev_type(cls, dev_type_id):
        cls.dev_type = {
            'id': dev_type_id,
            'name': DeviceTypeCode.text(dev_type_id)
        }

    @classmethod
    def cmds(cls):
        return DeviceTextCmdUtil.get_dev_text_cmd_dict(cls)

    @classmethod
    def service_cmds(cls):
        serv_cmds = []
        ids = []
        for _, service in cls.services.items():
            ids.append(service.service_id)

        idx = []
        cls_cmds = cls.cmds()
        for txt, cmd in cls_cmds.items():
            if cmd['serv_id'] in ids:
                idx.append((cmd['serv_id'], txt))

        idx.sort(key=lambda x: x[0])

        for _, txt in idx:
            serv_cmds.append(cls_cmds[txt])
        return serv_cmds

    @classmethod
    def cmd_help(cls):
        lines = []
        for _, cmd in cls.cmds().items():
            lines.append((cmd['serv_id'], cmd['txt'], cmd['serv_cls_name']))
        lines.sort(key=lambda x: x[0])
        space_len = max([len(line[1]) for line in lines]) + 3
        return '\n'.join(['\t0x{:02x}\t{: <{}}{}'.format(
            line[0], line[1], space_len, line[2]) for line in lines])

    @classmethod
    def cmd_read_request(cls, cmd_txt):
        request = None
        dev_txt_cmds = DeviceTextCmdUtil.get_dev_text_cmd_dict(cls)
        cmd = dev_txt_cmds.get(cmd_txt, None)
        cls_module_name = cls.module_name()
        if cmd:
            serv_id = cmd.get('serv_id')
            serv_cls_name = cmd.get('serv_cls_name')
            _, service = cls.inspect_module_cls_with_cls_name(cls_module_name, serv_cls_name)
            request = BaseReadRequest(
                service_id=serv_id,
                dev_type_id=cls.dev_type['id'])
        logger.debug('cmd_read_request {} >> {}'.format(cmd_txt, request))
        return request

    @classmethod
    def cmd_write_request(cls, cmd_txt, args):
        request = None
        dev_txt_cmds = DeviceTextCmdUtil.get_dev_text_cmd_dict(cls)
        cmd = dev_txt_cmds.get(cmd_txt, None)
        cls_module_name = cls.module_name()
        if cmd:
            serv_id = cmd.get('serv_id')
            serv_cls_name = cmd.get('serv_cls_name')
            _, service = cls.inspect_module_cls_with_cls_name(cls_module_name, serv_cls_name)
            # logger.debug('{} cmd txt {} service {}'.format(cls.__name__, cmd_txt, service))
            try:
                value = int(args)
                low_byte = value & 0xff
                high_byte = (value & 0xff00) >> 16
                request = BaseWriteRequest(
                                            service_id=serv_id,
                                            dev_type_id=cls.dev_type['id'],
                                            high_byte=high_byte, low_byte=low_byte)
            except ValueError:
                logger.warning('{} cmd_write_request {} {} ValueError'.format(
                    cls.__name__, cmd_txt, args))
        logger.debug('cmd_write_request {} {} >> {}'.format(cmd_txt, args, request))
        return request

    @classmethod
    def cmd_request(cls, cmd_params_txt):
        """cmd_args = [cmd_name, arg1, arg2, ...]
        args means cmd_write_request,
        no args means cmd_read_request,
        """
        logger.debug('{} cmd_request {}'.format(cls.__name__, cmd_params_txt))
        args = cmd_params_txt.lower()
        args = args.split(',')
        if args[0] == 'register':
            request = RegisterRequest()
        else:
            if len(args) == 1:
                request = cls.cmd_read_request(args[0])
            else:
                request = cls.cmd_write_request(args[0], args[1])
        logger.debug('>> return {} '.format(request))
        return request

    def get_request_pdu(self, request_name='register'):
        func_name = 'get_pdu_' + request_name + '_request'
        logger.debug('{} get_request_pdu by func_name {}'.format(self.__class__.__name__, func_name))
        func_get_pdu = getattr(self, func_name, None)
        logger.debug('{} get_request_pdu by func_name {} result func {}'.format(
            self.__class__.__name__, func_name, str(func_get_pdu)))
        if func_get_pdu:
            return func_get_pdu()
        else:
            return func_get_pdu

    @classmethod
    def config_with_register_response(cls, reg_response):
        cls.set_data_kind(reg_response.data_kind_code)
        cls.set_dev_class(reg_response.dev_class_code)
        cls.set_dev_version(reg_response.major_ver, reg_response.minor_ver)
        cls.dev_brand = reg_response.dev_brand
        cls.dev_model = reg_response.dev_model
        cls.services = reg_response.services
        logger.debug('config_with_register_response:\n{}'.format(cls.device_detail()))

    @classmethod
    def device_detail(cls, cmd_check_serv=True):
        details = {
            'device': '{}'.format(cls.__name__),
            'brand': '{}'.format(cls.dev_brand),
            'model': '{}'.format(cls.dev_model),
            'services': [],
            'cmds': []
        }

        infos = []
        ids = []
        for _, service in cls.services.items():
            infos.append((service.service_id, service.to_spec()))
            ids.append(service.service_id)
        infos.sort(key=lambda x: x[0])
        for info in infos:
            details['services'].append('0x{:02x}: {}'.format(info[0], info[1]))

        lines = []
        for txt, cmd in cls.cmds().items():
            if cmd_check_serv:
                if cmd['serv_id'] in ids:
                    lines.append((cmd['serv_id'], txt, cmd['serv_cls_name']))
            else:
                lines.append((cmd['serv_id'], txt, cmd['serv_cls_name']))

        if len(lines) > 0:
            lines.sort(key=lambda x: x[0])
            space_len = max([len(line[1]) for line in lines]) + 3
        for line in lines:
            details['cmds'].append('0x{:02x}: {: <{}}{}'.format(
                line[0], line[1], space_len, line[2]))

        return json.dumps(details, indent=2)

    @classmethod
    def get_service_cls_name_by_text_cmd(cls, text_cmd):
        """find DeviceService name that matched with text_cmd"""
        serv_code_cls = cls.get_service_code_class()
        codes = serv_code_cls.inspect_code_members()
        for code in codes:
            service_code_name = code[0]
            code_txt_cmd = '_'.join([txt.lower() for txt in service_code_name.split('_')[:-1]])
            if code_txt_cmd == text_cmd:
                return cls.inspect_service_cls_name_with_code_name(service_code_name)
        return None

    @classmethod
    def inspect_service_code_with_serv_cls_name(cls, serv_cls_name):
        logger.debug('{} inspect_service_code_with_serv_cls_name {}'.format(
            cls.__name__, serv_cls_name))
        serv_code = None
        cmds = cls.cmds()
        for cmd in cls.cmds():
            if cmds.get(cmd).get('serv_cls_name') == serv_cls_name:
                serv_code = cmds.get(cmd).get('serv_id')
        logger.debug('>> return {}'.format(serv_code))
        return serv_code

    @classmethod
    def inspect_service_txt_cmd_with_serv_cls_name(cls, serv_cls_name):
        logger.debug('{} inspect_service_txt_cmd_with_serv_cls_name {}'.format(
            cls.__name__, serv_cls_name))
        txt_cmd = None
        cmds = cls.cmds()
        for cmd in cmds:
            if cmds.get(cmd).get('serv_cls_name') == serv_cls_name:
                txt_cmd = cmds.get(cmd).get('txt')
        logger.debug('>> return {}'.format(txt_cmd))
        return txt_cmd

    @classmethod
    def inspect_service_cls_with_code(cls, __name__, service_code):
        logger.debug('{} inspect_service_cls_with_code {} {}'.format(
            cls.__name__, __name__, service_code))
        serv_code_cls = cls.get_service_code_class()
        logger.debug('>> serv_code_cls {} '.format(serv_code_cls))
        code_name = serv_code_cls.text(service_code)
        logger.debug('>> code_name {}'.format(code_name))
        serv_cls_name = cls.inspect_service_cls_name_with_code_name(code_name)
        logger.debug('>> serv_cls_name {}'.format(serv_cls_name))
        serv_cls = cls.inspect_module_cls_with_cls_name(__name__, serv_cls_name)
        return serv_cls

    @classmethod
    def inspect_service_cls_name_with_code_name(cls, service_code_name):
        logger.debug('{} inspect_service_cls_name_with_code_name {}'.format(
            cls.__name__, service_code_name
        ))
        if type(service_code_name) is str:
            parts = service_code_name.split("_")
            name_append = 'Service' if parts[-1] == 'RW' else 'RService'
            name_body = ''.join(part[0].upper() + part[1:].lower() for part in parts[:-1])
            service_cls_name = 'Device{}{}'.format(name_body, name_append)
        else:
            service_cls_name = ErrorResponse
        logger.debug('>> return {}'.format(service_cls_name))
        return service_cls_name

    @classmethod
    def inspect_module_cls_with_cls_name(cls, __name__, cls_name):
        """check whether class exist in module __name__"""
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj):
                if name == cls_name:
                    return name, obj
        return 'DeviceBaseService', DeviceBaseService

    @classmethod
    def inspect_module_cls_members(cls):
        logger.debug('inspect_module_cls_members >>')
        members = {}
        cls_module_name = cls.module_name()
        for name, obj in inspect.getmembers(sys.modules[cls_module_name]):
            if inspect.isclass(obj):
                if name.find('__') != 0:
                    members[name] = (name, obj)
        logger.debug('>> {}'.format([name for name in members]))
        return members

    @classmethod
    def validate_service_code_with_module_service_cls(cls, __name__):
        """check if there is any device ServiceCode does not has corresponding service class implement"""
        validates = []
        serv_code_cls = cls.get_service_code_class()
        codes = serv_code_cls.inspect_code_members()
        for code in codes:
            cls_name = cls.inspect_service_cls_name_with_code_name(code[0])
            cls_member = cls.inspect_module_cls_with_cls_name(__name__, cls_name)
            if cls_member is None:
                logger.debug('code {} service class name {} not exist'.format(
                    code, cls_name))
                validates.append(code)
        return validates

    @classmethod
    def print_service_cls_template(cls):
        """print out device's service class according to its ServiceCode"""
        serv_code_cls = cls.get_service_code_class()
        codes = serv_code_cls.inspect_code_members()
        for code in codes:
            parts = code[0].split("_")
            name_append = 'Service' if parts[-1] == 'RW' else 'RService'
            name_body = ''.join(part[0].upper()+part[1:].lower() for part in parts[:-1])
            service_cls_name = 'Device{}{}'.format(name_body, name_append)
            sys.stdout.write("""
class {}(DeviceEnum16Service):
    # {} = {}
    pass
    
""".format(service_cls_name, code[0], '0x{:02x}'.format(code[1])))
