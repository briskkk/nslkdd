
#%%
import  pandas as pd

#%% [markdown]
# ### import data as dataframe format

#%%
nsl_train = pd.read_csv('datasets/NSL-KDD/KDDTrain+.txt',header=None)


#%%
nsl_20 = pd.read_csv('datasets/NSL-KDD/KDDTrain+_20Percent.txt',header=None)


#%%
nsl_test = pd.read_csv('datasets/NSL-KDD/KDDTest+.txt',header=None)


#%%
nsl_test_21 = pd.read_csv('datasets/NSL-KDD/KDDTest-21.txt',header=None)

#%% [markdown]
# ### choose nsl_train&nsl_test as training set and test set 
#%% [markdown]
# ## Three features are nominal: protocol_type, service, flag. Transform them as umeric features.

#%%
service_map ={'aol':'0','auth':'1','bgp':'2','courier':'3','csnet_ns':'4','ctf':'5','daytime':'6','discard':'7','domain':'8',
              'domain_u':'9','echo':'10','eco_i':'11','ecr_i':'12' ,'efs':'13','exec':'14','finger':'15','ftp':'16',
              'ftp_data':'17','gopher':'18','harvest':'19','hostnames':'20','http':'21','http_2784':'22','http_443':'23',
              'http_8001':'24','imap4':'25','IRC':'26','iso_tsap':'27','klogin':'28','kshell':'29','ldap':'30','link':'31',
              'login':'32','mtp':'33','name':'34','netbios_dgm':'35','netbios_ns':'36','netbios_ssn':'37','netstat':'38',
              'nnsp':'39','nntp':'40','ntp_u':'41','other':'42','pm_dump':'43','pop_2':'44','pop_3':'45','printer':'46','private':'47',
              'red_i':'48','remote_job':'49','rje':'50','shell':'51','smtp':'52','sql_net':'53','ssh':'54','sunrpc':'55','supdup':'56',
              'systat':'57', 'telnet':'58','tftp_u':'59','tim_i':'60','time':'61','urh_i':'62','urp_i':'63',
              'uucp':'64','uucp_path':'65','vmnet':'66', 'whois':'67','X11':'68','Z39_50':'69'}

protocol_map = {'tcp':'1','udp':'2','icmp':'0'}
flag_map = {'OTH':'0','REJ':'1','RSTO':'2','RSTOS0':'3','RSTR':'4','S0':'5','S1':'6','S2':'7','S3':'8','SF':'9','SH':'10'}

attack_map = {'normal':'0',
              'ipsweep':'3',
              'mscan':'3',
              'nmap':'3',
              'portsweep':'3',
              'saint':'3',
              'satan':'3',
              'apache2':'4',
              'back':'4',
              'land':'4',
              'mailbomb':'4',
              'neptune':'4',
              'pod':'4',
              'processtable':'4',
              'smurf':'4',
              'teardrop':'4',
              'udpstorm':'4',
              'buffer_overflow':'1',
              'httptunnel':'1',
              'loadmodule':'1',
              'perl':'1',
              'ps':'1',
              'rootkit':'1',
              'sqlattack':'1',
              'xterm':'1',
              'ftp_write':'2',
              'guess_passwd':'2',
              'imap':'2',
              'multihop':'2',
              'named':'2',
              'phf':'2',
              'sendmail':'2',
              'snmpgetattack':'2',
              'snmpguess':'2',
              'spy':'2',
              'warezclient':'2',
              'warezmaster':'2',
              'worm':'2',
              'xlock':'2',
              'xsnoop':'2'}


#%%
def transform(nslkdd):
    nslkdd[41] = nslkdd[41].replace(attack_map)
    nslkdd[2] = nslkdd[2].replace(service_map)
    nslkdd[3] = nslkdd[3].replace(flag_map)
    nslkdd[1] = nslkdd[1].replace(protocol_map)
    return nslkdd


#%%
nsl_train.head()


#%%
pd.value_counts(nsl_train[1])


#%%
pd.value_counts(nsl_train[3])

#%% [markdown]
# ### remove content related features of each network connection vector(No.9-No.21)and difficulty(42)

#%%
nsltrain = pd.read_csv('datasets/NSL-KDD/KDDTrain+.txt', 
                  usecols=[0,1,2,3,4,5,6,7,8,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41] , header=None)
nsltest = pd.read_csv('datasets/NSL-KDD/KDDTest+.txt', 
                  usecols=[0,1,2,3,4,5,6,7,8,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41] , header=None)


#%%
transform(nsltrain)
transform(nsltest)


#%%
pd.value_counts(nsltrain[1])


#%%
pd.value_counts(nsltrain[3])


#%%
pd.value_counts(nsltrain[41])


#%%
pd.value_counts(nsltest[1])


#%%
pd.value_counts(nsltest[3])


#%%
pd.value_counts(nsltest[41])

#%% [markdown]
# ## I don't consider feature reducton first, coding the dataset as onehot format.

#%%
from sklearn.preprocessing  import OneHotEncoder
encoder = OneHotEncoder()
def onehot(self):
    return encoder.fit_transform(self.values.reshape(-1,1)).toarray()


#%%
nsltest.shape, nsltrain.shape


#%%
Traindata = nsltrain.iloc[:,:28]
Trainlabel = nsltrain[41]
Testdata = nsltest.iloc[:,:28]
Testlabel = nsltest[41]


#%%
Testlabel_onehot = onehot(Testlabel)
Testlabel_onehot = pd.DataFrame(Testlabel_onehot)
Testlabel_onehot.to_csv('datasets/testlabel_onehot.csv',index=False,header=False)
Testlabel = pd.DataFrame(Testlabel)
Testlabel.to_csv('datasets/testlabel.csv',index=False,header=False)
Testdata.to_csv('datasets/testdata.csv',index=False,header=False)

Trainlabel_onehot = onehot(Trainlabel)
Trainlabel_onehot = pd.DataFrame(Trainlabel_onehot)
Trainlabel_onehot.to_csv('datasets/trainlabel_onehot.csv',index=False,header=False)
Trainlabel = pd.DataFrame(Trainlabel)
Trainlabel.to_csv('datasets/trainlabel.csv',index=False,header=False)
Traindata.to_csv('datasets/traindata.csv',index=False,header=False)


#%%



