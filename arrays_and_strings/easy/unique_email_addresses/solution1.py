class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        visited = []
        for email in emails:
            local_name = email.split('@')[0]
            domain_name = email.split('@')[1]
            new_local_name = ''

            if '+' in local_name:
                local_name = local_name.split('+')[0]

            for letter in local_name:
                if letter == '.':
                    continue
                else:
                    new_local_name += letter
            
            
            full_email = new_local_name + '@' + domain_name
            
            if full_email not in visited:
                visited.append(full_email)
        
        return len(visited)
            


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

print(Solution().numUniqueEmails(emails=emails))