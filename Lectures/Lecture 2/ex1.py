# if(x > 5){
    
# }

# while True:    
#     if 5 > 4:
#         print("Five is more than 4")
#     else:
#         print("It's incorrect")
        
l = [1,2,3,4,5,6,'python','is','better','that','c++']
s = 'abcdefg'
print(type(l))
# for i in range(len(l)): #11 -> [0;11)
#     print(l[i])
    # print(i)
    
# for(int i = n-1; i>=0; i--){
#     cout << arr[i] << " ";
# }
   
length = len(l) - 1 #10
# while length >= 0:
#     print(l[length], end=" ")
#     length -= 1
    
# print(l[:-10])
l1 = [101,100,99,1,2,3,4,5]
l2 = [6,7,8,9,10]
# l3 -> [1; 10]
l3 = l1 + l2
# print(sorted(l3))
l3[4] = 11
# print(*l3)

# letters = ['a','b','c','d','e','f']
# letters.append('g')
# print(letters[::-1])

'''
int n = 0;
cin >> n;
int arr[n];
for(int i=0; i<n; i++){
    cin >> arr[i];
}
'''
'''
1
2
3
4
5
6
input() -> str
int()
append()
'''
# l1 = []
# s = input().split(' ')
# print(int(s))
# for i in s:
#     l1.append(int(i))
# l1.append([1,2,3,4,5])
# print(l1[6][3])
# n = int(input())
# for i in range(n):
#     l1.append(int(input()))
# print(*l1)
'''
1
2
3
4
5
[1, 2, 3, 4, 5]
'''
l1 = [1,2,3]
# l2 = l1
# l1.clear()
# print(l2)
# l1[1] = 11
# print(l2)
# l2 = [4,5,6]
# #l3 = l1 + l2
# l1.extend(l2)
# print(l1)
# l1.insert(2,[1,2,3,4,5])
# print(l1)
# l1.remove(2)
# print(l1)

# tup = (1,2,3,4,)
# # RGB -> pygame
# tup = (1,)
# print(type(tup))

data = {
"totalCount": "400",
"imdata": [
{
    "l1PhysIf": {
        "attributes": {
            "adminSt": "up",
            "autoNeg": "on",
            "brkoutMap": "none",
            "bw": "0",
            "childAction": "",
            "delay": "1",
            "descr": "",
            "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
            "dot1qEtherType": "0x8100",
            "ethpmCfgFailedBmp": "",
            "ethpmCfgFailedTs": "00:00:00:00.000",
            "ethpmCfgState": "0",
            "fecMode": "inherit",
            "id": "eth1/33",
            "inhBw": "unspecified",
            "layer": "Layer3",
            "lcOwn": "local",
            "linkDebounce": "100",
            "linkLog": "default",
            "mdix": "auto",
            "medium": "broadcast",
            "modTs": "2016-11-28T16:03:29.317-05:00",
            "mode": "trunk",
            "monPolDn": "uni/fabric/monfab-default",
            "mtu": "9150",
            "name": "",
            "pathSDescr": "",
            "portT": "fab",
            "prioFlowCtrl": "auto",
            "qiqL2ProtTunMask": "",
            "routerMac": "not-applicable",
            "snmpTrapSt": "enable",
            "spanMode": "not-a-span-dest",
            "speed": "inherit",
            "status": "",
            "switchingSt": "disabled",
            "trunkLog": "default",
            "usage": "fabric,fabric-ext"
        }
    }
}
]
}

# print(data['imdata'])
basket = {'a', 'b', 'c', 'd', 'e', 'a', 'e'}
print(*basket)