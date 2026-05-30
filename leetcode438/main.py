class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 记录各中个字母出现的次数
        cnt_p = Counter(p)
        # 记录s中长度为len(p)的子字符串各字母出现的次数
        cnt_s = Counter()

        result = []

        for right, a in enumerate(s):
            cnt_s[a] += 1

            left = right - len(p) + 1
            if left < 0:
                continue

            # s中长度为len(p)的子字符串各字母出现的次数跟p相同，就加入
            if cnt_p == cnt_s:
                result.append(left)

            cnt_s[s[left]] -= 1

        return result

