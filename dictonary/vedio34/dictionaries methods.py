ep1 ={122: 'python', 123: 'java', 124: 'c++'}
ep2 = {125: 'javascript', 126: 'ruby', 127: 'go'}
ep1.update(ep2) # update ka mtlb dono dict ka union sa ho gya ladle
print(ep1)
ep1.pop(122) # pop ka mtlb nikal ke fenk de 
print(ep1)
# agr mujhe last vala item htana h to item ka nam likhne ki jrurt nhi h bs seedha popitem() method use kr skte h
ep1.popitem()
print(ep1)
# esme bhi del hota h
del ep1[123]
# ya to m koi keyword delete kr skta hu
print(ep1)
print(ep1[124])
# del ep1 # ye error dega
# ya fir m pura dictionary delete kr skta hu

# agr m chahata hu ki meri dict hi clear ho jaya mtlb astitv nhi mile lekin andr se khatam ho jay (pyari smjh gyi....) to clear use krunga
ep1.clear()
print(ep1)