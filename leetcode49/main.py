class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = dict()  # 创建一个字典，其中key记录排好序的字符串，value记录相同的字符
        for s in strs:
            # 对每个字符串进行排序，作为字典的key
            sort_s = ''.join(sorted(s))
            # 如果字典中没有这个key，就初始化为空列表
            if sort_s not in str_dict:
                str_dict[sort_s] = []
            # 如果字典中有这个key，就直接加入
            str_dict[sort_s].append(s)
        return list(str_dict.values())  # 返回字典中的value
