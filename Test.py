import os
import sys
libpath="/usr/share/suf/csufc/gui/scripts/lib"
modulepath = os.path.join(libpath, "pypkg", "psqlmodule", "psycopg2")
sys.path.insert(0, modulepath)
import psycopg2 as pg

dbname='csaf'
dbhost='localhost'
dbuser='postgres'
dbport='5432'
dbp='Eric@123'

conn = pg.connect(host=dbhost, database=dbname, user=dbuser, password=dbp, port=dbport)
cur = conn.cursor()

def writetofile(output,filename):
    with open(filename, "w+") as tgt:
        for i in output:
            lt = [str(x) if x is not None else "" for x in i]
            line = ",".join(lt)
            tgt.write(line + "\n")

def fetchtasklist(parenttaskid, outfile):
    ParentTaskId = parenttaskid
    cur.execute("select task_id,task_name,task_type from csaf_re_sub_job_task_detail crsjtd where parent_job_id = '{}' and sub_job_id = '{}' and parent_task_id = '{}' order by sr_no".format(ParentJobId, SubJobId, ParentTaskId))
    out = cur.fetchall()
    fname = SubJobHome + outfile
    writetofile(out, fname)

def fetchsubsubtasklist(parenttaskid, outfile):
    ParentTaskId = parenttaskid
    cur.execute("select func_get_sub_sub_task_upgrade({},{},{})".format(ParentJobId, SubJobId, ParentTaskId))
    out = cur.fetchall()
    fname = SubJobHome + outfile
    out1 = []
    out2 = []
    print(fname)
    for i in out:
        out2 = i[0].replace("(", "").replace(")","").replace('"','').split(",")
        out1.append(out2)
    writetofile(out1, fname)

if sys.argv[1] == 'init':
    ParentJobName = sys.argv[2]
    SubJobName = sys.argv[3]
    OfferingTypeId = sys.argv[4]
    SubOfferingId = sys.argv[5]
    cur.execute("select parent_job_id from csaf_re_parent_job_detail where parent_job_name='{}'".format(ParentJobName))
    ParentJobId=cur.fetchall()[0][0]
    cur.execute("select sub_job_id from csaf_re_sub_job_detail where parent_job_id='{}' and sub_job_name='{}' and offering_type_id='{}' and sub_offering_id='{}'".format(ParentJobId,SubJobName,OfferingTypeId,SubOfferingId))
    SubJobId=cur.fetchall()[0][0]
    cur.execute("select club_key from csaf_re_sub_job_detail where parent_job_id='{}' and sub_job_id='{}' and offering_type_id='{}' and sub_offering_id='{}'".format(ParentJobId,SubJobId,OfferingTypeId,SubOfferingId))
    ClubKey=cur.fetchall()[0][0]
    cur.execute("select func_get_entity_details('{}')".format(ClubKey))
    entity = cur.fetchall()[0][0]
    NodeType = entity.split('|')[0].replace(" ","")
    ActionType = entity.split('|')[1].replace(" ","")
    EnvType = entity.split('|')[2].replace(" ","")
    HwType = entity.split('|')[3].replace(" ","")
    DestIcp = entity.split('|')[4].replace(" ","")
    SubOffering = entity.split('|')[5].replace(" ","")
    SubJobHome = "/usr/share/suf/csufc/gui/jobs/" + ParentJobName + "/" + NodeType + "/" + SubJobName + "/"
    print (SubJobHome)
    print ("ParentJobId={}".format(ParentJobId))
    print ("SubJobId={}".format(SubJobId))
    print ("ClubKey={}".format(ClubKey))
    print ("NodeType={}".format(NodeType))
    print ("ActionType={}".format(ActionType))
    print ("EnvType={}".format(EnvType))
    print ("HwType={}".format(HwType))
    print ("DestIcp={}".format(DestIcp))
    print ("Suboffering={}".format(SubOffering))

    if ActionType == "Installation":
        fetchtasklist(1,"validation_task.cfg")
        fetchtasklist(13,"installation_task.cfg")
        print ("###Fetching_Software_Start###")
        cur.execute("select sw_type,sw_name,sw_cksum from csaf_m_sw_details where club_key='{}'".format(ClubKey))
        out = cur.fetchall()
        for i in out:
            lt = [str(x).replace(" ", "") if x is not None else "" for x in i]
            print ('|'.join(lt))
        print("###Fetching_Software_End###")
    elif ActionType == "Upgrade":
        if NodeType != "NGVS":
            if NodeType == "SDP":
                fetchtasklist(72, "final_task.cfg")
            elif NodeType == "AIR":
                fetchtasklist(114,"final_task.cfg")
            fetchtasklist(69, "validation_task.cfg")
            fetchtasklist(70, "offline_task.cfg")
            fetchtasklist(71, "online_task.cfg")
            fetchsubsubtasklist(78, "conf_backup.cfg")
            fetchsubsubtasklist(95, NodeType + "_Checks.cfg")
            fetchsubsubtasklist(98, "pre_prep.cfg")
            fetchsubsubtasklist(102, "pre_upgrade.cfg")
            fetchsubsubtasklist(106, "post_upgrade.cfg")
        elif NodeType == "NGVS":
            fetchtasklist(183, "validation_task.cfg")
            fetchtasklist(187, "common_offline.cfg")
            fetchtasklist(196, "common_offline_maint.cfg")
            fetchtasklist(203, "clusterwise.cfg")
            fetchtasklist(206, "postupgrade.cfg")
            fetchtasklist(209, "firmware.cfg")
            fetchtasklist(211, "conf_after.cfg")
            fetchtasklist(218, "cleanup.cfg")
            fetchsubsubtasklist(193, "NGVS_Checks.cfg")
            fetchsubsubtasklist(192, "NGVS_conf_backup.cfg")
            cur.execute("select count(*) from csaf_re_sub_job_task_detail where parent_job_id = {} and sub_job_id= '{}' and task_id=200".format(ParentJobId,SubJobId))
            count = cur.fetchall()[0][0]
            for node in range(1,count+1):
                cur.execute("select task_id,task_name,task_type from csaf_re_sub_job_task_detail crsjtd where parent_job_id = '{}' and sub_job_id = '{}' and parent_task_id = 199 and node_number = {} order by sr_no".format(ParentJobId, SubJobId, node))
                out = cur.fetchall()
                fname = SubJobHome + "Node" + str(node) + "_online_task.cfg"
                writetofile(out, fname)
    conn.close()
    sys.exit()

if sys.argv[1] == 'getlist':
    query = sys.argv[2]
    cur.execute(query)
    out = cur.fetchall()
    for i in out:
        lt = [str(j) if j is not None else "" for j in i]
        print (','.join(lt))



