from typing import Optional

from .reqModule import clReq

class record():
    def list(
        zone_identifier:str = None,
        email:str = None,
        token:str = None,
        match:str = None,
        name:str = None,
        order:str = None,
        page:int = None,
        per_page:int = None,
        content:str = None,
        type:str = None,
        proxied:str = None,
        direction:str = None,
    ):
        """
        Cloudflare API Reference Link: https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records
        zone_identifier: str
            Description: A unique ID for each zone
        email: str
            Description: Your email when you login cloudflare
            Example: "example@example.com"
        token: str
            Description: Your API token
        match: str
            Description: Whether to match all search requirements or at least one (any)
            Example: "all"
            Constraints:
                default value: all
                valid values: any, all
        name: str
            Description: DNS record name (or @ for the zone apex)
            Example: "example.com"
            Constraints:
                max length: 255
        order: str
            Description: Field to order records by
            Example: "type"
            Constraints:
                valid values: type, name, content, ttl, proxied
        page: int
            Description: Page number of paginated results
            Example: 1
            Constraints:
                default value: 1
                min value:1
        per_page: int
            Description: Number of DNS records per page
            Example: 100
            Constraints:
                default value: 100
                min value:5
                max value:5000
        content: str
            Description: DNS record content
            Example: "127.0.0.1"
        type: str
            Description: DNS record type
            Example: "A"
            Constraints:
                valid values: A, AAAA, CNAME, HTTPS, TXT, SRV, LOC, MX, NS, CERT, DNSKEY, DS, NAPTR, SMIMEA, SSHFP, SVCB, TLSA, URI
                read only
        proxied: bool
            Description: DNS record proxied status
            Example: false
            Constraints:
                valid values: (true,false)
        direction: str
            Description: Direction to order domains
            Example: "desc"
            Constraints:
                valid values: asc, desc
        """
        if not zone_identifier:
            raise AttributeError("zone_identifier not found!")
        elif not email or not token:
            raise AttributeError("token or email not found!")
        else:
            url = f'https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/'
            headers = {
                'X-Auth-Email' : email,
                'Authorization': f'Bearer {token}',
                'Content-Type' :  'application/json'
            }
            payload = {}
            if match:
                payload['match'] = match
            if name:
                payload['name'] = name
            if order:
                payload['order'] = order
            if page:
                payload['page'] = page
            if page:
                payload['page'] = page
            if per_page:
                payload['per_page'] = per_page
            if content:
                payload['content'] = content
            if type:
                payload['type'] = type
            if proxied:
                payload['proxied'] = proxied
            if direction:
                payload['direction'] = direction

            res = clReq.request('GET', url, headers, payload)
            return res


    def create(
        zone_identifier:str = None,
        email:str = None,
        token:str = None,
        type:str = None,
        name:str = None,
        content:str = None,
        ttl:int = 1,
        priority:Optional[int] = None,
        proxied:Optional[bool] = None
    ):
        """
        Cloudflare API Reference Link: https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record
        zone_identifier: str
            Description: A unique ID for each zone
        email: str
            Description: Your email when you login cloudflare
            Example: "example@example.com"
        token: str
            Description: Your API token
        type: str
            Description: DNS record type
            Example: "A"
            Constraints:
                Valid Values: A, AAAA, CNAME, HTTPS, TXT, SRV, LOC, MX, NS, CERT, DNSKEY, DS, NAPTR, SMIMEA, SSHFP, SVCB, TLSA, URI
        name: str
            Description: DNS record name (or @ for the zone apex)
            Example: "example.com"
            Constraints:
                Max Length: 255
        content: str
            Description: DNS record content
            Example: "127.0.0.1"
        ttl: int
            Description: Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for 'automatic'
            Example: 3600
        priority: bool
            Description: Required for MX, SRV and URI records; unused by other record types. Records with lower priorities are preferred
            Min Value:0
            Max Value:65535
        proxied: bool
            Description: Whether the record is receiving the performance and security benefits of Cloudflare
            Example ; False
            Constraints:
                Valid Values: True,False
        """
        if not zone_identifier:
            raise AttributeError("zone_identifier not found!")
        elif not email or not token:
            raise AttributeError("token or email not found!")
        elif not name or not content or not ttl:
            raise AttributeError("You don't have required parameters. Plase check it https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record")
        else:
            url = f'https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/'
            headers = {
                'X-Auth-Email' : email,
                'Authorization': f'Bearer {token}',
                'Content-Type' :  'application/json'
            }
            payload = {
                "type":type,
                "name":name,
                "content":content,
                "ttl":ttl,
            }
            if priority:
                payload['priority'] = priority
            if proxied:
                payload['proxied'] = proxied

            res = clReq.request('POST', url, headers, payload)
            return res

    def details(
        zone_identifier:str = None,
        identifier:str = None,
        email:str = None,
        token:str = None,
    ):
        """
        Cloudflare API Reference Link: https://api.cloudflare.com/#dns-records-for-a-zone-dns-record-details
        zone_identifier: str
            Description: A unique ID for each zone
        identifier: str
            Description: A unique ID for each dns
        email: str
            Description: Your email when you login cloudflare
            Example: "example@example.com"
        token: str
            Description: Your API token
        """
        if not zone_identifier or not identifier:
            raise AttributeError("zone_identifier or identifier not found!")
        elif not email or not token:
            raise AttributeError("token or email not found!")
        else:
            url = f'https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/'
            headers = {
                'X-Auth-Email' : email,
                'Authorization': f'Bearer {token}',
                'Content-Type' :  'application/json'
            }
            res = clReq.request('GET', url, headers)

            return res

    def update(
        zone_identifier:str = None,
        identifier:str = None,
        email:str = None,
        token:str = None,
        type:str = None,
        name:str = None,
        content:str = None,
        ttl:int = 1,
        proxied:Optional[bool] = None
    ):
        """
        Cloudflare API Reference Link: https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record

        zone_identifier: str
            Description: A unique ID for each zone
        identifier: str
            Description: A unique ID for each record
        email: str
            Description: Your email when you login cloudflare
            Example: "example@example.com"
        token: str
            Description: Your API token
        type: str
            Description: DNS record type
            Example: "A"
            Constraints:
                Valid Values: A, AAAA, CNAME, HTTPS, TXT, SRV, LOC, MX, NS, CERT, DNSKEY, DS, NAPTR, SMIMEA, SSHFP, SVCB, TLSA, URI
        name: str
            Description: DNS record name (or @ for the zone apex)
            Example: "example.com"
            Constraints:
                Max Length: 255
        content: str
            Description: DNS record content
            Example: "127.0.0.1"
        ttl: int
            Description: Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for 'automatic'
            Example: 3600
        proxied: bool
            Description: Whether the record is receiving the performance and security benefits of Cloudflare
            Example ; False
            Constraints:
                Valid Values: True,False
        """
        
        if not zone_identifier or not identifier:
            raise AttributeError("zone_identifier or identifier not found!")
        elif not email or not token:
            raise AttributeError("token or email not found!")
        elif not name or not content or not ttl:
            raise AttributeError("You don't have required parameters. Plase check it https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record")
        else:
            url = f'https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/{identifier}'
            headers = {
                'X-Auth-Email' : email,
                'Authorization': f'Bearer {token}',
                'Content-Type' :  'application/json'
            }
            payload = {
                "type":type,
                "name":name,
                "content":content,
                "ttl":ttl
            }
            if proxied:
                payload['proxied'] = proxied
            res = clReq.request('PUT', url, headers, payload)
            return res
    
    def patch(
        zone_identifier:str = None,
        identifier:str = None,
        email:str = None,
        token:str = None,
        type:Optional[str] = None,
        name:Optional[str] = None,
        content:Optional[str] = None,
        ttl:Optional[int] = 1,
        proxied:Optional[bool] = None
    ):
        """
        Cloudflare API Reference Link: https://api.cloudflare.com/#dns-records-for-a-zone-patch-dns-record

        zone_identifier: str
            Description: A unique ID for each zone
        identifier: str
            Description: A unique ID for each record
        email: str
            Description: Your email when you login cloudflare
            Example: "example@example.com"
        token: str
            Description: Your API token
        type: str
            Description: DNS record type
            Example: "A"
            Constraints:
                Valid Values: A, AAAA, CNAME, HTTPS, TXT, SRV, LOC, MX, NS, CERT, DNSKEY, DS, NAPTR, SMIMEA, SSHFP, SVCB, TLSA, URI
        name: str
            Description: DNS record name (or @ for the zone apex)
            Example: "example.com"
            Constraints:
                Max Length: 255
        content: str
            Description: DNS record content
            Example: "127.0.0.1"
        ttl: int
            Description: Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for 'automatic'
            Example: 3600
        proxied: bool
            Description: Whether the record is receiving the performance and security benefits of Cloudflare
            Example ; False
            Constraints:
                Valid Values: True,False
        """
        if not zone_identifier or not identifier:
            raise AttributeError("zone_identifier or identifier not found!")
        elif not email or not token:
            raise AttributeError("token or email not found!")
        else:
            url = f'https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/{identifier}'
            headers = {
                'X-Auth-Email' : email,
                'Authorization': f'Bearer {token}',
                'Content-Type' :  'application/json'
            }
            payload = {}
            if type:
                payload['type'] = type
            if name:
                payload['name'] = name
            if content:
                payload['content'] = content
            if ttl:
                payload['ttl'] = ttl
            if proxied:
                payload['proxied'] = proxied
            if (payload == {}):
                raise AttributeError("You must one or more set argument. https://api.cloudflare.com/#dns-records-for-a-zone-patch-dns-record")
            else:
                res = clReq.request('PATCH', url, headers, payload)
                return res

    def scan(
        zone_identifier:str = None,
        email:str = None,
        token:str = None,
    ):
        """
        Cloudflare API Reference Link: https://api.cloudflare.com/#dns-records-for-a-zone-scan-dns-records
        zone_identifier: str
            Description: A unique ID for each zone
        email: str
            Description: Your email when you login cloudflare
            Example: "example@example.com"
        token: str
            Description: Your API token
        """
        if not zone_identifier:
            raise AttributeError("zone_identifier not found!")
        elif not email or not token:
            raise AttributeError("token or email not found!")
        else:
            url = f'https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/scan'
            headers = {
                'X-Auth-Email' : email,
                'Authorization': f'Bearer {token}',
                'Content-Type' :  'application/json'
            }
            res = clReq.request('POST', url, headers)

            return res