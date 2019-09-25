import data as rd

# improve

_time = {2: {
    'timely': [rd.timely3_2_4, rd.timely4_2_4, rd.timely5_2_4, rd.timely3_2_5, rd.timely4_2_5,
               rd.timely5_2_5,
               rd.timely3_2_6,
               rd.timely4_2_6,
               rd.timely5_2_6,
               rd.timely3_2_7,
               rd.timely4_2_7,
               rd.timely5_2_7
               ],
    'untimely': [rd.untimely3_2_4, rd.untimely4_2_4, rd.untimely5_2_4, rd.untimely3_2_5, rd.untimely4_2_5,
                 rd.untimely5_2_5,
                 rd.untimely3_2_6,
                 rd.untimely4_2_6,
                 rd.untimely5_2_6,
                 rd.untimely3_2_7,
                 rd.untimely4_2_7,
                 rd.untimely5_2_7
                 ]
},
    3: {
        'timely': [rd.timely3_3_4, rd.timely4_3_4, rd.timely5_3_4, rd.timely3_3_5, rd.timely4_3_5,
                   rd.timely5_3_5,
                   rd.timely3_3_6,
                   rd.timely4_3_6,
                   rd.timely5_3_6, rd.timely3_3_7,
                   rd.timely4_3_7,
                   rd.timely5_3_7
                   ],
        'untimely': [rd.untimely3_3_4, rd.untimely4_3_4, rd.untimely5_3_4, rd.untimely3_3_5, rd.untimely4_3_5,
                     rd.untimely5_3_5,
                     rd.untimely3_3_6,
                     rd.untimely4_3_6,
                     rd.untimely5_3_6,
                     rd.untimely3_3_7,
                     rd.untimely4_3_7,
                     rd.untimely5_3_7
                     ]
    },
    7: {
        'timely': [rd.timely3_7_4, rd.timely4_7_4, rd.timely5_7_4, rd.timely3_7_5, rd.timely4_7_5,
                   rd.timely5_7_5,
                   rd.timely3_7_6,
                   rd.timely4_7_6,
                   rd.timely5_7_6, rd.timely3_7_7,
                   rd.timely4_7_7,
                   rd.timely5_7_7
                   ],
        'untimely': [rd.untimely3_7_4, rd.untimely4_7_4, rd.untimely5_7_4, rd.untimely3_7_5, rd.untimely4_7_5,
                     rd.untimely5_7_5,
                     rd.untimely3_7_6,
                     rd.untimely4_7_6,
                     rd.untimely5_7_6, rd.untimely3_7_7,
                     rd.untimely4_7_7,
                     rd.untimely5_7_7
                     ],
    },
    10: {
        'timely': [rd.timely3_10_4, rd.timely4_10_4, rd.timely5_10_4, rd.timely3_10_5, rd.timely4_10_5,
                   rd.timely5_10_5,
                   rd.timely3_10_6,
                   rd.timely4_10_6,
                   rd.timely5_10_6, rd.timely3_10_7,
                   rd.timely4_10_7,
                   rd.timely5_10_7
                   ],
        'untimely': [rd.untimely3_10_4, rd.untimely4_10_4, rd.untimely5_10_4, rd.untimely3_10_5, rd.untimely4_10_5,
                     rd.untimely5_10_5,
                     rd.untimely3_10_6,
                     rd.untimely4_10_6,
                     rd.untimely5_10_6, rd.untimely3_10_7,
                     rd.untimely4_10_7,
                     rd.untimely5_10_7
                     ],
    },
    12: {
        'timely': [rd.timely3_12_4, rd.timely4_12_4, rd.timely5_12_4, rd.timely3_12_5, rd.timely4_12_5,
                   rd.timely5_12_5,
                   rd.timely3_12_6,
                   rd.timely4_12_6,
                   rd.timely5_12_6, rd.timely3_12_7,
                   rd.timely4_12_7,
                   rd.timely5_12_7
                   ],
        'untimely': [rd.untimely3_12_4, rd.untimely4_12_4, rd.untimely5_12_4, rd.untimely3_12_5, rd.untimely4_12_5,
                     rd.untimely5_12_5,
                     rd.untimely3_12_6,
                     rd.untimely4_12_6,
                     rd.untimely5_12_6, rd.untimely3_12_7,
                     rd.untimely4_12_7,
                     rd.untimely5_12_7
                     ],
    },
    16: {
        'timely': [rd.timely3_16_4, rd.timely4_16_4, rd.timely5_16_4, rd.timely3_16_5, rd.timely4_16_5,
                   rd.timely5_16_5,
                   rd.timely3_16_6,
                   rd.timely4_16_6,
                   rd.timely5_16_6, rd.timely3_16_7,
                   rd.timely4_16_7,
                   rd.timely5_16_7
                   ],
        'untimely': [rd.untimely3_16_4, rd.untimely4_16_4, rd.untimely5_16_4, rd.untimely3_16_5, rd.untimely4_16_5,
                     rd.untimely5_16_5,
                     rd.untimely3_16_6,
                     rd.untimely4_16_6,
                     rd.untimely5_16_6, rd.untimely3_16_7,
                     rd.untimely4_16_7,
                     rd.untimely5_16_7
                     ],
    }
}

wait_time = {
    24: [rd.wt0_2_4, rd.wt1_2_4, rd.wt2_2_4, rd.wt3_2_4],
    25: [rd.wt0_2_5, rd.wt1_2_5, rd.wt2_2_5, rd.wt3_2_5, rd.wt4_2_5, ],
    26: [rd.wt0_2_6, rd.wt1_2_6, rd.wt2_2_6, rd.wt3_2_6, rd.wt4_2_6, rd.wt5_2_6],
    27: [rd.wt0_2_7, rd.wt1_2_7, rd.wt2_2_7, rd.wt3_2_7, rd.wt4_2_7, rd.wt5_2_7, rd.wt6_2_7],

    34: [rd.wt0_3_4, rd.wt1_3_4, rd.wt2_3_4, rd.wt3_3_4],
    35: [rd.wt0_3_5, rd.wt1_3_5, rd.wt2_3_5, rd.wt3_3_5, rd.wt4_3_5],
    36: [rd.wt0_3_6, rd.wt1_3_6, rd.wt2_3_6, rd.wt3_3_6, rd.wt4_3_6, rd.wt5_3_6],
    37: [rd.wt0_3_7, rd.wt1_3_7, rd.wt2_3_7, rd.wt3_3_7, rd.wt4_3_7, rd.wt5_3_7, rd.wt6_3_7],

    74: [rd.wt0_7_4, rd.wt1_7_4, rd.wt2_7_4, rd.wt3_7_4],
    75: [rd.wt0_7_5, rd.wt1_7_5, rd.wt2_7_5, rd.wt3_7_5, rd.wt4_7_5],
    76: [rd.wt0_7_6, rd.wt1_7_6, rd.wt2_7_6, rd.wt3_7_6, rd.wt4_7_6, rd.wt5_7_6],
    77: [rd.wt0_7_7, rd.wt1_7_7, rd.wt2_7_7, rd.wt3_7_7, rd.wt4_7_7, rd.wt5_7_7, rd.wt6_7_7],

    104: [rd.wt0_10_4, rd.wt1_10_4, rd.wt2_10_4, rd.wt3_10_4],
    105: [rd.wt0_10_5, rd.wt1_10_5, rd.wt2_10_5, rd.wt3_10_5, rd.wt4_10_5],
    106: [rd.wt0_10_6, rd.wt1_10_6, rd.wt2_10_6, rd.wt3_10_6, rd.wt4_10_6, rd.wt5_10_6],
    107: [rd.wt0_10_7, rd.wt1_10_7, rd.wt2_10_7, rd.wt3_10_7, rd.wt4_10_7, rd.wt5_10_7, rd.wt6_10_7],

    124: [rd.wt0_12_4, rd.wt1_12_4, rd.wt2_12_4, rd.wt3_12_4],
    125: [rd.wt0_12_5, rd.wt1_12_5, rd.wt2_12_5, rd.wt3_12_5, rd.wt4_12_5],
    126: [rd.wt0_12_6, rd.wt1_12_6, rd.wt2_12_6, rd.wt3_12_6, rd.wt4_12_6, rd.wt5_12_6],
    127: [rd.wt0_12_7, rd.wt1_12_7, rd.wt2_12_7, rd.wt3_12_7, rd.wt4_12_7, rd.wt5_12_7, rd.wt6_12_7],

    164: [rd.wt0_16_4, rd.wt1_16_4, rd.wt2_16_4, rd.wt3_16_4],
    165: [rd.wt0_16_5, rd.wt1_16_5, rd.wt2_16_5, rd.wt3_16_5, rd.wt4_16_5],
    166: [rd.wt0_16_6, rd.wt1_16_6, rd.wt2_16_6, rd.wt3_16_6, rd.wt4_16_6, rd.wt5_16_6],
    167: [rd.wt0_16_7, rd.wt1_16_7, rd.wt2_16_7, rd.wt3_16_7, rd.wt4_16_7, rd.wt5_16_7, rd.wt6_16_7],
}

_rtt_ = {
    24: [rd.rtt0_2_4, rd.rtt1_2_4, rd.rtt2_2_4, rd.rtt3_2_4],
    25: [rd.rtt0_2_5, rd.rtt1_2_5, rd.rtt2_2_5, rd.rtt3_2_5, rd.rtt4_2_5, ],
    26: [rd.rtt0_2_6, rd.rtt1_2_6, rd.rtt2_2_6, rd.rtt3_2_6, rd.rtt4_2_6, rd.rtt5_2_6],
    27: [rd.rtt0_2_7, rd.rtt1_2_7, rd.rtt2_2_7, rd.rtt3_2_7, rd.rtt4_2_7, rd.rtt5_2_7, rd.rtt6_2_7],

    34: [rd.rtt0_3_4, rd.rtt1_3_4, rd.rtt2_3_4, rd.rtt3_3_4],
    35: [rd.rtt0_3_5, rd.rtt1_3_5, rd.rtt2_3_5, rd.rtt3_3_5, rd.rtt4_3_5],
    36: [rd.rtt0_3_6, rd.rtt1_3_6, rd.rtt2_3_6, rd.rtt3_3_6, rd.rtt4_3_6, rd.rtt5_3_6],
    37: [rd.rtt0_3_7, rd.rtt1_3_7, rd.rtt2_3_7, rd.rtt3_3_7, rd.rtt4_3_7, rd.rtt5_3_7, rd.rtt6_3_7],

    74: [rd.rtt0_7_4, rd.rtt1_7_4, rd.rtt2_7_4, rd.rtt3_7_4],
    75: [rd.rtt0_7_5, rd.rtt1_7_5, rd.rtt2_7_5, rd.rtt3_7_5, rd.rtt4_7_5],
    76: [rd.rtt0_7_6, rd.rtt1_7_6, rd.rtt2_7_6, rd.rtt3_7_6, rd.rtt4_7_6, rd.rtt5_7_6],
    77: [rd.rtt0_7_7, rd.rtt1_7_7, rd.rtt2_7_7, rd.rtt3_7_7, rd.rtt4_7_7, rd.rtt5_7_7, rd.rtt6_7_7],

    104: [rd.rtt0_10_4, rd.rtt1_10_4, rd.rtt2_10_4, rd.rtt3_10_4],
    105: [rd.rtt0_10_5, rd.rtt1_10_5, rd.rtt2_10_5, rd.rtt3_10_5, rd.rtt4_10_5],
    106: [rd.rtt0_10_6, rd.rtt1_10_6, rd.rtt2_10_6, rd.rtt3_10_6, rd.rtt4_10_6, rd.rtt5_10_6],
    107: [rd.rtt0_10_7, rd.rtt1_10_7, rd.rtt2_10_7, rd.rtt3_10_7, rd.rtt4_10_7, rd.rtt5_10_7, rd.rtt6_10_7],

    124: [rd.rtt0_12_4, rd.rtt1_12_4, rd.rtt2_12_4, rd.rtt3_12_4],
    125: [rd.rtt0_12_5, rd.rtt1_12_5, rd.rtt2_12_5, rd.rtt3_12_5, rd.rtt4_12_5],
    126: [rd.rtt0_12_6, rd.rtt1_12_6, rd.rtt2_12_6, rd.rtt3_12_6, rd.rtt4_12_6, rd.rtt5_12_6],
    127: [rd.rtt0_12_7, rd.rtt1_12_7, rd.rtt2_12_7, rd.rtt3_12_7, rd.rtt4_12_7, rd.rtt5_12_7, rd.rtt6_12_7],

    164: [rd.rtt0_16_4, rd.rtt1_16_4, rd.rtt2_16_4, rd.rtt3_16_4],
    165: [rd.rtt0_16_5, rd.rtt1_16_5, rd.rtt2_16_5, rd.rtt3_16_5, rd.rtt4_16_5],
    166: [rd.rtt0_16_6, rd.rtt1_16_6, rd.rtt2_16_6, rd.rtt3_16_6, rd.rtt4_16_6, rd.rtt5_16_6],
    167: [rd.rtt0_16_7, rd.rtt1_16_7, rd.rtt2_16_7, rd.rtt3_16_7, rd.rtt4_16_7, rd.rtt5_16_7, rd.rtt6_16_7],
}

_cpu_ = {
    24: [rd.cpu0_2_4, rd.cpu1_2_4, rd.cpu2_2_4, rd.cpu3_2_4],
    25: [rd.cpu0_2_5, rd.cpu1_2_5, rd.cpu2_2_5, rd.cpu3_2_5, rd.cpu4_2_5, ],
    26: [rd.cpu0_2_6, rd.cpu1_2_6, rd.cpu2_2_6, rd.cpu3_2_6, rd.cpu4_2_6, rd.cpu5_2_6],
    27: [rd.cpu0_2_7, rd.cpu1_2_7, rd.cpu2_2_7, rd.cpu3_2_7, rd.cpu4_2_7, rd.cpu5_2_7, rd.cpu6_2_7],

    34: [rd.cpu0_3_4, rd.cpu1_3_4, rd.cpu2_3_4, rd.cpu3_3_4],
    35: [rd.cpu0_3_5, rd.cpu1_3_5, rd.cpu2_3_5, rd.cpu3_3_5, rd.cpu4_3_5],
    36: [rd.cpu0_3_6, rd.cpu1_3_6, rd.cpu2_3_6, rd.cpu3_3_6, rd.cpu4_3_6, rd.cpu5_3_6],
    37: [rd.cpu0_3_7, rd.cpu1_3_7, rd.cpu2_3_7, rd.cpu3_3_7, rd.cpu4_3_7, rd.cpu5_3_7, rd.cpu6_3_7],

    74: [rd.cpu0_7_4, rd.cpu1_7_4, rd.cpu2_7_4, rd.cpu3_7_4],
    75: [rd.cpu0_7_5, rd.cpu1_7_5, rd.cpu2_7_5, rd.cpu3_7_5, rd.cpu4_7_5],
    76: [rd.cpu0_7_6, rd.cpu1_7_6, rd.cpu2_7_6, rd.cpu3_7_6, rd.cpu4_7_6, rd.cpu5_7_6],
    77: [rd.cpu0_7_7, rd.cpu1_7_7, rd.cpu2_7_7, rd.cpu3_7_7, rd.cpu4_7_7, rd.cpu5_7_7, rd.cpu6_7_7],

    104: [rd.cpu0_10_4, rd.cpu1_10_4, rd.cpu2_10_4, rd.cpu3_10_4],
    105: [rd.cpu0_10_5, rd.cpu1_10_5, rd.cpu2_10_5, rd.cpu3_10_5, rd.cpu4_10_5],
    106: [rd.cpu0_10_6, rd.cpu1_10_6, rd.cpu2_10_6, rd.cpu3_10_6, rd.cpu4_10_6, rd.cpu5_10_6],
    107: [rd.cpu0_10_7, rd.cpu1_10_7, rd.cpu2_10_7, rd.cpu3_10_7, rd.cpu4_10_7, rd.cpu5_10_7, rd.cpu6_10_7],

    124: [rd.cpu0_12_4, rd.cpu1_12_4, rd.cpu2_12_4, rd.cpu3_12_4],
    125: [rd.cpu0_12_5, rd.cpu1_12_5, rd.cpu2_12_5, rd.cpu3_12_5, rd.cpu4_12_5],
    126: [rd.cpu0_12_6, rd.cpu1_12_6, rd.cpu2_12_6, rd.cpu3_12_6, rd.cpu4_12_6, rd.cpu5_12_6],
    127: [rd.cpu0_12_7, rd.cpu1_12_7, rd.cpu2_12_7, rd.cpu3_12_7, rd.cpu4_12_7, rd.cpu5_12_7, rd.cpu6_12_7],

    164: [rd.cpu0_16_4, rd.cpu1_16_4, rd.cpu2_16_4, rd.cpu3_16_4],
    165: [rd.cpu0_16_5, rd.cpu1_16_5, rd.cpu2_16_5, rd.cpu3_16_5, rd.cpu4_16_5],
    166: [rd.cpu0_16_6, rd.cpu1_16_6, rd.cpu2_16_6, rd.cpu3_16_6, rd.cpu4_16_6, rd.cpu5_16_6],
    167: [rd.cpu0_16_7, rd.cpu1_16_7, rd.cpu2_16_7, rd.cpu3_16_7, rd.cpu4_16_7, rd.cpu5_16_7, rd.cpu6_16_7],
}


def average_timely():
    av = {}

    for i in _time:
        for j in _time[i]:
            _id = 4
            a = 0
            for t in range(4):
                _key = f'{j}_{_id}_{i}'
                av[_key] = sum(_time[i][j][a:a + 3])
                _id += 1
                a += 3

    return av


print(average_timely())
