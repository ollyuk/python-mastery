class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(', '.join('%s' % h for h in headers))

    def row(self, rowdata):
        print(', '.join('%s' % d for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<table>')
        print('<tr>' + ' '.join([f'<th>{col}</th>' for col in headers]) + '</tr>')

    def row(self, rowdata):
        print('<tr> ' + ' '.join([f'<td>{col}</td>' for col in rowdata]) + ' </tr>')


def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
