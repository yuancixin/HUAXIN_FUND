# coding=UTF-8
'''
Created on 2018年11月26日

@author: wanglx
'''
"""
单个合约代码
"""
"""郑州"""
ZCE_CODE = ['CF 01', 'CF 05', 'CF 09', 'RM 01', 'RM 05', 'RM 09', 'RM 11', 'ZC 01', 'ZC 03', 'ZC 05', 
            'ZC 07', 'ZC 09', 'ZC 11', 
            'WH 01', 'WH 05', 'WH 09', 'MA 01', 'MA 05', 'MA 09', 'SF 01', 'SF 05', 'SF 09', 'SM 01',
            'SM 05', 'SM 09', 'TA 01', 'TA 03', 'TA 05', 'TA 07', 'TA 09', 'TA 11', 'AP 01', 'AP 02', 'AP 03',
            'AP 05', 'AP 07', 'AP 10', 'AP 11', 'AP 12', 'FG 01',
            'FG 05', 'FG 09', 'OI 01', 'OI 05', 'OI 09', 'SR 01', 'SR 05', 'SR 09']

"""大连"""
DCE_CODE = ['C 01' , 'C 03' , 'C 05' , 'C 09' , 'M 01' , 'M 03' , 'M 05' , 'M 09' , 'M 11' , 'JD 01', 'JD 02',
            'JD 03', 'JD 04', 'JD 05', 'JD 08', 'JD 10', 'JD 11', 'JD 12', 'JD 09', 'J 01' , 'J 05' ,
            'J 09' , 'JM 01', 'JM 05', 'JM 09', 'I 01' , 'I 03 ', 'I 05' , 'I 09' , 'PP 01', 'PP 05', 'PP 09',
            'L 01' , 'L 05' , 'L 09' , 'V 01' , 'V 05' , 'V 09' , 'A 01' , 'A 05' , 'A 09' , 'B 01' ,
            'B 05' , 'B 09' , 'P 01' , 'P 05' , 'P 09' , 'CS 01', 'CS 05', 'CS 09', 'Y 01' , 'Y 05' ,
            'Y 09' , 'EG 01', 'EG 05', 'EG 09']

"""上海"""
SHF_CODE = ['RU 01', 'RU 05', 'RU 09', 'RB 01', 'RB 05', 'RB 10', 'CU 01', 'CU 02', 'CU 03', 'CU 04',
            'CU 05', 'CU 06', 'CU 07', 'CU 08', 'CU 09', 'CU 10', 'CU 11', 'CU 12', 'AL 01', 'AL 02',
            'AL 03', 'AL 04', 'AL 05', 'AL 06', 'AL 07', 'AL 08', 'AL 09', 'AL 10', 'AL 11', 'AL 12',
            'NI 01', 'NI 02', 'NI 03', 'NI 04', 'NI 05', 'NI 06',
            'NI 07', 'NI 08', 'NI 09', 'NI 10', 'NI 11', 'NI 12', 'SN 01', 'SN 05', 'SN 09', 'AU 12',
            'AU 06', 'AG 12', 'AG 06', 'HC 01', 'HC 05', 'HC 10', 'FU 01', 'FU 05',
            'FU 09', 'BU 01', 'BU 06', 'BU 09', 'BU 12', 'SP 09', 'SP 06']

"""
一一倍合约组合代码
"""
CODE_COMBINATION = [['CF 01', 'CF 05'], ['CF 05', 'CF 09'], ['CF 01', 'CF 09'], ['RM 01', 'RM 05'], ['RM 05', 'RM 09'],
                    ['RM 01', 'RM 09'], ['ZC 01', 'ZC 05'], ['ZC 05', 'ZC 09'], ['ZC 01', 'ZC 09'], ['WH 01', 'WH 05'],
                    ['WH 05', 'WH 09'], ['WH 01', 'WH 09'], ['MA 01', 'MA 05'], ['MA 05', 'MA 09'], ['MA 01', 'MA 09'],
                    ['SF 01', 'SF 05'], ['SF 05', 'SF 09'], ['SF 01', 'SF 09'], ['SM 01', 'SM 05'], ['SM 05', 'SM 09'],
                    ['SM 01', 'SM 09'], ['TA 01', 'TA 05'], ['TA 05', 'TA 09'], ['TA 01', 'TA 09'], ['AP 01', 'AP 05'],
                    ['AP 05', 'AP 09'], ['AP 01', 'AP 09'], ['FG 01', 'FG 05'], ['FG 05', 'FG 09'], ['FG 01', 'FG 09'],
                    ['OI 01', 'OI 05'], ['OI 05', 'OI 09'], ['OI 01', 'OI 09'], ['SR 01', 'SR 05'], ['SR 05', 'SR 09'],
                    ['SR 01', 'SR 09'], ['C 01' , 'C 05' ], ['C 01' , 'C 09' ], ['C 05' , 'C 09' ], ['M 01' , 'M 05' ],
                    ['M 01' , 'M 09' ], ['M 05' , 'M 09' ], ['JD 01', 'JD 05'], ['JD 05', 'JD 09'], ['JD 01', 'JD 09'],
                    ['J 01' , 'J 05' ], ['J 01' , 'J 09' ], ['J 05' , 'J 09' ], ['JM 01', 'JM 05'], ['JM 01', 'JM 09'],
                    ['JM 05', 'JM 09'], ['I 01' , 'I 05' ], ['I 01' , 'I 09' ], ['I 05' , 'I 09' ], ['PP 01', 'PP 05'],
                    ['PP 01', 'PP 09'], ['PP 05', 'PP 09'], ['L 01' , 'L 05' ], ['L 01' , 'L 09' ], ['L 05' , 'L 09' ],
                    ['V 01' , 'V 05' ], ['V 01' , 'V 09' ], ['V 05' , 'V 09' ], ['A 01' , 'A 05' ], ['A 01' , 'A 09' ],
                    ['A 05' , 'A 09' ], ['B 01' , 'B 05' ], ['B 01' , 'B 09' ], ['B 05' , 'B 09' ], ['P 01' , 'P 05' ],
                    ['P 01' , 'P 09' ], ['P 05' , 'P 09' ], ['CS 01', 'CS 05'], ['CS 01', 'CS 09'], ['CS 05', 'CS 09'],
                    ['RU 01', 'RU 05'], ['RU 05', 'RU 09'], ['RU 01', 'RU 09'], ['RB 01', 'RB 05'], ['RB 05', 'RB 09'],
                    ['RB 01', 'RB 09'], ['L 01' , 'PP 01'], ['L 05' , 'PP 05'], ['L 09' , 'PP 09'], ['L 01' , 'V 01' ],
                    ['L 05' , 'V 05' ], ['L 09' , 'V 09' ], ['P 01' , 'M 01' ], ['P 05' , 'M 05' ], ['P 09' , 'M 09' ],
                    ['SM 01', 'SF 01'], ['SM 05', 'SF 05'], ['SM 09', 'SF 09'], ['M 01' , 'C 01' ], ['M 05' , 'C 05' ],
                    ['M 09' , 'C 09' ], ['EG 01', 'EG 05'], ['EG 05', 'EG 09'], ['EG 01', 'EG 09'], ['TA 01', 'EG 01'],
                    ['TA 05', 'EG 05'], ['TA 09', 'EG 09'], ['OI 01', 'P 01' ], ['OI 05', 'P 05' ], ['OI 09', 'P 09' ],
                    ['M 01' , 'RM 01'], ['M 05' , 'RM 05'], ['M 09' , 'RM 09'], ['A 01' , 'M 01' ], ['A 05' , 'M 05' ],
                    ['A 09' , 'M 09' ]]

"""
一二倍合约组合代码
"""
CODE_COMBINATION2 = [['P 01' , 'M 01' ], ['P 05' , 'M 05' ], ['P 09' , 'M 09' ], ['Y 01' , 'M 01' ], ['Y 05' , 'M 05' ], 
                     ['Y 09' , 'M 09' ], ['OI 01', 'RM 01'], ['OI 05', 'RM 05'], ['OI 09', 'RM 09']] 

"""
接口TOKEN
"""
TOKEN = '03732aff833845903c8d68dd24c79e7c41d6b2f2e8c62ee13c2713e5'

"""
路径配置
"""
SOURCE_DIR = 'D:/HUAXIN_FUND/SourceData'  # 源文件目录
RESULT_DIR = 'D:/HUAXIN_FUND/ResultData'  # 结果文件目录
RESEARCH_STOCK_DIR = 'D:/HUAXIN_FUND/ResearchReport/STOCK'  # 个股研报文件目录
RESEARCH_INDUSTRY_DIR = 'D:/HUAXIN_FUND/ResearchReport/INDUSTRY'  # 行业研报文件目录
