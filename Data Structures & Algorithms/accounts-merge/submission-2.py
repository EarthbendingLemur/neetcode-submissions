class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_ID = {}
        user_ID = {}

        def checkEmailID(emails):
            matchedIDS = set()

            for email in emails:
                if email in email_ID:
                    matchedIDS.add(email_ID[email])
            return matchedIDS


        for account in accounts:
            # Account is in form [USER, EMAIL1, EMAIL2...]
            username = account[0]
            emails = account[1:]
            existingIDS = checkEmailID(emails)
            if not existingIDS:
                newID = len(email_ID) + 1
                for email in emails:
                    email_ID[email] = newID
                user_ID[newID] = username
            else:
                existingID = next(iter(existingIDS))
                for oldID in existingIDS:
                    if oldID == existingID:
                        continue
                    
                    for email in email_ID:
                        if email_ID[email] == oldID:
                            email_ID[email] = existingID
                    del user_ID[oldID]
                
                for email in emails:
                    email_ID[email] = existingID
        
        res = []
        print(email_ID)
        print(user_ID)
        for userID, username in user_ID.items():
            this_account = []
            this_account.append(username)

            matching_emails = [email for email, emailID in email_ID.items() if emailID == userID]
            this_account.extend(matching_emails)
            res.append(this_account)
        return res



            