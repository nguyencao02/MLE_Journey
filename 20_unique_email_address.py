class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        list_mail_unique = set()  
        for email in emails:  
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.',"")
            new_email = local + "@" + domain
            list_mail_unique.add(new_email)
        return len(list_mail_unique)
            