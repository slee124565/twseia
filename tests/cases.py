#
# from django.test import SimpleTestCase
#
# import dehumidifier  # import Dehumidifier
# import airconditioner
# import fan
# from general import GeneralDevice
# from general import RegisterResponse
# from general import ErrorResponse
#
# import json
# import logging
# logger = logging.getLogger(__name__)
#
# DEVICES = [
#     {
#         'cls': dehumidifier.Dehumidifier,
#         'pdu': {
#             'DeviceRegisterResponse':
#                 '45,00,00,04,00,03,00,04,50,61,6e,61,73,6f,6e,69,63,00,'
#                 '46,59,54,57,2d,30,35,37,36,30,31,32,31,00,80,00,03,81,'
#                 '00,7f,82,00,0c,84,00,06,07,00,00,89,00,0f,0a,00,00,8d,'
#                 '00,03,8e,00,0f,12,00,00,98,00,03,9d,00,00,d6',
#             'Services': [
#                 ('06,04,00,00,00,02', dehumidifier.DevicePowerService),
#                 ('06,04,00,00,01,03', dehumidifier.DevicePowerService),
#                 ('0x06, 0x04, 0x82, 0x00, 0x0c, 0x8c', dehumidifier.DeviceOpTimerService),
#                 ('0x06, 0x04, 0x82, 0xff, 0xff, 0x80', dehumidifier.DeviceOpTimerService),
#                 ('0x06, 0x04, 0xff, 0xff, 0xff, 0xfd', ErrorResponse),
#             ],
#         }
#     },
#     {
#         'cls': airconditioner.AirConditioner,
#     },
#     {
#         'cls': fan.Fan,
#     },
# ]
#
#
# class ValidateDeviceTextCmdUtil(SimpleTestCase):
#
#     def test_util_get_txt_cmd_with_service_code_name(self):
#         pass
#
#     def test_util_get_dev_text_cmd_dict(self):
#         pass
#
#
# class ValidateGeneralDeviceImplement(SimpleTestCase):
#
#     def test_general_dev_cls_imple_parse_register_response_pdu(self):
#         for dev in DEVICES:
#             dev_cls = GeneralDevice
#             pdu_hex = dev.get('pdu').get('DeviceRegisterResponse')
#             pdu = [int(n, 16) for n in pdu_hex.split(',')]
#             response = dev_cls.parse_response_pdu(pdu)
#             # logger.debug('device {} register response parsing {}'.format(dev_cls.__name__, response))
#             self.assertEquals(
#                 True, isinstance(response, RegisterResponse),
#                 'dev class GeneralDevice parse_register_response_pdu for device {} error'.format(
#                     dev_cls.__name__))
#
#     def test_dev_cls_imple_parse_register_response_pdu(self):
#         # logger.debug('\n=== test_dev_cls_imple_parse_register_response_pdu ===\n')
#         for dev in DEVICES:
#             dev_cls = dev.get('cls')
#             pdu_hex = dev.get('pdu').get('DeviceRegisterResponse')
#             pdu = [int(n, 16) for n in pdu_hex.split(',')]
#             response = dev_cls.parse_response_pdu(pdu)
#             # logger.debug('device {} register response parsing {}'.format(dev_cls.__name__, response))
#             self.assertEquals(
#                 True, isinstance(response, RegisterResponse),
#                 'dev class {} parse_register_response_pdu error'.format(dev_cls.__name__))
#         # logger.debug('\n=== test_dev_cls_imple_parse_register_response_pdu ===\n')
#
#     def test_dev_obj_imple_device_detail(self):
#         for dev in DEVICES:
#             dev_cls = dev.get('cls')
#             pdu_hex = dev.get('pdu').get('DeviceRegisterResponse')
#             pdu = [int(n, 16) for n in pdu_hex.split(',')]
#             register_response = dev_cls.parse_response_pdu(pdu)
#             dev_obj = dev_cls()
#             dev_obj.config_with_register_response(register_response)
#             dev_details = dev_obj.device_detail()
#             logger.debug('{} device details\n{}'.format(dev_cls.__name__, dev_details))
#             self.assertNotEqual(dev_details, '')
#
#     def test_dev_cls_cmd_help(self):
#         for dev in DEVICES:
#             dev_cls = dev.get('cls')
#             cmd_help = dev_cls.cmd_help()
#             self.assertNotEqual(cmd_help, '')
#
#
# class ValidateDeviceTemplateImplement(SimpleTestCase):
#
#     def test_dev_cls_get_service_code_class(self):
#         for dev in DEVICES:
#             dev_cls = dev.get('cls')
#             serv_code_cls = dev_cls.get_service_code_class()
#             logger.debug('device {} get_service_code_class {}'.format(
#                 dev_cls.__name__, serv_code_cls))
#             members = serv_code_cls.inspect_code_members()
#             members.sort(key=lambda x: x[1])
#             logger.debug('code members: {}'.format(members))
#             self.assertEquals(serv_code_cls, dev_cls.ServiceCode)
#
#     def test_dev_cls_imple_inspect_module_cls_members(self):
#         for dev in DEVICES:
#             dev_cls = dev.get('cls')
#             members = dev_cls.inspect_module_cls_members()
#             self.assertNotEqual(len(members), 0,
#                                 '{} classmethod inspect_module_cls_members not implemented'.format(
#                                     self.__class__.__name__
#                                 ))
#
#
# class ValidateDevicePduParsingImplement(SimpleTestCase):
#
#     def test_dev_cls_imple_parse_response_pdu(self):
#         logger.debug('\n=== test_dev_cls_imple_parse_response_pdu ===\n')
#         for dev in DEVICES:
#             dev_cls = dev.get('cls')
#             datas = dev.get('pdu').get('Services')
#             self.assertNotEqual(len(datas), 0)
#             for pdu_hex, target_cls in datas:
#                 # logger.debug('test pdu hex {}'.format(pdu_hex))
#                 pdu = [int(n, 16) for n in pdu_hex.split(',')]
#                 response = dev_cls.parse_response_pdu(pdu)
#                 logger.debug('response {}'.format(response))
#                 logger.debug('\n{}'.format(json.dumps(response.to_json(), indent=2)))
#                 self.assertEqual(
#                     isinstance(response, target_cls), True,
#                     'GeneralDevice parse_response_pdu for device {} error'.format(
#                         target_cls.__name__))
#         logger.debug('\n=== test_dev_cls_imple_parse_response_pdu ===\n')
#
#     def test_dev_cls_imple_cmd_read_request(self):
#         for dev in DEVICES:
#             dev_cls = dev.get('cls')
#             cls_cmds = dev_cls.cmds()
#             for txt_cmd in cls_cmds:
#                 request = dev_cls.cmd_request(txt_cmd)
#                 self.assertNotEqual(request, None)
#
#     def test_dev_cls_imple_cmd_write_request(self):
#         for dev in DEVICES:
#             dev_cls = dev.get('cls')
#             checked = getattr(dev_cls, 'cmd_write_request', None)
#             if checked:
#                 cls_cmds = dev_cls.cmds()
#                 for txt_cmd in cls_cmds:
#                     check_str = 'RService'
#                     serv_name = cls_cmds.get(txt_cmd).get('serv_cls_name')
#                     if serv_name[-len(check_str):] != check_str:
#                         request = dev_cls.cmd_request('{},0'.format(txt_cmd))
#                         self.assertNotEqual(request, None)
