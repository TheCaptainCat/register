class Escape:
    @property
    def escaped_chars(self):
        return {
            '*': '&#42;',
            ']': '&#91;',
            '\\': '&#92;',
            '[': '&#93;',
            '^': '&#94;',
            '_': '&#95;',
        }

    def escape_line(self, line):
        chars = self.escaped_chars
        i = 0
        while i < len(line) - 1:
            if line[i] == '\\' and line[i + 1] in chars.keys():
                escaped = chars[line[i + 1]]
                line = line[:i] + escaped + line[i+2:]
                i += len(escaped)
            i += 1
        return line
