class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for m in emails:
            lname,dom_name = m.split('@')
            lname=lname.replace(".","")
            if "+" in lname:
                lname= lname[:lname.index("+")]
            res.add(lname+'@'+dom_name)
        return len(res)
