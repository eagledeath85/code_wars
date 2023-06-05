def outed(meet: dict, boss: str) -> str:
    meet.update({boss: 2*meet[boss]})
    total = []
    for k, v in meet.items():
        total.append(v)
    happiness = round(sum(total) / len(total))
    return "Get Out Now!" if happiness <= 5 else 'Nice Work Champ!'




decision1 = outed({'tim' :0, 'jim' :2, 'randy' :0, 'sandy' :7, 'andy' :0, 'katie' :5, 'laura' :1, 'saajid' :2, 'alex' :3, 'john' :2, 'mr' :0}, 'laura')
# test.assert_equals(outed
#     ({'tim' :0, 'jim' :2, 'randy' :0, 'sandy' :7, 'andy' :0, 'katie' :5, 'laura' :1, 'saajid' :2, 'alex' :3, 'john' :2, 'mr' :0}, 'laura'), 'Get Out Now!')
# test.assert_equals(outed
#     ({'tim' :1, 'jim' :3, 'randy' :9, 'sandy' :6, 'andy' :7, 'katie' :6, 'laura' :9, 'saajid' :9, 'alex' :9, 'john' :9, 'mr' :8}, 'katie'), 'Nice Work Champ!')
# test.assert_equals(outed
#     ({'tim' :2, 'jim' :4, 'randy' :0, 'sandy' :5, 'andy' :8, 'katie' :6, 'laura' :2, 'saajid' :2, 'alex' :3, 'john' :2, 'mr' :8}, 'john'), 'Get Out Now!')

decision2 = outed({
    'tim': 0,
    'jim': 3,
    'randy': 3,
    'sandy': 6,
    'andy': 1,
    'katie': 3,
    'laura': 8,
    'saajid': 5,
    'alex': 9,
    'john': 9,
    'mr': 1,
  },
  boss = 'randy')
print(decision2)