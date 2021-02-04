voted = dict()
def check_voter(name):
    if voted.get(name):
        return print("돌려보내기")
    else:
        voted[name] = True
        return print("투표하게 하기")

check_voter('kang_texas')
check_voter('kang_texas')
