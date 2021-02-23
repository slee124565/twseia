class SmartApplication:

    def read_service(self, service_id):
        raise NotImplementedError

    def write_service(self, service_id, value):
        raise NotImplementedError


__all__ = [SmartApplication]
