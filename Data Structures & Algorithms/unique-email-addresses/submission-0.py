class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        def parseEmail(email):
            sep_idx = email.find('@')
            local_name = ""
            for c in range(sep_idx):
                if email[c] == '.':
                    continue
                if email[c] == '+':
                    break
                local_name += email[c]
            domain_name = email[sep_idx:]
            return local_name + domain_name


        for email in emails:
            unique_emails.add(parseEmail(email))
        return len(unique_emails)
