class LeftParagraph:
    def __init__(self, width: int):
        self.width = width
        self.lines = []
        self.line = ''

    def add_word(self, word):
        if self.line:
            if len(self.line + ' ' + word) <= self.width:
                self.line += ' ' + word
            else:
                self.lines.append(self.line)
                self.line = word
        else:
            self.line += word

    def end(self):
        print('\n'.join(self.lines))


class RightParagraph:
    def __init__(self, width: int):
        self.width = width
        self.lines = []
        self.line = ''

    def add_word(self, word):
        if self.line:
            if len(self.line + ' ' + word) <= self.width:
                self.line += ' ' + word
            else:
                self.lines.append(self.line)
                self.line = word
        else:
            self.line += word

    def end(self):
        print('\n'.join(i.rjust(self.width, ' ') for i in self.lines))


if __name__ == '__main__':
    pass
