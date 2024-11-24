class Solution:
    def solution(self, phone_book):

        order_phone_book = sorted(phone_book)
        answer = True

        for i in range(len(order_phone_book)):
            for j in range(len(order_phone_book)-1):
                print(order_phone_book[j+1])
                if order_phone_book[j+i].startswith(order_phone_book[i]):
                    answer = False
                    return answer

        return answer


phone_book = ["123","456","789"]
print(Solution().solution(phone_book))