import configparser


IMG_TEMPLATE = \
    '<div style="width:{1}px;height:{1}px;position:absolute;left:{2}px;top:{3}px;" onclick="event.stopPropagation();" id="{4}"><img src="/static/{0}" style="width:{1}px;height:{1}px;pointer-events:none;"></div>\n'

def configLoader():
    loader = configparser.ConfigParser()
    loader.read('config.ini', encoding='utf-8')

    conf = dict()
    switches = dict()

    for s in loader.sections():
        section = dict(loader.items(s))
        conf.update(
            {
                s: dict(
                    x=int(section.get('x')),
                    y=int(section.get('y')),
                    size=int(section.get('size')),
                    key=int(section.get('key')),
                    ico=section.get('ico'),
                    mode=section.get('mode') # normal 普通; switch 切换
                )
            }
        )

        if section.get('mode') == 'switch':
            switches.update({s: 0})
    return conf, switches

def htmlGenerator(conf:dict[str, dict]):
    items = str()

    for c in conf:
        s = conf[c]
        item = IMG_TEMPLATE\
            .format(s.get('ico'), s.get('size'), s.get('x'), s.get('y'), c)
        items += item

    html = str()
    with open('default.html','r', encoding='utf-8') as f:
        html = f.read().replace('{{{0}}}', items)
        f.close()

    return html