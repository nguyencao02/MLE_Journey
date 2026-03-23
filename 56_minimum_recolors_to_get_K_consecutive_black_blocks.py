class Solution:
    def minimumRecolors(self, blocks: str, k: int)-> int:
        current_W = blocks[:k].count('W')
        min_W = current_W
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_W -= 1
            if blocks[i] == 'W':
                current_W += 1
            if current_W < min_W:
                min_W = current_W
        return min_W