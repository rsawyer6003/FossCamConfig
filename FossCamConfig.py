from WSDiscovery import WSDiscovery, QName, Scope

wsd = WSDiscovery()
wsd.start()

ttype = QName("abc", "def")

ttype1 = QName("namespce", "myTestService")
scope1 = Scope("http://myscope")
ttype2 = QName("namespace", "myOtherTestService_type1")
scope2 = Scope("http://other_scope")

xAddr = "localhost:8080/abc"
wsd.publishService(types=[ttype], scopes=[scope2], xAddrs=[xAddr])

#ret = wsd.searchServices(scopes=[scope1], timeout=10)
ret = wsd.searchServices()

for service in ret:
	print(service.getEPR() + ":" + service.getXAddrs()[0])
print("Done")

wsd.stop()
