# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IwoKaW1wb3J0IG9zCmltcG9ydCBzeXMKCgpkZWYgQWxsKCk6CiAgICBjd2QgPSBvcy5nZXRjd2QoKQoKICAgIHNwYWNlciA9ICc9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09JwoKICAgIHByaW50KCc9PT09PT09PT09PT09PT09PUF2YWlsYWJsZV9QYWNrYWdlcz09PT09PT09PT09PT09PT09JykKICAgIHByaW50KCdMb2NhbCA6IDEnKQogICAgcHJpbnQoJ0dpdEh1YiA6IDInKQogICAgaW5wID0gTm9uZQogICAgaW5wID0gaW50KGlucHV0KCdFbnRlciB2YWx1ZSB0byBjb250aW51ZTogJykpCgoKICAgIGlmIGlucCA9PSAyOgoKICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0lucCA9IEdpdEh1YicsIFBvbD0xKQoKICAgICAgICB3aXRoIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9pbnQudHh0JywgJ3InKSBhcyByLCBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvaW50Mi50eHQnLCAndycpIGFzIG86CiAgICAgICAgICAgIGZvciBsaW5lIGluIHI6CiAgICAgICAgICAgICAgICBpZiBsaW5lLnN0cmlwKCk6CiAgICAgICAgICAgICAgICAgICAgby53cml0ZShsaW5lKQoKICAgICAgICBmID0gb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL2ludDIudHh0JywgInIiKQogICAgICAgIGUgPSBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvQ29tcGxleDInLCAiciIpCiAgICAgICAgbGluZXMgPSBmLnJlYWRsaW5lcygpCiAgICAgICAgY291bnQgPSAwCiAgICAgICAgZm9yIGxpbmUgaW4gbGluZXM6CiAgICAgICAgICAgIGNvdW50ICs9IDEKCiAgICAgICAgY291bnQxID0gMAogICAgICAgIGZvciBsaW5lIGluIGxpbmVzOgogICAgICAgICAgICB2YWx1ZTQgPSBsaW5lLnN0cmlwKCkKICAgICAgICAgICAgVmFsID0gdmFsdWU0LnNwbGl0KCcmJywgMSkKICAgICAgICAgICAgaWYgbGVuKFZhbCkgPiAwOgogICAgICAgICAgICAgICAgdmFsdWU0ID0gVmFsWzFdCiAgICAgICAgICAgIGNvdW50MSArPSAxCgogICAgICAgICAgICBwcmludCgie30gfCB7fSIuZm9ybWF0KGNvdW50MSwgdmFsdWU0KSkKICAgICAgICAgICAgcHJpbnQoc3BhY2VyKQoKICAgICAgICBsaW5lczIgPSBlLnJlYWRsaW5lcygpCiAgICAgICAgZm9yIGxpbmUyIGluIGxpbmVzMjoKICAgICAgICAgICAgY291bnQxICs9IDEKICAgICAgICAgICAgcHJpbnQoInt9IHwge30iLmZvcm1hdChjb3VudDEsIGxpbmUyKSkKCiAgICAgICAgdmFsdWVlID0gaW5wdXQoJ0VudGVyIGEgdmFsdWUgdG8gY29udGludWU6ICcpCiAgICAgICAgIyByZW1vdmUgYSBsaW5lIGNvbnRhaW5pbmcgYSBzdHJpbmcKCiAgICAgICAgaWYgaW50KHZhbHVlZSkgPiBjb3VudDoKICAgICAgICAgICAgZHIgPSBpbnQodmFsdWVlKS1jb3VudAogICAgICAgICAgICBjb21tYW5kID0gbGluZXMyW2RyLTFdCiAgICAgICAgICAgIHByaW50KGNvbW1hbmQpCiAgICAgICAgICAgIGNvID0gY29tbWFuZC5zcGxpdCgnJCcsIDEpWzBdCiAgICAgICAgICAgIHByaW50KGNvKQogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKICAgICAgICAgICAgICAgIGltcG9ydCBzaHV0aWwKCiAgICAgICAgICAgICAgICBzaHV0aWwucm10cmVlKGNvKQoKICAgICAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgogICAgICAgICAgICAgICAgcHJpbnQoZidQcm9qZWN0IFJlbW92ZWQge2NvfScpCiAgICAgICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0RpclJlbW92YWwgPSBTdWNjZXNzISB7Y299JywgUG9sPTApCgogICAgICAgICAgICBleGNlcHQ'
love = '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'
god = 'ogICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnSW5wID0gTG9jYWwnLCBQb2w9MSkKCiAgICAgICAgZiA9IG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsL0ludDIucHknLCAncicpCgogICAgICAgIHdpdGggb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vTG9jYWwvSW50LnB5JywgJ3InKSBhcyByLCBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9Mb2NhbC9JbnQyLnB5JywndycpIGFzIG86CiAgICAgICAgICAgIGZvciBsaW5lIGluIHI6CiAgICAgICAgICAgICAgICBpZiBsaW5lLnN0cmlwKCk6CiAgICAgICAgICAgICAgICAgICAgby53cml0ZShsaW5lKQogICAgICAgIGYgPSBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9Mb2NhbC9JbnQyLnB5JywgInIiKQoKICAgICAgICBsaW5lcyA9IGYucmVhZGxpbmVzKCkKICAgICAgICBjb3VudCA9IDAKICAgICAgICBmb3IgbGluZSBpbiBsaW5lczoKICAgICAgICAgICAgY291bnQgKz0gMQoKICAgICAgICBjb3VudDEgPSAwCiAgICAgICAgZm9yIGxpbmUgaW4gbGluZXM6CiAgICAgICAgICAgIGNvdW50MSArPSAxCiAgICAgICAgICAgIHByaW50KCJ7fSB8IHt9Ii5mb3JtYXQoY291bnQxLCBsaW5lLnN0cmlwKCkpKQogICAgICAgICAgICBwcmludChzcGFjZXIpCiAgICAgICAgICAgIGlmIGNvdW50MSA9PSBjb3VudDoKCiAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgICAgICB2YWx1ZWUgPSBpbnB1dCgnRW50ZXIgYSB2YWx1ZSB0byBjb250aW51ZTogJykKICAgICAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYndmFsdWVlID17dmFsdWVlfScsIFBvbD0wKQogICAgICAgICAgICAgICAgdmFsdWUgPSBsaW5lc1tpbnQodmFsdWVlKSAtIDFdCiAgICAgICAgICAgICAgICBsaXN0T2ZXb3JkcyA9IHZhbHVlLnNwbGl0KCctJywgMSkKCiAgICAgICAgICAgICAgICBpZiBsZW4obGlzdE9mV29yZHMpID4gMDoKICAgICAgICAgICAgICAgICAgICB2YWx1ZWcgPSBsaXN0T2ZXb3Jkc1sxXQoKICAgICAgICAgICAgICAgIHdpdGggb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vTG9jYWwvSW50LnB5JywgJ3InKSBhcyBmaWxlOgogICAgICAgICAgICAgICAgICAgIGxpbmVzNTUgPSBmaWxlLnJlYWRsaW5lcygpCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgd2l0aCBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9Mb2NhbC9JbnQucHknLCAndycpIGFzIGZpbGU6CiAgICAgICAgICAgICAgICAgICAgICAgIGZvciBsaW5lZmYgaW4gbGluZXM1NToKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIGxpbmVmZi5maW5kKHZhbHVlKSAhPSAtMToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZpbGUud3JpdGUobGluZWZmKQogICAgICAgICAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgogICAgICAgICAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnTGF1bmNoIENvbW1hbmQgUmVtb3ZlZCcsIFBvbD0wKQoKICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKICAgICAgICAgICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0xhdW5jaCBDb21tYW5kIEZhaWxlZCBUbyBSZW1vdmUnLCBQb2w9MCkKCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgdmFsdWUxID0gdmFsdWUuc3BsaXQoZictJywgMSlbMF0KICAgICAgICAgICAgICAgICAgICBTdHIgPSB2YWx1ZTFbOmxlbih2Y'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
