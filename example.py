

from fixed_file.layout import Layout
from fixed_file.parse import FixedFile


layout = [
    Layout(1, 2, 'TIPREG', 'int'),
    Layout(3, 10, 'DATA DO PREGAO'),
    Layout(11, 12, 'CODBDI', 'int'),
    Layout(13, 24, 'CODNEG'),
    Layout(25, 27, 'TPMERC', 'int'),
    Layout(28, 39, 'NOMRES'),
    Layout(40, 49, 'ESPECI'),
    Layout(50, 52, 'PRAZOT'),
    Layout(53, 56, 'MODREF'),
    Layout(57, 69, 'PREABE', 'money'),
    Layout(70, 82, 'PREMAX', 'money'),
    Layout(83, 95, 'PREMIN', 'money'),
    Layout(96, 108, 'PREMED', 'money'),
    Layout(109, 121, 'PREULT', 'money'),
    Layout(122, 134, 'PREOFC', 'money'),
    Layout(135, 147, 'PREOFV', 'money'),
    Layout(148, 152, 'TOTNEG', 'int'),
    Layout(153, 170, 'QUATOT', 'int'),
    Layout(171, 188, 'VOLTOT', 'int'),
    Layout(189, 201, 'PREEXE', 'money'),
    Layout(202, 202, 'INDOPC', 'int'),
    Layout(203, 210, 'DATVEN'),
    Layout(211, 217, 'FATCOT'),
    Layout(218, 230, 'PTOEXE'),
    Layout(231, 242, 'CODISI'),
    Layout(243, 245, ),
]


fixed_file = FixedFile.read_text(
    'data/COTAHIST_A2021_AMZ.txt', layout=layout, ignore_index=[0, -1])

print(fixed_file.columns)
for row in fixed_file.data:
    print(row)

fixed_file.to_csv('data/amz.csv')