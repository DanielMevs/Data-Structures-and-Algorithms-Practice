class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}

        def count(current_goal, old_songs):
            if current_goal == 0 and old_songs == n:
                return 1
            if current_goal == 0 or old_songs > n:
                return 0
            if (current_goal, old_songs) in dp:
                return dp[(current_goal, old_songs)]

            result = (n - old_songs) * count(current_goal - 1, old_songs + 1)

            if old_songs > k:
                # choose an old song
                result += (old_songs - k) * count(current_goal - 1, old_songs)

            dp[(current_goal, old_songs)] = result % mod
            return result % mod

        return count(goal, 0)
