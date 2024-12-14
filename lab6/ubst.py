# Хомхойлох (Greedy) аргыг ашиглан оновчтой хоёртын хайлтын модыг (OBST) үүсгэх алгоритм:
#
# Энэ алгоритм нь түлхүүрүүд (keys) болон тэдгээрийн давтамж (freq)-д үндэслэн 
# хоёртын хайлтын модыг үүсгэхдээ хомхойлох аргыг ашиглана. Хомхойлох арга нь 
# тухайн мөчид хамгийн ашигтай буюу хамгийн бага зардалтай үйлдлийг сонгодог.
#
# Алгоритмын үндсэн санаа:
#
# 1. **Хамгийн өндөр давтамжтай түлхүүрийг сонгох:**
#    - Хайлт хийх зардлыг бууруулахын тулд хамгийн их магадлалтай түлхүүрийг 
#      модны үндэс болгон сонгоно.
#    - Сонгосон үндэс нь үлдсэн түлхүүрүүдийг зүүн болон баруун дэд моднуудад хуваана.
#
# 2. **Хуваагдлыг давтах:**
#    - Зүүн болон баруун дэд модыг тус тусын хамгийн өндөр давтамжтай түлхүүрүүдийг 
#      үндэс болгон сонгох аргаар дахин үүсгэнэ.
#
# 3. **Давтамжийн нийлбэр:**
#    - Түлхүүрүүдийг үндсэнээс хамгийн доод түвшин хүртэл жингээр нь 
#      тооцож хайлтын нийт зардлыг гаргана.
#
# Алгоритмын үр дүн:
# - Түлхүүрүүдийг хомхойлох аргаар хоёртын хайлтын модонд зохион байгуулахад 
#   шаардлагатай нийт хайлтын зардлыг тооцно.
#
# Энэ арга нь үргэлж оновчтой шийдэлд хүрэхгүй ч хурдан бөгөөд ойлгомжтой шийдэл гаргана.
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  
        dp[1] = 1  
        
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1  
                right = nodes - root  
                dp[nodes] += dp[left] * dp[right]
        
        return dp[n]

# Main функц
if __name__ == "__main__":
    solution = Solution()
    print("Number of unique BSTs for n = 3:", solution.numTrees(3))  # 5
    print("Number of unique BSTs for n = 1:", solution.numTrees(1))  # 1
