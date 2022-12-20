# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyBCYW5uZXIgRmlsZQppbXBvcnQgZGF0ZXRpbWUKaW1wb3J0IHRpbWUKCmltcG9ydCBTeXN0ZW0uUmVxdWlyZW1lbnRzLkZURAoKTGF1bmNoZXIgPSAnJycKICBfICAgICAgICAgICAgICAgICAgICAgICAgICAgIF8gICAgICAgICAgICAgICAKfCB8ICAgICAgICAgICAgICAgICAgICAgICAgICB8IHwgICAgICAgICAgICAgIAp8IHwgICAgIF9fIF8gXyAgIF8gXyBfXyAgIF9fX3wgfF9fICAgX19fIF8gX18gCnwgfCAgICAvIF9gIHwgfCB8IHwgJ18gXCAvIF9ffCAnXyBcIC8gXyBcfCBfX3wKfCB8X19ffCAoX3wgfCB8X3wgfCB8IHwgfCAoX198IHwgfCB8ICBfXy8gfCAgIApcX19fX18vXF9fLF98XF9fLF98X3wgfF98XF9fX3xffCB8X3xcX19ffF98ICAgIAo9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KJycnCnRyeToKICAgIGltcG9ydCBVc2VyLlVzZXJQcm9maWxlCgogICAgVXNlciA9IFVzZXIuVXNlclByb2ZpbGUuVXNlcm5hbWUKZXhjZXB0OgogICAgcGFzcwpGdW5jdGlvbkxpc3QgPWYnJycKfCAgfCAgIFNTU1NTU1NTU1NTU1NTUyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBBQUEgICAgICAgICBUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVAp8ICB8IFNTOjo6Ojo6Ojo6Ojo6Ojo6UyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQTo6OkEgICAgICAgIFQ6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6OjpUCnwgIHxTOjo6OjpTU1NTU1M6Ojo6OjpTICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIEE6Ojo6OkEgICAgICAgVDo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6OlQKfCAgfFM6Ojo6OlMgICAgIFNTU1NTU1MgICAgICAgICAgICAgICAgICAgICAgICAgIC'
love = 'NtVPNtVPNtVPOOBwb6Bwb6BxRtVPNtVPOHBwb6BwcHIQb6Bwb6BwcHIQb6Bwb6INc8VPO8Hmb6Bwb6HlNtVPNtVUq3q3q3q3ptVPNtVPNtVPNtVUq3q3q3VPNtVPNtVPNtVPO3q3q3q3q3DGb6Bwb6Bwb6BxRtVPNtVSEHISEHIPNtIQb6Bwb6IPNtISEHISEHPajtVUkGBwb6BwcGVPNtVPNtVUp6Bwb6BaptVPNtVPNtVPO3Bwb6Bwc3VPNtVPNtVPNtqmb6Bwb6q0R6Bwb6BxR6Bwb6BxRtVPNtVPNtVPNtVPOHBwb6BwcHVPNtVPNtVPNXsPNtsPOGBwb6ByAGH1ZtVPNtVUp6Bwb6BaptVPNtVPNtqmb6Bwb6Bwc3VPNtVPNtVUp6Bwb6BaqOBwb6BwcOVRR6Bwb6BxRtVPNtVPNtVPNtVSD6Bwb6ByDtVPNtVPNtVNc8VPO8VPOGHmb6Bwb6ByAGH1AGVUp6Bwb6BaptVPNtVUp6Bwb6Bwb6Bwc3VPNtVPO3Bwb6Bwc3DGb6Bwb6DFNtVRR6Bwb6BxRtVPNtVPNtVPNtIQb6Bwb6IPNtVPNtVPNtPajtVUjtVPNtH1AGBwb6Bwb6BwcGH3p6Bwb6BaptVPO3Bwb6Bwc3Bwb6Bwc3VPNtqmb6Bwb6q0R6Bwb6BxRtVPNtVRR6Bwb6BxRtVPNtVPNtVPOHBwb6BwcHVPNtVPNtVPNXsPNtsPNtVPNtVPOGH1AGH1Z6Bwb6H3p6Bwb6Baptqmb6Bwb6qlO3Bwb6Bwc3VUp6Bwb6BaqOBwb6BwcODHSODHSODHR6Bwb6BxRtVPNtVPNtVSD6Bwb6ByDtVPNtVPNtVNc8VPO8VPNtVPNtVPNtVPNtHmb6Bwb6H3p6Bwb6Bap6Bwb6BaptVPO3Bwb6Bwc3Bwb6Bwc3DGb6Bwb6Bwb6Bwb6Bwb6Bwb6Bwb6BxRtVPNtVPNtIQb6Bwb6IPNtVPNtVPNtPajtVUjtVPNtVPNtVPNtVPOGBwb6BwcGVUp6Bwb6Bwb6Bwc3VPNtVPO3Bwb6Bwb6Bwb6q0R6Bwb6BxSODHSODHSODHSODHR6Bwb6BxRtVPNtVPOHBwb6BwcHVPNtVPNtVPNXsPNtsSAGH1AGH1ZtVPNtVSZ6Bwb6ByZtVUp6Bwb6Bwb6qlNtVPNtVPO3Bwb6'
god = 'Ojo6OndBOjo6OjpBICAgICAgICAgICAgIEE6Ojo6OkEgICBUVDo6Ojo6OjpUVCAgICAgIAp8ICB8Uzo6Ojo6OlNTU1NTUzo6Ojo6UyAgIHc6Ojo6OncgICAgICAgICB3Ojo6Ojp3QTo6Ojo6QSAgICAgICAgICAgICAgIEE6Ojo6OkEgIFQ6Ojo6Ojo6OjpUICAgICAgCnwgIHxTOjo6Ojo6Ojo6Ojo6Ojo6U1MgICAgIHc6Ojp3ICAgICAgICAgICB3Ojo6d0E6Ojo6OkEgICAgICAgICAgICAgICAgIEE6Ojo6OkEgVDo6Ojo6Ojo6OlQgICAgICAKfCAgfCBTU1NTU1NTU1NTU1NTU1MgICAgICAgIHd3dyAgICAgICAgICAgICB3d3dBQUFBQUFBICAgICAgICAgICAgICAgICAgIEFBQUFBQUFUVFRUVFRUVFRUVAo9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQp8L3wgICAgICAgICAgICAgV2hhdCdzIHVwIHtVc2VyfSEgICAgICAgCnwvfCAgICAgICAgICAgICBUb2RheToge2RhdGV0aW1lLmRhdGV0aW1lLnRvZGF5KCl9CnwvfCAgICAgICAgICAgICBGcm9tIFRoZSBEZXZzISB7U3lzdGVtLlJlcXVpcmVtZW50cy5GVEQuVmVyc2lvbn0KPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KfC98ICAgICAgICAgICAgIHwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tfC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS18IAp8L3wgICAgICAgICAgICAgfCAxOjogU3dBVCBJbmZvcm1hdGlvbiAgICAgICAgICB8IDU6OiBQYWNrYWdlIExhdW5jaGVyICAgICAgICAgIHwKfC98ICAgICAgICAgICAgIHwtLS0tLS'
destiny = '0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gsP0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF18PajisPNtVPNtVPNtVPNtVPO8VQV6BvOALJ51LJjtD2SwnTHtoJShLJqyoJIhqPNtVUjtAwb6VSOuL2guM2HtIJ5coaA0LJkfMKVtVPNtVPNtsNc8Y3jtVPNtVPNtVPNtVPNtsP0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF18YF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYKjXsP98VPNtVPNtVPNtVPNtVUjtZmb6VSOuL2guM2HtH2I0qTyhM3ZtVPNtVPNtVPNtsPN3BwbtERIJVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO8PajisPNtVPNtVPNtVPNtVPO8YF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYKjgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gsNc8Y3jtVPNtVPNtVPNtVPNtsPN0BwbtHTSwn2SaMFOQo21jnJkypvNtVPNtVPNtVPO8VQt6BvOSrTy0VPNtVPNtVPNtVPNtVPNtVPNtVPNtVUjXsP98VPNtVPNtVPNtVPNtVUjgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gsP0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF18PvpaWjcTqJ5wqTyioy9GMKE0nJ5aplN9VPpaWlNtVPNtVPNtPajtVUjtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOGMKE0nJ5apjb9CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG0XsPNtsPNtVPNtVPNtVPNtVPNtVPO8ZFO8VRyhMz8XsPNtsPNtVPNtVPNtVPNtVPNtVPO8CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CDc8VPO8VPNtVPNtVPNtVPNtVPNtVUjlVUjtIKAypvOGpTIwnJMcLlOGMKE0nJ5apjc8VPO8VPNtVPNtVPNtVPNtVPNtVUj9CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CDbaWlpXPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
