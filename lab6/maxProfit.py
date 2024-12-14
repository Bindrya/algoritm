 # maxProfit хувьсагч нь нийт ашигийг хадгалах зориулалттай. Эхлээд 0 гэж өгсөн.
        
        # Үнийн жагсаалтад эхнээс нь 1-р индексээс эхэлж, дараагийн үнийг өмнөх үнийнхтэй харьцуулж, 
        # үнийн өсөлттэй үед ашиг олох зарчмаар ажиллана. 
        # Хэрвээ дараагийн үнэ нь өмнөх үнийн үнэас их байвал энэ нь худалдан авах ба борлуулах боломжийг илэрхийлнэ.
        
        # Өмнөх үнийн өсөлтөөс олсон ашигийг нийт ашигтай холбож, эцсийн үр дүнг тооцно.
        # Хэрвээ үнэ буурсан бол ашиг олох боломжгүй учир хичнээн бууралтаас хамаарахгүй.
        
        # Эцсийн эцэст, нийт ашигийг `maxProfit` хувьсагчийг буцааж өгнө.



class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        
        # Үнийн өсөлтүүдийг тооцох
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        
        return maxProfit


# Main хэсэг
if __name__ == "__main__":
    solution = Solution()

    # Туршилтын тоонууд
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Max Profit for prices1:", solution.maxProfit(prices1))  # 7

    prices2 = [1, 2, 3, 4, 5]
    print("Max Profit for prices2:", solution.maxProfit(prices2))  # 4

    prices3 = [7, 6, 4, 3, 1]
    print("Max Profit for prices3:", solution.maxProfit(prices3))  # 0
