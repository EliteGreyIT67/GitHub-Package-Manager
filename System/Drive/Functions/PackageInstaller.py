

import base64, codecs
magic = 'IyBpbXBvcnQgU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5QYWNrYWdlSW5zdGFsbGVyCiMgZXhlYygnU3lzdGVtLkRyaXZlLkZ1bmN0aW9ucy5QYWNrYWdlSW5zdGFsbGVyJykKZ2xvYmFsIGxhdW5jaAoKCmRlZiBtYWluKCk6CiAgICBwcmludChmJycnCj09PT09PT09PT09PT09PT09cGFja2FnZV9pbnN0YWxsZXI9PT09PT09PT09PT09PT09PT0KMSA9IEZyb20gR2l0SHViIHJlcG86IAo9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CjIgPSBGcm9tIExvY2FsIEZvbGRlcgo9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09JycnKQogICAgUm91dGUgPSBpbnB1dCgnRW50ZXIgVmFsdWUgVG8gQ29udGludWU6ICcpCgogICAgc3BhY2VyID0gJz09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0nCgogICAgaWYgUm91dGUgPT0gJzEnOgoKICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgRVYuTmV3RXZlbnQoZXZlbnQ9ZidJbnN0YWxsIEBHaXRSZXBvJywgUG9sPTEpCgogICAgICAgIGltcG9ydCBvcwogICAgICAgIGN3ZCA9IG9zLmdldGN3ZCgpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBvcy5ta2RpcihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0Rvd25sb2FkcycpCgogICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvRG93bmxvYWRzIDogQ3JlYXRlZCcsIFBvbD0wKQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgcGFzcwogICAgICAgIFNvdXJjZSA9IGN3ZAogICAgICAgIHByaW50KHNwYWNlcikKICAgICAgICBEb3dubG9hZF9Tb3VyY2UgPSBpbnB1dCgnR2l0SHViIFJlcG8gVG8gRG93bmxvYWQgRnJvbTogJykKICAgICAgICBkaXIgPSBmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0Rvd25sb2FkcycKICAgICAgICBvcy5jaGRpcihkaXIpCiAgICAgICAgcHJpbnQoJ1shXSBDaGVja1BvaW50IDF8NCBbIV0nKQoKICAgICAgICBGaWxlcyA9IFtdCiAgICAgICAgZm9yIHBhdGggaW4gb3MubGlzdGRpcihjd2QpOgogICAgICAgICAgICAjIGNoZWNrIGlmIGN1cnJlbnQgcGF0aCBpcyBhIGZpbGUKICAgICAgICAgICAgaWYgb3MucGF0aC5pc2ZpbGUob3MucGF0aC5qb2luKGN3ZCwgcGF0aCkpOgogICAgICAgICAgICAgICAgRmlsZXMuYXBwZW5kKHBhdGgpCgogICAgICAgIFNEaXIgPSBsaXN0KGZpbHRlcihvcy5wYXRoLmlzZGlyLCBvcy5saXN0ZGlyKG9zLmN1cmRpcikpKQoKICAgICAgICB0cnk6ICAjIGRvd25sb2FkaW5nIGZyb20gR2l0SHViCiAgICAgICAgICAgIG9zLnN5c3RlbShmImdpdCBjbG9uZSAne0Rvd25sb2FkX1NvdXJjZX0nIikKCiAgICAgICAgICAgIHByaW50KCdbIV0gQ2hlY2tQb2ludCAyfDQgWyFdJykKICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5FcnJvcnNfRXZlbnRzLkV2ZW50TWFuIGFzIEVWCgogICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0Rvd25sb2FkZWQgZnJvbSBHaXRodWInLCBQb2w9MCkKICAgICAgICAgICAgRmlsZXMxID0gW10KICAgICAgICAgICAgZm9yIHBhdGggaW4gb3MubGlzdGRpcihjd2QpOgogICAgICAgICAgICAgICAgIyBjaGVjayBpZiBjdXJyZW50IHBhdGggaXMgYSBmaWxlCiAgICAgICAgICAgICAgICBpZiBvcy5wYXRoLmlzZmlsZShvcy5wYXRoLmpvaW4oY3dkLCBwYXRoKSk6CiAgICAgICAgICAgICAgICAgICAgRmlsZXMxLmFwcGVuZChwYXRoKQoKICAgICAgICAgICAgU0RpcjEgPSBsaXN0KGZpbHRlcihvcy5wYXRoLmlzZGlyLCBvcy5saXN0ZGlyKG9zLmN1cmRpcikpKQoKICAgICAgICAgICAgZm9yIHggaW4gRmlsZXMxOgogICAgICAgICAgICAgICAgaWYgeCBpbiBGaWxlczoKICAgICAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgogICAgICAgICAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnUGFja2FnZSBEb3dubG9hZGVkOiB7eH0nLCBQb2w9MCkKCiAgICAgICAgICAgIGZvciB5IGluIFNEaXIxOgogICAgICAgICAgICAgICAgaWYgeSBpbiBTRGlyOgogICAgICAgICAgICAgICAgICAgIHBhc3MKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1shXSBDaGVja1BvaW50IDN8NCBbIV0nKQogICAgICAgICAgICAgICAgICAgIGRpcjEgPSBmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0Rvd25sb2Fkcy97eX0nCgogICAgICAgICAgICAgICAgICAgIENoYW5nZURpciA9IGRpcjEKCiAgICAgICAgICAgICAgICAgICAgRmlsZXMwID0gW10KICAgICAgICAgICAgICAgICAgICBmb3IgcGF0aCBpbiBvcy5saXN0ZGlyKGRpcjEpOgogICAgICAgICAgICAgICAgICAgICAgICAjIGNoZWNrIGlmIGN1cnJlbnQgcGF0aCBpcyBhIGZpbGUKICAgICAgICAgICAgICAgICAgICAgICAgaWYgb3MucGF0aC5pc2ZpbGUob3MucGF0aC5qb2luKGRpcjEsIHBhdGgpKToKICAgICAgICAgICAgICAgICAgICAgICAgICAgIEZpbGVzMC5hcHBlbmQocGF0aCkKCiAgICAgICAgICAgICAgICAgICAgcHJpb'
love = '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PNtVPNtVPNtVPNtVPNtVPNtVRAioKOfMKucoaA0LJkfVQ0to3OyovuzW3gwq2E9Y1A5p3EyoF9QLJAbMF9GrKA0MJ0iE2y0FUIvY0AioKOfMKusnJ5mqTSfoPpfVPquWlxXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtD29gpTkyrTyhp3EuoTjhq3WcqTHbqT9ioPxXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtD29gpTkyrRkwLKIhL2thL2kip2HbXDbXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbW0M1oTk5VTyhp3EuoTkyMPRaXDbXVPNtVPNtVPNtVPNtVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOznFN9VRMcoTImZSgcoaDbMzxcVP0tZI0XPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTEup2uWEPN9VSfaHzIkqJImqUZhqUu0WljtW1WypKIcpzIgMJ50pl50rUDaYPNapzIkqJImqUZhqUu0WljtW1WypKIcpzIgMJ50pl50rUDaKDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO0pax6PvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOzo3VtMTSmnPOcovOxLKAbFHD6PvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJLtMTSmnPOcovOTnJkypmN6PvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTEup2ttCFOzW3gxnKVksF97MTSmnU0aPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTEup2tkVQ0tMvqjrKEbo24mVP1gVUOcpPOcoaA0LJkfVP1lVUgxLKAbsFpXVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtqUW5BtbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNto3Zhp3ymqTIgXTEup2tkXDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbW1WypKIcpzIgMJ50plOWoaA0LJkfMJDaXDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOyrTAypUD6PvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOjLKAmPvNtVPNtVPNtVPNtVP'
god = 'AgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KCdObyBSZXF1aXJlbWVudHMgZm91bmQnKQoKICAgICAgICAgICAgICAgICAgICAgICAgY2ggPSAnLicKICAgICAgICAgICAgICAgICAgICAgICAgIyBSZW1vdmUgYWxsIGNoYXJhY3RlcnMgYmVmb3JlIHRoZSBjaGFyYWN0ZXIgJy0nIGZyb20gc3RyaW5nCiAgICAgICAgICAgICAgICAgICAgICAgIGxpc3RPZldvcmRzID0gZmkuc3BsaXQoY2gsIDEpCiAgICAgICAgICAgICAgICAgICAgICAgIGlmIGxlbihsaXN0T2ZXb3JkcykgPiAwOgogICAgICAgICAgICAgICAgICAgICAgICAgICBmZmkgPSBsaXN0T2ZXb3Jkc1sxXQoKCgoKCiAgICAgICAgICAgICAgICAgICAgICAgIGlmIGZmaSA9PSAncHknOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF1bmNoID0gZicmcHl0aG9uMyB7Zml9JwoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpZXIgPSBmJyZweXRob24zIHtkaXIxfS97Zml9JwogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1shXSBDaGVja1BvaW50IDR8NCBbIV0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQobGF1bmNoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgRm9ybSA9IGYne0NoYW5nZURpcn1Ae2ZpWzotM119ID0ge2xhdW5jaH0nCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0xhdW5jaCBDb21tYW5kIENyZWF0ZWQ6IHtGb3JtfScsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgb3MuY2hkaXIoU291cmNlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgY3dkZCA9IG9zLmdldGN3ZCgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmID0gb3BlbihmJ3tjd2RkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9JbnQudHh0JywgJ2EnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZi53cml0ZShmJ1xue0Zvcm19JykKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ0luc3RhbGxhdGlvbiBDb21wbGV0ZSEnKQoKICAgICAgICAgICAgICAgICAgICAgICAgZWxpZiBmZmkgPT0gJ2MnOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF1bmNoID0gZicmZ2NjIHtmaX0nCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1shXSBDaGVja1BvaW50IDR8NCBbIV0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQobGF1bmNoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgRm9ybSA9IGYne0NoYW5nZURpcn1Ae2ZpWzotM119ID0ge2xhdW5jaH0nCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLkVycm9yc19FdmVudHMuRXZlbnRNYW4gYXMgRVYKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBFVi5OZXdFdmVudChldmVudD1mJ0xhdW5jaCBDb21tYW5kIENyZWF0ZWQ6IHtGb3JtfScsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgb3MuY2hkaXIoU291cmNlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgY3dkZCA9IG9zLmdldGN3ZCgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmID0gb3BlbihmJ3tjd2RkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9JbnQudHh0JywgJ2EnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZi53cml0ZShmJ1xue0Zvcm19JykKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ0luc3RhbGxhdGlvbiBDb21wbGV0ZSEnKQoKICAgICAgICAgICAgICAgICAgICAgICAgZWxpZiBmZmkgPT0gJ2NwcCc6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXVuY2ggPSBmJyZnKysge2ZpfScKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCgnWyFdIENoZWNrUG9pbnQgNHw0IFshXScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludChsYXVuY2gpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBGb3JtID0gZid7Q2hhbmdlRGlyfUB7ZmlbOi0zXX0gPSB7bGF1bmNofScKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuRXJyb3JzX0V2ZW50cy5FdmVudE1hbiBhcyBFVgoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIEVWLk5ld0V2ZW50KGV2ZW50PWYnTGF1bmNoIENvbW1hbmQgQ3JlYXRlZDoge0Zvcm19JywgUG9sPTApCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBvcy5jaGRpcihTb3VyY2UpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjd2RkID0gb3MuZ2V0Y3dkKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKGYne2N3ZGR9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0ludC50eHQnLCAnYScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmLndyaXRlKGYnXG57Rm9ybX0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZi5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCgnSW5zdGFsbGF0aW9uIENvbXBsZXRlIScpCgogICAgICAgICAgICAgICAgICAgICAgICBlbGlmIGZmaSA9PSAnc2gnOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF1bmN'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
