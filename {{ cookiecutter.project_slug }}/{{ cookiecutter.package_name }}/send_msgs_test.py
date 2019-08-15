#!/usr/bin/env python
from event_service_utils.streams.redis import RedisStreamFactory
from event_service_utils.schemas.internal_msgs import (
    BaseInternalMessage,
)


from {{ cookiecutter.package_name }}.conf import (
    REDIS_ADDRESS,
    REDIS_PORT,
    SERVICE_STREAM_KEY,
    SERVICE_CMD_KEY,
)


def make_dict_key_bites(d):
    return {k.encode('utf-8'): v for k, v in d.items()}


def new_action_msg(action, event_data):
    schema = BaseInternalMessage(action=action)
    schema.dict.update(event_data)
    return schema.json_msg_load_from_dict()


def send_msgs(service_stream):
    msg_1 = new_action_msg(
        'someAction',
        {
            'some': 'event',
            'data': 'to be used'
        }
    )
    msg_2 = new_action_msg(
        'someOtherAction',
        {
            'some': 'other event',
            'data': 'to be used'
        }
    )

    import ipdb; ipdb.set_trace()
    print(f'Sending msg {msg_1}')
    service_stream.write_events(msg_1)
    print(f'Sending msg {msg_2}')
    service_stream.write_events(msg_2)


def main():
    stream_factory = RedisStreamFactory(host=REDIS_ADDRESS, port=REDIS_PORT)
    service_stream = stream_factory.create(SERVICE_STREAM_KEY, stype='streamOnly')
    send_msgs(service_stream)


if __name__ == '__main__':
    main()
