"""Complete binary NBT identity; only native entity Attributes maps are unordered.

Primitive bit patterns/tag types, unknown fields, array bytes and every other
list order remain exact. Raw original records are never rewritten.
"""
import base64
import struct


class Reader:
    def __init__(self, data):
        self.data, self.offset = data, 0

    def take(self, count):
        if count < 0 or self.offset + count > len(self.data):
            raise ValueError('Incomplete binary NBT observation')
        value = self.data[self.offset:self.offset + count]
        self.offset += count
        return value

    def number(self, pattern):
        return struct.unpack(pattern, self.take(struct.calcsize(pattern)))[0]

    def text(self):
        # Retain exact native modified-UTF bytes, including surrogate/code-unit
        # choices, rather than recoding imported strings or normalizing text.
        return self.take(self.number('>H'))

    def tag(self, kind, depth=0):
        if depth > 128:
            raise ValueError('NBT depth exceeds the owned evidence budget')
        if kind in (1, 2, 3, 4, 5, 6):
            return kind, self.take({1: 1, 2: 2, 3: 4, 4: 8, 5: 4, 6: 8}[kind])
        if kind in (7, 11, 12):
            count = self.number('>i')
            if count < 0:
                raise ValueError('Negative native NBT array size')
            return kind, self.take(count * {7: 1, 11: 4, 12: 8}[kind])
        if kind == 8:
            return kind, self.text()
        if kind == 9:
            element, count = self.number('>B'), self.number('>i')
            if count < 0 or count > len(self.data) or (element == 0 and count):
                raise ValueError('Invalid native NBT list contract')
            return kind, (element, tuple(self.tag(element, depth + 1) for _ in range(count)))
        if kind == 10:
            values = {}
            while True:
                element = self.number('>B')
                if element == 0:
                    return kind, values
                name = self.text()
                if name in values:
                    raise ValueError('Ambiguous duplicate native NBT compound field')
                values[name] = self.tag(element, depth + 1)
        raise ValueError('Unknown native binary NBT tag type')


def decode(encoded):
    reader = Reader(base64.b64decode(encoded, validate=True))
    kind, name = reader.number('>B'), reader.text()
    if kind != 10:
        raise ValueError('Entity persistence root was not a compound')
    value = reader.tag(kind)
    if reader.offset != len(reader.data):
        raise ValueError('Native binary NBT contains unobserved trailing bytes')
    return name, value


def entity_identity(tag):
    if tag[0] != 10:
        raise ValueError('Entity/passenger persistence was not a compound')
    values = dict(tag[1])
    if b'Attributes' in values:
        attributes = values[b'Attributes']
        if attributes[0] != 9 or attributes[1][0] not in (0, 10):
            raise ValueError('Native named attribute map was not a compound list')
        named = {}
        for attribute in attributes[1][1]:
            if attribute[0] != 10:
                raise ValueError('Native attribute was not a compound')
            name = attribute[1].get(b'Name')
            if not name or name[0] != 8 or not name[1] or name[1] in named:
                raise ValueError('Missing/ambiguous native attribute identity')
            named[name[1]] = attribute
        values[b'Attributes'] = 9, (attributes[1][0], tuple(named[key] for key in sorted(named)))
    if b'Passengers' in values:
        passengers = values[b'Passengers']
        if passengers[0] != 9 or passengers[1][0] not in (0, 10):
            raise ValueError('Native passengers were not a compound list')
        values[b'Passengers'] = 9, (passengers[1][0], tuple(entity_identity(row) for row in passengers[1][1]))
    return 10, values


def equal(before, after):
    left, right = decode(before), decode(after)
    return left[0] == right[0] and entity_identity(left[1]) == entity_identity(right[1])


if __name__ == '__main__':
    import json
    import sys
    from pathlib import Path
    receipt = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    for row in receipt['rows']:
        if equal(row['beforeBinary'], row['afterBinary']) != row['equal']:
            raise ValueError('Independent typed NBT comparison disagrees: ' + row['key'])
    print(json.dumps(dict(passed=True, completeRealEntities=receipt['completeRealEntities'],
                         generatedControls=sum(row['synthetic'] for row in receipt['rows']),
                         scope='Full native binary NBT comparison; no field/type/list-order loss')))
