def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda phone: len(phone))
    phone_dic = {}

    for phone in phone_book:
        for i in range(len(phone)):
            if phone[:i+1] in phone_dic:
                return False
        else:
            phone_dic[phone] = True
    return True

print(solution(["12","123","1235","567","88"]))